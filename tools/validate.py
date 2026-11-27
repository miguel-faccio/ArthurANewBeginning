"""Validate Content Patcher source and the artwork supplied for a release."""
import argparse
from collections import deque
import json
from pathlib import Path
import re
import struct
import sys
from xml.etree import ElementTree
import zlib

PROJECT = Path(__file__).resolve().parents[1]
PACK = PROJECT / "[CP] Arthur - A New Beginning"
BASE = {"assets/portraits/ArthurANB.png", "assets/characters/ArthurANB.png"}
NPC = "ArthurANB"
MOD = "ArthurANewBeginning.Content"
NATIVE = {"Mountain", "Town", "SeedShop", "Forest", "ArchaeologyHouse", "Saloon", "Beach", "BusStop"}
TOKENS = re.compile(r"\{\{i18n:([^{}]+)\}\}")

def require(condition, message):
    if not condition:
        raise ValueError(message)

def unique_object(pairs):
    values = {}
    for key, value in pairs:
        require(key not in values, f"Chave JSON duplicada: {key}")
        values[key] = value
    return values

def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=unique_object)

def check_png(path, expected):
    raw = path.read_bytes()
    require(raw.startswith(b"\x89PNG\r\n\x1a\n"), f"{path.name}: assinatura PNG inválida")
    cursor = 8
    chunks = set()
    compressed = bytearray()
    while cursor + 12 <= len(raw):
        size, kind = struct.unpack_from(">I4s", raw, cursor)
        end = cursor + size + 12
        require(end <= len(raw), f"{path.name}: bloco truncado")
        payload = raw[cursor + 8:end - 4]
        crc, = struct.unpack_from(">I", raw, end - 4)
        require(zlib.crc32(kind + payload) == crc, f"{path.name}: CRC inválido")
        if not chunks:
            require(kind == b"IHDR" and size == 13, f"{path.name}: cabeçalho inválido")
            width, height, depth, mode, compression, filtering, interlace = struct.unpack(">IIBBBBB", payload)
            require([width, height] == expected, f"{path.name}: dimensões esperadas {expected}")
            require((depth, mode, compression, filtering, interlace) == (8, 6, 0, 0, 0),
                    f"{path.name}: exporte PNG RGBA 8 bits sem entrelaçamento")
        require(kind != b"acTL", f"{path.name}: PNG animado")
        if kind == b"IDAT":
            compressed.extend(payload)
        cursor = end
        chunks.add(kind)
        if kind == b"IEND":
            require(size == 0 and cursor == len(raw), f"{path.name}: final PNG inválido")
            break
    require({b"IHDR", b"IDAT", b"IEND"} <= chunks, f"{path.name}: PNG incompleto")
    stride = 1 + 4 * expected[0]
    length = stride * expected[1]
    decoder = zlib.decompressobj()
    pixels = decoder.decompress(compressed, length + 1)
    require(decoder.eof and not decoder.unused_data and len(pixels) == length, f"{path.name}: fluxo PNG inválido")
    require(all(value <= 4 for value in pixels[::stride]), f"{path.name}: filtro PNG inválido")

def patches(documents, file="content.json", trail=()):
    require(file not in trail, f"Include circular: {file}")
    require(file in documents, f"Include ausente: {file}")
    for patch in documents[file]["Changes"]:
        if patch["Action"] == "Include":
            yield from patches(documents, patch["FromFile"], (*trail, file))
        else:
            yield patch

def map_data(path):
    node = ElementTree.parse(path).getroot()
    width, height = (int(node.attrib[k]) for k in ("width", "height"))
    require(node.get("tilewidth") == node.get("tileheight") == "16", f"{path.name}: tamanho de tile inválido")
    gids = {0}
    for sheet in node.findall("tileset"):
        first, count = int(sheet.get("firstgid")), int(sheet.get("tilecount"))
        require(sheet.find("image").get("source") in {".townInterior.png", ".spring_outdoorsTileSheet.png", ".paths.png"},
                f"{path.name}: tilesheet fora do inventário")
        gids.update(range(first, first + count))
    layers = {}
    for layer in node.findall("layer"):
        cells = [int(x) for x in layer.find("data").text.split(",")]
        require(len(cells) == width * height and set(cells) <= gids, f"{path.name}: camada inválida")
        layers[layer.attrib["name"]] = cells
    require({"Back", "Buildings", "Front"} <= layers.keys(), f"{path.name}: camadas ausentes")
    walkable = {(i % width, i // width) for i, tile in enumerate(layers["Back"]) if tile and not layers["Buildings"][i]}
    return {prop.get("name"): prop.get("value") for prop in node.findall("./properties/property")}, walkable

def reachable(start, walkable):
    found = {start}
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for point in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if point in walkable and point not in found:
                found.add(point)
                queue.append(point)
    return found

def time(value):
    return 600 <= value <= 2600 and value % 100 < 60 and value % 10 == 0

def check_schedules(variants, maps, animations):
    base = variants[0]
    require("spring" in base, "Rotina spring ausente")
    for variant in variants:
        for key, script in variant.items():
            if script.startswith("GOTO "):
                dest = script[5:]
                require(dest in base and not base[dest].startswith("GOTO "), f"GOTO inválido em {key}")
                continue
            last = 0
            for step in script.split("/"):
                hour, where, x, y, facing, *anim = step.split()
                hour, x, y, facing = map(int, (hour, x, y, facing))
                require(time(hour) and hour > last and 0 <= facing <= 3, f"Horário/direção inválidos em {key}")
                require(where in NATIVE or (x,y) in maps.get(where, set()), f"Destino inválido em {key}: {step}")
                require(not anim or anim[0] in animations, f"Animação ausente em {key}")
                last = hour

def check_events(events, maps, translations):
    ids = {}
    parents = {}
    count = 0
    for where, key, script in events:
        event_id, *tests = key.split("/")
        require(event_id.startswith(MOD+"_") and event_id not in ids, f"ID repetido ou inválido: {event_id}")
        ids[event_id] = where
        parents[event_id] = [test.split()[1] for test in tests if test.startswith("SawEvent ")]
        for token in TOKENS.findall(script):
            require(all(not any(c in t[token] for c in '/"') for t in translations), f"Separador de script em {token}")
        if not tests:
            continue
        count += 1
        for test in tests:
            if test.startswith("Time "):
                start, end = map(int, test.split()[1:])
                require(time(start) and time(end) and start < end, f"Janela de evento inválida: {key}")
        fields = script.split("/")
        actors = fields[2].split()
        require(len(actors) % 4 == 0 and "skippable" in fields, f"Cena sem atores válidos ou opção de pular: {key}")
        tiles = {actors[i]: tuple(map(int, actors[i+1:i+3])) for i in range(0, len(actors), 4)}
        require(set(tiles.values()) <= maps[where], f"Posição inicial bloqueada em {key}")
        for cmd in fields[3:]:
            verb, *args = cmd.split()
            if verb == "move":
                actor, dx, dy, _ = args
                x, y = tiles[actor]
                dest = (x + int(dx), y + int(dy))
                require(dest in maps[where], f"Movimento bloqueado em {key}")
                tiles[actor] = dest
            if verb == "end" and args[0] == "position":
                require(tuple(map(int, args[1:])) in maps[where], f"Saída bloqueada em {key}")
    def visit(event_id, trail=()):
        require(event_id in ids and event_id not in trail, f"Pré-requisito ausente ou ciclo: {event_id}")
        for parent in parents[event_id]:
            visit(parent, (*trail, event_id))
    for event_id in ids:
        visit(event_id)
    for where, key, script in events:
        for fork in re.findall(r"/fork ([^ /]+)", script):
            require(ids.get(fork) == where, f"Fork ausente: {key}")
    return count

def check_project(release=False):
    docs = {p.relative_to(PACK).as_posix(): read_json(p) for p in PACK.rglob("*.json")}
    manifest, content, art = (docs[k] for k in ("manifest.json", "content.json", "asset-manifest.json"))
    require(manifest["UniqueID"] == MOD and manifest["ContentPackFor"]["UniqueID"] == "Pathoschild.ContentPatcher",
            "Manifesto inválido")
    require(content["Format"] == manifest["ContentPackFor"]["MinimumVersion"], "Versão de Content Patcher divergente")
    locales = [docs[f"i18n/{loc}.json"] for loc in ("default", "pt")]
    require(locales[0].keys() == locales[1].keys(), "Traduções sem par")
    for dictionary in locales:
        for key, text in dictionary.items():
            require(text.strip() and all(int(i) < 12 for i in re.findall(r"\$(\d+)", text)), f"Texto ou expressão inválida: {key}")
    require({name for name,spec in art.items() if spec["required"]} == BASE, "Inventário base divergente")
    conditions = {"HasFile:"+name:True for name in BASE}
    require(all(p["Action"] == "Include" and conditions.items() <= p["When"].items() for p in content["Changes"]),
            "Um módulo raiz está ativo sem as folhas-base")
    switches = content["ConfigSchema"]
    for key in switches:
        require(f"config.{key}.description" in locales[0], f"Descrição de configuração ausente: {key}")
    maps, props, schedules, events, animations, loads = {}, {}, [], [], {}, set()
    for patch in patches(docs):
        action, target, when = patch["Action"], patch["Target"], patch.get("When",{})
        for key, value in when.items():
            if key.startswith("Enable"):
                require(key in switches and isinstance(value,bool), f"Configuração inválida: {key}")
            if key.startswith("HasFile:"):
                require(key[8:] in art and value is True, f"Asset fora do inventário: {key}")
        for token in TOKENS.findall(json.dumps(patch, ensure_ascii=False)):
            require(token in locales[0], f"Tradução ausente: {token}")
        if action == "Load":
            path = patch["FromFile"]
            if path.endswith(".png"):
                require(path in art and when.get("HasFile:"+path) is True, f"PNG sem proteção: {path}")
                loads.add(path)
            else:
                require((PACK/path).is_file(), f"Arquivo ausente: {path}")
            if path.endswith(".tmx"):
                where = target.split("/")[-1]
                props[where],maps[where] = map_data(PACK/path)
        if action == "EditData" and target == f"Characters/schedules/{NPC}":
            schedules.append(patch["Entries"])
        if action == "EditData" and target.startswith("Data/Events/"):
            events.extend((target.split("/")[-1],key,value) for key,value in patch["Entries"].items())
        if target == "Data/animationDescriptions":
            animations.update(patch["Entries"])
    require(loads == art.keys(), "Referências PNG divergentes")
    for where, properties in props.items():
        for key in ("Warp", "NPCWarp"):
            fields = properties.get(key,"").split()
            require(len(fields) % 5 == 0, f"Warp malformado em {where}")
            for i in range(0,len(fields),5):
                x,y,dest,dx,dy = fields[i:i+5]
                require((int(x),int(y)) in maps[where], f"Warp bloqueado em {where}")
                require(dest in NATIVE or (int(dx),int(dy)) in maps.get(dest,set()), f"Destino inválido em {where}")
        if where in {NPC+"_House",NPC+"_Lookout"}:
            require(reachable((8,10),maps[where]) == maps[where], f"Piso desconectado em {where}")
    for key,script in animations.items():
        require(all(0 <= int(frame) < 52 for frame in " ".join(script.split("/")[:3]).split()), f"Quadro inválido: {key}")
    check_schedules(schedules,maps,animations)
    count = check_events(events,maps,locales)
    absent = sorted(path for path in BASE if not (PACK/path).is_file())
    for path,spec in art.items():
        asset = PACK/path
        if asset.is_file():
            check_png(asset,spec["size"])
        elif path not in BASE:
            require(not any((PACK/sibling).is_file() for sibling in art if Path(sibling).stem == asset.stem),
                    f"Contraparte ausente: {path}")
    texts = sum(not k.startswith(("config.","location.","npc.")) for k in locales[0])
    print(f"Validação estática: {len(docs)} JSON, {len(maps)} TMX, {count} eventos, {len(schedules[0])} chaves de rotina, {texts} textos por idioma.")
    if absent:
        print("PNGs obrigatórios pendentes: "+", ".join(absent))
    return 2 if release and absent else 0

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release", action="store_true")
    args = parser.parse_args()
    try:
        return check_project(args.release)
    except (ValueError, KeyError, OSError, ElementTree.ParseError, zlib.error) as error:
        print(f"Falha de validação: {error}",file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())

"""Package the installable Content Patcher mod after checking required artwork."""
import argparse
from pathlib import Path
import sys
from zipfile import ZipFile, ZIP_DEFLATED
import zlib

from validate import PACK, check_project

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    destination = args.destination.resolve()
    if destination.suffix.lower() != ".zip" or destination.is_relative_to(PACK):
        parser.error("Escolha um arquivo .zip fora do pack.")
    try:
        result = check_project(release=True)
        if result:
            return result
        with ZipFile(destination,"x",compression=ZIP_DEFLATED) as archive:
            for source in sorted(PACK.rglob("*")):
                if not source.is_file() or source.is_symlink():
                    continue
                relative = source.relative_to(PACK)
                if any(p.startswith(".") for p in relative.parts) or relative.as_posix() == "config.json":
                    continue
                if relative.suffix.lower() in {".json",".tmx",".png"}:
                    archive.write(source,(Path(PACK.name)/relative).as_posix())
    except (ValueError,KeyError,OSError,zlib.error) as error:
        print(f"Falha ao empacotar: {error}",file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())

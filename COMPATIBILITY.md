# Compatibilidade

Os ensaios em Stardew Valley continuam pendentes. A base é SMAPI e `Pathoschild.ContentPatcher`. O pack declara SVE e LittleNPCs como dependências opcionais.

| Mod | Evidência e estado |
| --- | --- |
| Stardew Valley Expanded | Patch opcional para a Montanha, detectado pelo ID `FlashShifter.StardewValleyExpandedCP`. A análise anterior usou o manifesto 1.15.11, commit `7481ed586043802876d047d09aeaa3a6b7834858`. Confirmar tiles e rotas com os overlays carregados. [Repositório](https://github.com/FlashShifter/StardewValleyExpanded) |
| Ridgeside Village | Não testada. Conferir a Montanha e rotas SVE + RSV. [Descrição](https://www.nexusmods.com/stardewvalley/mods/7286) |
| East Scarp | Não testada. IDs históricos `LemurKat.EastScarpe.SMAPI` e `LemurKat.EastScarpe.CP`. Confirmar a versão escolhida e participação em festivais. [Repositório](https://github.com/lemurkat/East-Scarp) |
| Generic Mod Config Menu | Integração nativa documentada no CP, ID `spacechase0.GenericModConfigMenu`. [Configuração do CP](https://github.com/Pathoschild/StardewMods/blob/develop/ContentPatcher/docs/author-guide/config.md) |
| Fashion Sense | Compatibilidade provável. `PeacefulEnd.FashionSense`. Arthur usa o sistema de aparências nativo. [Manifesto](https://github.com/Floogen/FashionSense/blob/development/FashionSense/manifest.json) |
| Alternative Textures | Compatibilidade provável. `PeacefulEnd.AlternativeTextures`. O pack usa decoração em tiles. [Manifesto](https://github.com/Floogen/AlternativeTextures/blob/development/AlternativeTextures/manifest.json) |
| Seasonal Outfits | Compatibilidade provável com a variante consultada. Conferir alterações em mapas de festival. [Slightly Cuter Aesthetic](https://www.nexusmods.com/stardewvalley/mods/5450) |
| Date Night Redux | Compatibilidade provável. O autor documenta suporte a cônjuges customizados. Validar se o fluxo seleciona `ArthurANB`. [Descrição](https://www.nexusmods.com/stardewvalley/mods/22714) |
| Immersive Spouses | Não testada. O mod alerta sobre conflitos de horários conjugais. [Descrição](https://www.nexusmods.com/stardewvalley/mods/5117) |
| Immersive Characters — Shane | Pode exigir desativar `EnableShaneDialogue` se os dois packs ocuparem `Fri_2`. As menções de Arthur vêm desativadas por padrão. [Descrição](https://www.nexusmods.com/stardewvalley/mods/22955) |
| NPC Map Locations | Não testada. `Bouhm.NPCMapLocations`. Conferir registro dentro de casa e na trilha. [Manifesto](https://github.com/Bouhm/stardew-valley-mods/blob/main/NPCMapLocations/manifest.json) |
| Lookup Anything | Compatibilidade provável. `Pathoschild.LookupAnything`. Testar gostos e aniversário. [Manifesto](https://github.com/Pathoschild/StardewMods/blob/develop/LookupAnything/manifest.json) |
| UI Info Suite 2 | Compatibilidade provável. `Annosz.UiInfoSuite2`, manifesto analisado 2.3.7. Conferir o aniversário. [Manifesto](https://github.com/Annosz/UIInfoSuite2/blob/master/UIInfoSuite2/manifest.json) |
| Dynamic Reflections | Não testada. `PeacefulEnd.DynamicReflections`. A trilha não configura superfícies reflexivas. [Manifesto](https://github.com/Floogen/DynamicReflections/blob/development/DynamicReflections/manifest.json) |
| Weather Wonders | Não testada. Roupas e condições especiais usam climas nativos. [Descrição](https://www.nexusmods.com/stardewvalley/mods/23868) |
| Happy Home Designer | Não testada. Conferir o espaço do quarto e a circulação. [Descrição](https://www.nexusmods.com/stardewvalley/mods/19675) |
| Reformas da fazenda e do quarto conjugal | Podem exigir ajustes. Conferir o encaixe 6 × 9 do quarto, o pátio 4 × 4 e a posição do cônjuge. |
| Expansões de diálogo | Conferir as sete chaves opcionais de outros moradores. As opções individuais permitem desativar apenas a chave em conflito. |

## Filhos

| Mod | Evidência e estado |
| --- | --- |
| LittleNPCs | Ponte opcional implementada para duas falas conjugais, por tokens de `Candidus42.LittleNPCs` 2.2.1. Validação em jogo pendente. [Tokens e manifesto](https://github.com/mus-candidus/LittleNPCs) |
| The Farmer’s Children | Não testada. Conferir se a versão escolhida reconhece um cônjuge customizado. [Descrição](https://www.nexusmods.com/stardewvalley/mods/5436) |
| Immersive Family | Não testada. Conferir condições de eventos com crianças. [Descrição](https://www.nexusmods.com/stardewvalley/mods/18972) |
| Unique Children | Não testada. Arthur não inclui arte das crianças. [Descrição](https://www.nexusmods.com/stardewvalley/mods/6278) |
| Unique Children Talk | Não testada. Validar referências a cônjuge e combinação com crescimento. [Descrição](https://www.nexusmods.com/stardewvalley/mods/9540) |
| Growing Children | Não testada. Validar se a contagem nativa ainda inclui crianças crescidas. [Descrição](https://www.nexusmods.com/stardewvalley/mods/48458) |
| Growing Valley | Não testada com Arthur. O pack não acrescenta criança ligada ao personagem. [Descrição](https://www.nexusmods.com/stardewvalley/mods/23234) |

IDs e versões ausentes da tabela ainda dependem de verificação. Evite combinar dois mods que alterem o crescimento das mesmas crianças sem uma combinação documentada pelos autores.

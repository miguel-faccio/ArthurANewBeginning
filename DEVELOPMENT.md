# Desenvolvimento

O código-fonte editável está no pack `[CP] Arthur - A New Beginning`. O jogo usa JSON, i18n e TMX. Python 3.9 ou posterior é usado pelas ferramentas de desenvolvimento. O pack roda com SMAPI e Content Patcher.

| Área | Fonte |
| --- | --- |
| Identidade, aniversário, amizade, dados conjugais | `data/npc/core.json` |
| Gostos | `data/gifts/tastes.json` |
| Território e rotas | `data/locations/home.json`, `data/schedules/routes.json`, `assets/maps/` |
| Aparências | `data/appearances/wardrobe.json` e `asset-manifest.json` |
| Diálogo | `data/dialogue/everyday.json`, `data/marriage/dialogue.json`, `i18n/` |
| Ativação de eventos | `data/events/story.json`, `data/family/story.json` |
| Festivais e interações opcionais | `data/festivals/traditional.json`, `data/compatibility/` |

Preserve `ArthurANB`, `ArthurANB_House`, `ArthurANB_Lookout` e o prefixo de eventos `ArthurANewBeginning.Content_` entre versões. O warp da Montanha vanilla está em (48,30), com retorno em (47,30). A variante SVE usa (47,30) com retorno em (47,29). Ambas exigem teste de navegação real. A porta visitável abre das 8h às 22h. O NPC usa um warp próprio.

Use a amizade nativa para o arco de 2 a 8 corações. O evento de dez corações verifica namoro ou noivado e permite aceitar o beijo ou esperar. Os dois capítulos de quatorze corações dependem de casamento. O arco familiar acompanha conversa inicial, chegada e dois filhos conforme contagem nativa. O projeto usa as regras nativas de gravidez e adoção.

O recurso de compatibilidade LittleNPCs consulta os tokens de primeira e segunda criança para diálogos conjugais. Ele preserva o ciclo de vida das crianças. Os posicionamentos tradicionais são opt-in. O Content Patcher expõe o esquema de configuração no GMCM quando instalado.

“Jantar completo” continua sem ID confirmado. Os quatro itens amados registrados são pizza, bolo de chocolate, sorvete e expresso triplo.

[Guia do Content Patcher](https://github.com/Pathoschild/StardewMods/blob/develop/ContentPatcher/docs/author-guide.md) · [Dados de NPC](https://stardewvalleywiki.com/Modding:NPC_data) · [Horários](https://stardewvalleywiki.com/Modding:Schedule_data) · [Eventos](https://stardewvalleywiki.com/Modding:Event_data) · [Localizações](https://stardewvalleywiki.com/Modding:Location_data) · [Condições](https://stardewvalleywiki.com/Modding:Game_state_queries)

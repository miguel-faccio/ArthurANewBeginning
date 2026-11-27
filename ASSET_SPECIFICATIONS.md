# Especificações dos assets

Use PNG estático RGBA de 8 bits por canal, fundo transparente, sem entrelaçamento e sem antialiasing. Mantenha a escala e a ancoragem dos pés em todas as roupas. Arthur tem cabelo loiro claro, cacheado e volumoso, olhos azuis, rosto arredondado, ombros largos e postura relaxada. A roupa-base é cardigan azul acinzentado, camiseta branca, calça escura e tênis. A altura canônica é 1,89 m, com caixa de colisão padrão do jogo.

## Arquivos

Caminhos relativos a `[CP] Arthur - A New Beginning/`. Todas as folhas de retrato medem **128 × 384**, com 12 quadros de 64 × 64. Todas as folhas de personagem medem **64 × 416**, com 52 quadros de 16 × 32. Os primeiros 16 quadros da folha de personagem são os ciclos de caminhada. O restante acomoda as poses especiais, a dança e o casamento.

| Variação | Retrato | Personagem |
| --- | --- | --- |
| Base, obrigatória | `assets/portraits/ArthurANB.png` | `assets/characters/ArthurANB.png` |
| Primavera | `assets/portraits/ArthurANB_Spring.png` | `assets/characters/ArthurANB_Spring.png` |
| Verão | `assets/portraits/ArthurANB_Summer.png` | `assets/characters/ArthurANB_Summer.png` |
| Outono | `assets/portraits/ArthurANB_Fall.png` | `assets/characters/ArthurANB_Fall.png` |
| Inverno | `assets/portraits/ArthurANB_Winter.png` | `assets/characters/ArthurANB_Winter.png` |
| Chuva | `assets/portraits/ArthurANB_Rain.png` | `assets/characters/ArthurANB_Rain.png` |
| Resort | `assets/portraits/ArthurANB_Beach.png` | `assets/characters/ArthurANB_Beach.png` |
| Festival | `assets/portraits/ArthurANB_Festival.png` | `assets/characters/ArthurANB_Festival.png` |
| Pijama | `assets/portraits/ArthurANB_Pajamas.png` | `assets/characters/ArthurANB_Pajamas.png` |
| Trabalho | `assets/portraits/ArthurANB_Work.png` | `assets/characters/ArthurANB_Work.png` |
| Fazenda | `assets/portraits/ArthurANB_Spouse.png` | `assets/characters/ArthurANB_Spouse.png` |
| Aniversário | `assets/portraits/ArthurANB_Birthday.png` | `assets/characters/ArthurANB_Birthday.png` |

Forneça variações em pares. A precedência é resort, festival, aniversário, pijama, chuva, expediente, fazenda e estação. O traje de cerimônia fica nos quadros 48–50 de cada folha de personagem. A aparência muda quando o jogo recalcula as condições, por exemplo ao trocar de local. A troca na hora exata do fim do expediente não foi verificada no jogo.

## Retrato

| Índice | Expressão | X, Y |
| --- | --- | --- |
| 0 | Neutro | 0, 0 |
| 1 | Feliz | 64, 0 |
| 2 | Rindo | 0, 64 |
| 3 | Sério | 64, 64 |
| 4 | Surpreso | 0, 128 |
| 5 | Confuso | 64, 128 |
| 6 | Envergonhado | 0, 192 |
| 7 | Triste | 64, 192 |
| 8 | Preocupado | 0, 256 |
| 9 | Pensativo | 64, 256 |
| 10 | Animado | 0, 320 |
| 11 | Apaixonado | 64, 320 |

Os diálogos de Arthur usam marcadores numéricos. Textos genéricos do motor podem usar a associação de expressões nativa.

## Personagem

Na ordem das colunas, a origem X é **0, 16, 32, 48**.

| Y | Quadros | Uso |
| --- | --- | --- |
| 0 | 0, 1, 2, 3 | Caminhar para baixo |
| 32 | 4, 5, 6, 7 | Caminhar para a direita |
| 64 | 8, 9, 10, 11 | Caminhar para cima |
| 96 | 12, 13, 14, 15 | Caminhar para a esquerda |
| 128 | 16, 17, 18, 19 | Reservados |
| 160 | 20, 21, 22, 23 | Desenho, em dois quadros, e videogame, em dois quadros |
| 192 | 24, 25, 26, 27 | Desenho sentado, em dois quadros, dormir e reserva |
| 224 | 28, 29, 30, 31 | Beijo voltado para a direita e reservas |
| 256 | 32, 33, 34, 35 | Reservados |
| 288 | 36, 37, 38, 39 | Reservados |
| 320 | 40, 41, 42, 43 | Reservados |
| 352 | 44, 45, 46, 47 | Dança das Flores masculina |
| 384 | 48, 49, 50, 51 | Casamento masculino e reserva |

Deixe espaços reservados transparentes. Confira em jogo a ordem das poses de cerimônia, dança e beijo antes de considerar a folha final. O escritório usa `arthuranb_draw` (20–21), o descanso usa `arthuranb_game` (22–23), o sono usa `arthuranb_sleep` (26), e o pátio usa 24–25.

## Inclusão e mapas

Crie `assets/portraits` e `assets/characters` se estiver usando um checkout do Git. Adicione seus arquivos com os nomes exatos e rode `python tools/validate.py --release`. O validador confere dimensões, a estrutura PNG e a presença de pares. Associação visual de quadros e recorte dos pixels precisam de inspeção humana.

Os TMX referenciam `.townInterior.png`, `.spring_outdoorsTileSheet.png` e `.paths.png` da instalação do jogo. Preserve o prefixo ponto na referência do mapa. Para editar no Tiled, use uma cópia de trabalho com os tilesheets extraídos localmente da sua instalação.

[Dados de NPC](https://stardewvalleywiki.com/Modding:NPC_data) · [Mapas](https://stardewvalleywiki.com/Modding:Maps)

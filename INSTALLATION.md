# Instalação e saves

A 0.1.0 é uma versão de desenvolvimento. Faça a primeira instalação com um save descartável depois de fornecer a arte-base.

1. No Windows, prepare Stardew Valley 1.6.15, SMAPI compatível e Content Patcher 2.9.0 ou posterior. [SMAPI](https://smapi.io/) · [Content Patcher](https://www.nexusmods.com/stardewvalley/mods/1915)
2. Adicione os PNGs nos caminhos de [ASSET_SPECIFICATIONS.md](ASSET_SPECIFICATIONS.md) e rode `py -3 tools/validate.py --release`.
3. Copie a pasta `[CP] Arthur - A New Beginning` para `Mods`. Abra o jogo com SMAPI. Em um save existente, durma uma noite antes de avaliar a rotina.
4. Confira `config.json`, criado pelo Content Patcher. Reinicie após mudar opções de mapa.
5. Execute o roteiro de [TESTING.md](TESTING.md). Depois dos ensaios, `py -3 tools/package.py ArthurANewBeginning-0.1.0.zip` prepara o ZIP de instalação.

Feche o jogo e guarde uma cópia de `%AppData%\StardewValley\Saves` antes de instalar, atualizar ou remover. Preserve IDs, configuração e versão usada nesse save. Antes da remoção, retire objetos guardados nos mapas de Arthur e salve em outro local. Remover o pack após casamento, nascimento ou adoção pode deixar vínculos e dados do mapa inconsistentes. Guarde um backup anterior à instalação. Se Arthur desaparecer de um save existente, saia sem salvar e restaure o pack com os PNGs-base e a configuração anterior.

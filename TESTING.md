# Validação

A validação estática da reconstrução leu 18 JSON, quatro TMX, 22 eventos, 52 chaves de rotina e 258 entradas de texto correspondentes por idioma. Cinco testes automatizados passaram. O validador verifica pares de traduções e assets, referências, sintaxe básica, coordenadas e conectividade dos mapas próprios, rotinas e pré-requisitos de eventos. O empacotador da versão jogável encerra com código 2 enquanto faltarem os dois PNGs-base.

Este ambiente não executou Stardew Valley ou SMAPI. Os testes abaixo precisam ser feitos com a arte real e um save descartável.

| Área | Ensaio |
| --- | --- |
| Carregamento | Testar com zero, um e dois PNGs-base. Verificar calendário, amizade e spawn depois de dormir em fazenda existente. |
| Residência | Confirmar warps de ida e volta, bloqueios, porta e horários. Testar Montanha vanilla, SVE e SVE com o ajuste desligado. |
| Rotinas | Acompanhar Arthur andando todos os dias. Repetir em chuva, tempestade, neve, aniversário, casamento e depois de ter filhos. |
| Eventos | Ver as 22 cenas, testar pular e verificar os dois caminhos nas cenas de seis e dez corações. Conferir continuidade e se o beijo usa os quadros corretos. |
| Casamento e família | Testar pedido, cerimônia, quarto, pátio, mudança, divórcio, adoção e gravidez em saves separados. Conferir o texto com um e dois filhos. |
| Festivais | Ativar o posicionamento experimental. Conferir anos ímpares e pares, fase principal, dança, casamento e espectadores de outros mods. |
| Integrações | Instalar os mods opcionais em combinações controladas. Registrar versões, configuração, save, log e resultado. |
| Saves | Salvar e recarregar dentro e fora da casa. Testar host e farmhand e restauração de backup. |

Verifique os assets efetivos no console do Content Patcher, em especial `Data/Characters`, `Data/Locations`, `Characters/schedules/ArthurANB` e os dois arquivos de eventos. Confira colisões percorrendo a rota a pé.

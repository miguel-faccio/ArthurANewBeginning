# Estado da versão 0.1.0

Reconstruída a partir do histórico em 27 de novembro de 2026 após a perda de acesso ao workspace anterior. O projeto tem 33 arquivos. A comparação com o ZIP anterior não foi possível. Os IDs e o escopo conhecidos foram preservados. Trechos de diálogos, mapas, ferramentas e documentação foram reconstituídos ou reescritos.

| Fase | Implementação | Pendente |
| --- | --- | --- |
| Arquitetura e NPC | Manifesto, módulos CP, identificadores fixos, amizade, presentes, aniversário e configurações | Inserir duas folhas-base e confirmar o item “Jantar completo” |
| Casa e rotinas | Quatro mapas, duas localizações, 52 chaves, entrada vanilla e ajuste opcional SVE | Revisar visual dos mapas e percorrer as rotas no jogo |
| Diálogos | 258 entradas por idioma para contextos e cenas | Alcançar a meta de 1.000 originais e ampliar variações por hora, clima e situação |
| Narrativa | 2, 4, 6, 8 e 10 corações, dois capítulos de 14, três cenas familiares e 12 eventos secundários | Testar os 22 eventos e os dois caminhos das cenas ramificadas |
| Casamento e família | Noivado, quarto, pátio, falas conjugais e parentais, retorno antecipado em parte das rotas | Validar casamento, filhos, adoção, divórcio e multiplayer |
| Festivais | Oito posicionamentos experimentais, rotinas passivas de Mercado Noturno, Trout Derby e SquidFest | Validar colisões, fases principais, Dança das Flores e Festival do Deserto |
| Compatibilidade | Ajuste de rota SVE, ponte LittleNPCs e matriz documental | Rodar a matriz com as versões do modpack e confirmar IDs pendentes |
| Validação | Análise estática, cinco testes e bloqueio de empacotamento jogável | Validar os PNGs reais e executar testes dentro do jogo antes de distribuir |

Para retomar, rode `python tools/validate.py` e `python -m unittest discover -s tests -v`. Use [ASSET_SPECIFICATIONS.md](ASSET_SPECIFICATIONS.md) para preparar os PNGs. A primeira sessão no jogo deve provar o spawn, a entrada e saída da casa e a rota de segunda-feira.

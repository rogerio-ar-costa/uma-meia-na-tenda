# Workflow de Conteúdos

Este repositório deve passar a ser o sítio principal para guardar recursos úteis do projeto, em vez de haver cópias espalhadas pelo portátil.

## Regra simples

Se um recurso é útil mais do que uma vez, deve existir aqui em formato publicável:
- uma página em `content/games/` se for uma atividade;
- uma página em `content/library/` se for um livro, manual ou referência;
- uma página em `content/tools/` se for um site, app ou utilitário.

## Processo recomendado

1. Junta primeiro os ficheiros soltos numa pasta temporária fora do repositório.
2. Elimina duplicados óbvios e escolhe uma versão final por recurso.
3. Decide em que secção o recurso deve viver: jogos, biblioteca ou ferramentas.
4. Cria uma nova pasta dentro de `content/<secao>/<slug>/`.
5. Coloca aí o `index.md` e apenas os ficheiros que a página realmente usa, por exemplo `featured.svg`, `action.jpg` ou PDFs locais.
6. Dá contexto humano ao recurso: para que serve, quando usar, que secção beneficia mais, o que o torna útil.
7. Faz preview local antes de publicar.

## O que evitar

- PDFs repetidos com nomes diferentes.
- Links guardados sem descrição.
- Páginas que só fazem sentido para quem já sabe o histórico do ficheiro.
- Misturar notas privadas com conteúdo publicável.

## Critério de qualidade

Cada página deve responder rapidamente a estas perguntas:
- O que é isto?
- Quando é que eu usaria isto?
- Para quem é útil?
- O que preciso de saber antes de abrir, imprimir ou partilhar?

## Preview antes de merge

Trabalha sempre numa branch própria para cada melhoria ou conjunto coerente de conteúdos. Assim consegues abrir o site localmente, rever tudo com calma e só depois fazer merge.

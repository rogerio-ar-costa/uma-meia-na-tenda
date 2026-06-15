# Prompts para Imagens dos Jogos (`action.jpg`)

Os jogos abaixo têm, de momento, um **placeholder** em `action.jpg` (gerado por
`scripts/gen_placeholders.py`). Substitui cada um por uma imagem real gerada por AI.

## Estilo comum (acrescenta a todos os prompts)

> Cartoon style, colorful, friendly, flat illustration, scouts/cub-scouts activity,
> outdoors, dynamic and joyful, no text, no watermark, square 1:1, 1024x1024.

## Como aplicar

1. Gera a imagem (1024×1024, JPEG).
2. Guarda-a como `content/games/<slug>/action.jpg`, substituindo o placeholder.
3. Faz preview local e confirma que aparece logo a seguir ao `{{< lead >}}`.

## Prompts por jogo

| Slug | Prompt sugerido |
|------|-----------------|
| `caca-a-mola` | Children playing a tag game in an arena, stealing clothes-pegs from each other's backs, running and laughing. |
| `caca-o-rabo-do-macaco` | Kids with coloured ribbons tucked in their belts like tails, chasing and dodging to grab each other's ribbons, agility and balance. |
| `copos-e-molas` | A child stacking plastic cups into a pyramid using a single clothes-peg as a tool, focused and fun, table-top challenge. |
| `corda-de-fogo` | Children jumping over a rope that swings a water bottle in a circle near the ground, timing their jumps, outdoor game. |
| `corrida-de-cavaletes` | Scouts building a wooden trestle with ropes and poles (pioneering) and racing while carrying it, teamwork and speed. |
| `desenho-magico` | A relay drawing game: children running to a shared paper and adding one stroke each to a collective drawing, crayons and easel. |
| `engenhos-de-agua` | Kids building DIY water squirters from recycled bottles and tubes, crafting and testing them outdoors, splashes of water. |
| `guerra-de-catapultas` | Scouts building small wooden catapults with ropes (pioneering) and launching soft projectiles, friendly competition. |
| `o-tripe-escutista` | Scouts lashing three poles into a tripod with correct knots, focused teamwork, pioneering skills demonstration. |
| `pesca-de-escuteiros` | Children inside a hula-hoop being gently pulled toward a finish line by a teammate, "fishing" cooperative race. |
| `veste-o-balao` | A child putting on clothes while keeping a balloon in the air with the other hand, silly coordination challenge, laughter. |

> Nota: `jogo-do-kim` usa `items.jpg` (objetos para memorizar) — imagem já existente e
> intencionalmente descritiva; não precisa de `action.jpg`.

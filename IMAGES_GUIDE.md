# Guia para Adicionar Imagens de Destaque

Este guia explica como adicionar imagens de destaque (feature images) ao seu site, semelhante ao estilo do Blowfish.

## Estrutura de Pastas

Cada conteúdo deve estar numa pasta própria com um ficheiro `index.md` e as suas imagens:

```
content/
├── games/
│   ├── jogo-do-kim/
│   │   ├── index.md
│   │   └── featured.jpg  <- Imagem de destaque
│   └── jogo-da-bandeira/
│       ├── index.md
│       └── featured.png
```

## Como Adicionar uma Imagem de Destaque

### 1. Escolher a Imagem

- **Formato**: JPG, PNG ou WebP
- **Dimensões recomendadas**: 1200x630px (proporção 1.91:1)
- **Tamanho**: Até 500KB (otimize para web)
- **Nome do ficheiro**: `featured.jpg`, `featured.png` ou `feature.jpg`

### 2. Colocar a Imagem

Coloque a imagem na mesma pasta do `index.md` do conteúdo:

```bash
content/games/jogo-do-kim/featured.jpg
```

### 3. Referenciar no Front Matter

Adicione no front matter do `index.md`:

```yaml
---
title: "O Jogo do Kim"
description: "..."
# A imagem será automaticamente detetada se usar o nome 'featured'
# Ou pode especificar explicitamente:
images:
  - featured.jpg
---
```

## Tipos de Hero Styles

Pode personalizar como a imagem é exibida:

```yaml
---
showHero: true
heroStyle: "background"  # Opções: basic, big, background, thumbAndBackground
---
```

### Estilos Disponíveis:

- **basic**: Imagem simples no topo
- **big**: Imagem grande em destaque
- **background**: Imagem como fundo com overlay (recomendado)
- **thumbAndBackground**: Miniatura + fundo

## Fontes de Imagens Gratuitas

### Recomendadas para Escutismo:

1. **Unsplash** (https://unsplash.com)
   - Pesquise: "camping", "hiking", "nature", "teamwork", "outdoor games"

2. **Pexels** (https://pexels.com)
   - Pesquise: "scouts", "youth activities", "outdoor adventure"

3. **Pixabay** (https://pixabay.com)
   - Pesquise: "children playing", "camping", "nature"

### Dicas de Pesquisa:

- "campfire", "tent camping", "rope knots"
- "team building", "outdoor education"
- "forest adventure", "hiking trail"
- "children outdoor games"

## Exemplo Completo

### Estrutura:
```
content/games/orientacao/
├── index.md
├── featured.jpg
└── diagrama-bussola.png
```

### Front Matter:
```yaml
---
title: "Jogo de Orientação"
description: "Aprende a usar bússola e mapa"
date: 2026-01-08
tags: ["Exploradores", "Exterior", "Orientação"]
categories: ["Jogos"]
showHero: true
heroStyle: "background"
images:
  - featured.jpg
showTableOfContents: true
showReadingTime: true
showWordCount: true
---
```

## Otimização de Imagens

Antes de adicionar, otimize suas imagens:

### Online:
- TinyPNG (https://tinypng.com)
- Squoosh (https://squoosh.app)

### Linha de Comando:
```bash
# Redimensionar para 1200px de largura
magick input.jpg -resize 1200x output.jpg

# Comprimir com qualidade 85%
magick input.jpg -quality 85 output.jpg
```

## Ícones para Secções

Para ícones nas páginas de índice, considere:

- **Font Awesome** (já incluído no Blowfish)
- **Emojis** (funciona em todos os browsers modernos)
- **SVGs personalizados** (para identidade visual própria)

### Exemplo com Emoji no Título:
```yaml
---
title: "🎮 Jogos Escutistas"
---
```

### Exemplo com Font Awesome:
```markdown
## {{< icon "campground" >}} Jogos ao Ar Livre
```

## Checklist Final

Ao adicionar conteúdo novo com imagem:

- [ ] Imagem otimizada (< 500KB)
- [ ] Dimensões corretas (1200x630px ou similar)
- [ ] Nome do ficheiro: `featured.jpg` ou `featured.png`
- [ ] Colocada na pasta correta
- [ ] Front matter configurado corretamente
- [ ] `showHero: true` e `heroStyle` definidos
- [ ] Testado localmente antes de commitar

## Recursos Adicionais

- [Documentação Blowfish - Thumbnails](https://blowfish.page/docs/thumbnails/)
- [Documentação Blowfish - Front Matter](https://blowfish.page/docs/front-matter/)

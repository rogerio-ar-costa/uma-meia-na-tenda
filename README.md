# Uma Meia na Tenda 🧦⛺

Repositório de jogos, livros e ferramentas para escuteiros do Corpo Nacional de Escutas.

## Como Usar Este Projeto

### Pré-requisitos

Este projeto usa Hugo como gerador de site estático. O executável do Hugo já está incluído na pasta `.bin/`.

### Executar o Site Localmente

Para ver o site no teu browser:

```bash
./.bin/hugo.exe server -D
```

Depois abre o browser em: `http://localhost:1313/uma-meia-na-tenda/`

### Construir o Site para Produção

```bash
./.bin/hugo.exe --cleanDestinationDir
```

Os ficheiros gerados estarão na pasta `public/`.

## Estrutura do Projeto

```
.
├── content/
│   ├── games/          # Jogos e atividades
│   ├── library/        # Livros e recursos
│   └── tools/          # Ferramentas digitais
├── config/
│   └── _default/       # Configurações do site
├── static/             # Ficheiros estáticos (imagens, etc)
└── themes/blowfish/    # Tema Hugo
```

## Adicionar Novo Conteúdo

### Adicionar um Jogo

1. Cria uma nova pasta em `content/games/nome-do-jogo/`
2. Cria um ficheiro `index.md` com o seguinte formato:

```markdown
---
title: "Nome do Jogo"
description: "Breve descrição do jogo"
date: 2026-01-07
tags: ["Lobitos", "Exploradores", "Interior"]
categories: ["Jogos"]
---

Conteúdo do jogo aqui...

## Material Necessário
- Item 1
- Item 2

## Como Jogar
1. Passo 1
2. Passo 2

## Vídeo (opcional)
{{< youtube "VIDEO_ID" >}}
```

### Adicionar um Livro

Similar aos jogos, mas na pasta `content/library/`.

### Adicionar uma Ferramenta

Similar aos jogos, mas na pasta `content/tools/`.

## Funcionalidades

### Tags e Categorias

Usa tags para facilitar a pesquisa:
- **Secções**: Lobitos, Exploradores, Pioneiros, Caminheiros
- **Tipo**: Interior, Exterior, Memória, Técnicas, Equipa
- **Outros**: Digital, Planeamento, Dirigentes

### Imagens

Para adicionar uma imagem a um item:

1. Coloca a imagem na mesma pasta que o `index.md` (ex: `featured.jpg`)
2. O Hugo usa automaticamente essa imagem como destaque

### Vídeos do YouTube

Usa o shortcode:
```markdown
{{< youtube "ID_DO_VIDEO" >}}
```

### Links Externos

Para criar um card que linka diretamente para um site externo, adiciona no frontmatter:
```yaml
externalUrl: "https://exemplo.com"
```

## Pesquisa

A pesquisa está ativada por defeito. Funciona por:
- Título
- Descrição
- Tags
- Conteúdo

## Tema

Este projeto usa o tema [Blowfish](https://blowfish.page/) com esquema de cores "emerald" (verde escutista).

## Deploy

O site está configurado para deploy automático via GitHub Actions. Cada push para a branch principal atualiza automaticamente o site.

## Suporte

Para questões ou sugestões, abre uma issue no repositório.

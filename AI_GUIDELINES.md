# 🤖 AI Guidelines - Uma Meia na Tenda

Este documento contém as regras e padrões para agentes AI criarem ou modificarem conteúdo neste repositório.

---

## 🏗️ Arquitetura do Projeto

### Stack Tecnológico
- **Gerador**: Hugo (v0.141.0+)
- **Tema**: Blowfish
- **Linguagem**: Português de Portugal (pt)
- **Servidor Local**: `./.bin/hugo.exe server -D`
- **URL Base**: `http://localhost:1313/uma-meia-na-tenda/`

### Estrutura de Diretórios

```
uma-meia-na-tenda/
├── content/
│   ├── _index.pt.md           # Página inicial (português)
│   ├── games/                 # 🎯 Jogos e Atividades
│   │   ├── _index.md         
│   │   └── [jogo]/
│   │       ├── index.md
│   │       └── featured.svg
│   ├── library/              # 📖 Recursos Pedagógicos
│   │   ├── _index.md
│   │   └── [recurso]/
│   │       ├── index.md
│   │       └── featured.svg
│   └── tools/                # 🛠️ Ferramentas
│       ├── _index.md
│       └── [ferramenta]/
│           ├── index.md
│           └── featured.svg
├── config/
│   └── _default/
│       └── config.toml       # Configuração principal
├── static/                   # Ficheiros estáticos (imagens, etc)
└── themes/blowfish/          # Tema Hugo
```

---

## 📝 Frontmatter Obrigatório

### Template Padrão

```yaml
---
title: "Título do Item"
summary: "Resumo curto para listagens (máx. 100 caracteres)"
description: "Descrição mais detalhada para SEO e metadados"
date: 2026-01-18
tags: ["tag1", "tag2", "tag3"]
categories: ["Jogos"]  # ou ["Livros"] ou ["Ferramentas"]
---
```

### Campos Opcionais

```yaml
# Para links externos diretos (abre em nova aba)
externalUrl: "https://exemplo.com"

# Para configuração específica de exibição
showReadingTime: true
showWordCount: true
showTableOfContents: false
```

### Categorias Válidas
- `["Jogos"]` → para items em `content/games/`
- `["Livros"]` → para items em `content/library/`
- `["Ferramentas"]` → para items em `content/tools/`

### Tags Recomendadas

**Secções Escutistas:**
- Lobitos, Exploradores, Pioneiros, Caminheiros, Dirigentes

**Tipo de Atividade:**
- Interior, Exterior, Memória, Observação, Técnicas, Equipa

**Temas Específicos:**
- GPS, Navegação, Orientação, Códigos, Cifras, Morse, Digital, Formação

**Exemplo completo:**
```yaml
tags: ["Lobitos", "Exploradores", "Interior", "Memória", "Observação"]
```

---

## 📄 Estrutura de Conteúdo

### Para Ferramentas e Recursos (Listas de Links)

Use este formato para páginas que agregam múltiplos recursos externos:

```markdown
---
title: "Nome da Ferramenta"
summary: "Resumo conciso"
description: "Descrição completa"
tags: ["tag1", "tag2"]
categories: ["Ferramentas"]
---

Parágrafo introdutório explicando o tipo de recursos disponíveis (1-2 linhas).

### [Nome do Recurso 1](https://url1.com/)
Descrição breve e objetiva do que este recurso oferece.

### [Nome do Recurso 2](https://url2.com/)
Outra descrição concisa e informativa.

### [Nome do Recurso 3](https://url3.com/)
Mais uma descrição clara do recurso.
```

**Regras:**
- Headers H3 (`###`) para cada recurso
- Título do link em formato `[Texto](URL)`
- Uma linha de descrição por recurso
- Sem parágrafos longos entre recursos
- Links verificados e funcionais

#### Emojis para Links
Use os seguintes emojis prefixados nos links para identificar o tipo de conteúdo:
- 📄 **Documentos/Páginas**: Para links gerais, PDFs ou artigos.
- 🎵 **Áudio/Música**: Para cancioneiros ou ficheiros de som.
- 🔗 **Ferramentas/Externo**: Para plataformas interativas ou visualizadores externos.

Exemplo: `📄 [Manual do Dirigente](https://...)`

### Para Jogos e Atividades

Todos os jogos e atividades devem seguir rigorosamente esta estrutura altamente visual, engajadora e completa:

```markdown
---
title: "Nome do Jogo"
summary: "Objetivo do jogo em poucas palavras"
description: "Descrição completa"
tags: ["Lobitos", "Interior", "Memória"]
categories: ["Jogos"]
---

{{\u003c lead \u003e}}
Introdução super apelativa ao jogo com 1-2 frases dinâmicas que destaquem o quão divertido e inovador é.
{{\u003c /lead \u003e}}

![Nome do Jogo](action.jpg)

## 🎯 Objetivo
1-2 frases explicando claramente a finalidade principal do jogo.

## ⏱️ Duração e Participantes
- **Duração:** X minutos
- **Participantes:** Tamanho da equipa recomendado.

## 🛠️ Material Necessário
- Item 1
- Item 2
- Item 3

## Imagem do Jogo (Nota AI)
<!-- Lembra-te: Deves incluir uma imagem gerada por AI (cartoon style e colorful) e salva como `action.jpg`. Usa `![Descrição da imagem](action.jpg)` imediatamente após o lead, como no exemplo acima. -->

## 📜 Como Jogar
1. **Passo 1:** Descrição do passo.
2. **Passo 2:** Descrição do passo.
3. **Passo 3:** Descrição do passo.

## 🌟 Dicas de Animação

> [!TIP]
> Ideias para o imaginário do jogo, truques para o dirigente envolver mais as crianças, ou métodos para aumentar o espírito de equipa. Use Markdown blockquotes (GitHub alerts) `> [!TIP]` para destaque.

## 🛡️ Segurança

> [!WARNING]
> Alertas cruciais sobre terreno, possíveis perigos, ou regras essenciais para evitar lesões. Use `> [!WARNING]` ou `> [!CAUTION]`.

## 🔄 Variantes

### Nome da Variante
Como adaptar o jogo a espaços mais pequenos, menos material, idades diferentes, ou como complicar as regras para os mais velhos.

## Vídeo (opcional)
{{\u003c youtube "VIDEO_ID" \u003e}}
```

---

## 🎨 SVG - Imagem de Destaque

### Especificações Obrigatórias

- **Nome**: `featured.svg`
- **Dimensões**: `1200x400` (NÃO 630!)
- **Conteúdo**: Emoji + Título (SEM descrição/subtítulo)
- **Posicionamento**:
  - Emoji: `y="140"`
  - Título: `y="280"`
  - Espaçamento: 140px entre elementos

### Template Completo

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400">
  <defs>
    <linearGradient id="grad-NOME-UNICO" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#COR1;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#COR2;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="1200" height="400" fill="url(#grad-NOME-UNICO)"/>
  <text x="600" y="140" font-family="Arial, sans-serif" font-size="120" fill="white" text-anchor="middle" font-weight="bold">🎯</text>
  <text x="600" y="280" font-family="Arial, sans-serif" font-size="60" fill="white" text-anchor="middle" font-weight="bold">Título</text>
</svg>
```

### Paletas de Cores

| Categoria | Tema | Gradiente | Cor Início | Cor Fim |
|-----------|------|-----------|-----------|---------|
| **Tools** | Navegação/GPS | Verde | `#10b981` | `#059669` |
| **Tools** | Cifras/Códigos | Roxo/Índigo | `#8b5cf6` | `#6366f1` |
| **Library** | Livros | Laranja | `#f59e0b` | `#d97706` |
| **Games** | Jogos | Verde | `#10b981` | `#059669` |

### Emojis Sugeridos

- 🗺️ Trilhos, Mapas, Rotas
- 🧭 Orientação, Navegação, Coordenadas
- 🔐 Cifras, Códigos Secretos, Criptografia
- 📚 Livros, Biblioteca, Literatura
- 🧠 Memória, Inteligência, Raciocínio
- 🎯 Atividades, Objetivos, Metas
- ⚡ Técnicas, Ação, Dinâmica
- 🏕️ Campismo, Acampamento

### ⚠️ ID do Gradiente - CRÍTICO

**NUNCA** duplicar IDs de gradiente! Use nomes únicos:

```xml
<!-- ✅ CORRETO -->
<linearGradient id="grad-cifras" ...>
<linearGradient id="grad-trilhos" ...>
<linearGradient id="grad-livros" ...>

<!-- ❌ ERRADO -->
<linearGradient id="grad1" ...>  <!-- Genérico -->
<linearGradient id="gradient" ...>  <!-- Pode duplicar -->
```

---

## 🚫 Regras CRÍTICAS

### ❌ NUNCA FAZER

1. **SVG com altura 630px** → Formato ANTIGO descontinuado
2. **Adicionar subtítulos nos SVGs** → Apenas emoji + título
3. **Usar cores genéricas** → Sem vermelho/azul/verde puros
4. **IDs de gradiente duplicados** → Usar `grad-[nome-unico]`
5. **Criar páginas sem frontmatter** → Sempre obrigatório
6. **Links não verificados** → Testar todos os URLs
7. **Parágrafos longos entre links** → Manter conciso
8. **Esquecer o featured.svg** → Obrigatório para todas as páginas

### ✅ SEMPRE FAZER

1. **SVG 1200x400** → Formato padrão atual
2. **Emoji apropriado** → Representativo do conteúdo
3. **Gradientes profissionais** → Usar paleta de cores definida
4. **Tags relevantes** → Facilitar busca e filtros
5. **Descrições concisas** → Máximo 1-2 linhas
6. **Português de Portugal** → Linguagem consistente
7. **Links funcionais** → Verificar antes de adicionar
8. **Testar localmente** → `hugo server -D` antes de commit

---

## 🛠️ Shortcodes Hugo Disponíveis

### Vídeo YouTube
```markdown
{{\u003c youtube "VIDEO_ID" \u003e}}
```

### Lead (texto introdutório destacado)
```markdown
{{\u003c lead \u003e}}
Texto de introdução em destaque.
{{\u003c /lead \u003e}}
```

### Comentários HTML
```html
\u003c!--
Conteúdo comentado que não aparece no site
--\u003e
```

---

## 📂 Nomes de Ficheiros e Pastas

### Convenção de Nomenclatura

**Pastas**: Usar kebab-case (minúsculas com hífenes)
```
✅ jogo-do-kim
✅ cifras-escutistas
✅ livros

❌ Jogo do Kim
❌ cifras_escutistas
❌ LIVROS
```

**Ficheiros**:
- `index.md` → Conteúdo principal (obrigatório)
- `featured.svg` → Imagem destaque (obrigatório)
- `_index.md` → Página de secção/categoria

---

## 🔄 Fluxo de Criação de Conteúdo

1. **Escolher categoria**: games, library ou tools
2. **Criar diretório**: `content/[categoria]/[nome-slug]/`
3. **Criar index.md** com frontmatter completo
4. **Escrever conteúdo** seguindo estrutura apropriada
5. **Criar featured.svg** com especificações corretas
6. **Verificar links** e formatação
7. **Testar localmente**: `./.bin/hugo.exe server -D`
8. **Validar**: Abrir `http://localhost:1313/uma-meia-na-tenda/`

---

## 🎯 Princípios de Design

1. **Minimalismo** → Evitar poluição visual
2. **Clareza** → Linguagem direta e acessível
3. **Consistência** → Seguir padrões estabelecidos
4. **Praticidade** → Foco em recursos úteis
5. **Profissionalismo** → Design moderno e curado

---

## 📚 Exemplos de Referência no Repositório

### Estrutura Perfeita
- `content/tools/cifras/` → Lista de links bem organizada
- `content/tools/trilhos/` → Múltiplos recursos categorizados
- `content/library/livros/` → Referências bibliográficas
- `content/games/jogo-do-kim/` → Jogo documentado

### SVGs Exemplares
- `content/tools/cifras/featured.svg` → Roxo/índigo com 🔐
- `content/library/livros/featured.svg` → Laranja com 📚
- `content/tools/trilhos/featured.svg` → Verde com 🗺️

---

## 🧪 Testar Alterações

### Comandos Úteis

```bash
# Iniciar servidor de desenvolvimento
./.bin/hugo.exe server -D

# Build de produção
./.bin/hugo.exe --cleanDestinationDir

# Ver versão do Hugo
./.bin/hugo.exe version
```

### Checklist de Validação

- [ ] Frontmatter completo e válido
- [ ] Tags relevantes adicionadas
- [ ] SVG no formato 1200x400
- [ ] ID de gradiente único
- [ ] Links testados e funcionais
- [ ] Descrições concisas
- [ ] Português (pt-pt) correto
- [ ] Página visível localmente

---

## 📞 Recursos Adicionais

- **README.md**: Informação geral do projeto
- **Documentação Hugo**: https://gohugo.io/
- **Tema Blowfish**: https://blowfish.page/
- **Repositório**: https://github.com/rogerio-ar-costa/uma-meia-na-tenda

---

**Versão**: 2.0  
**Última atualização**: 2026-01-18

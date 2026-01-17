# Resumo do Projeto - Uma Meia na Tenda

## O Que Foi Feito

Limpeza e reestruturação completa do projeto Hugo para criar um repositório simples e funcional de recursos escutistas.

## Estrutura Criada

### 3 Secções Principais

1. **Jogos** (`/games`)
   - Jogo do Kim
   - Jogo da Bandeira
   - Nós e Amarras

2. **Biblioteca** (`/library`)
   - Manual do Escuteiro
   - O Livro da Selva

3. **Ferramentas** (`/tools`)
   - Gerador de Programas

### Funcionalidades Implementadas

#### Grid System
- Layout em grelha (cards) para todos os recursos
- Visualização responsiva e moderna
- Cards com imagem, título, descrição e tags

#### Sistema de Pesquisa
- Pesquisa ativada por defeito
- Funciona por:
  - Nome do recurso
  - Descrição
  - Tags
  - Conteúdo completo
- Interface overlay (abre por cima do site)

#### Sistema de Tags
Tags implementadas para filtrar recursos:
- **Secções**: Lobitos, Exploradores, Pioneiros, Caminheiros, Todos
- **Tipos**: Interior, Exterior, Memória, Técnicas, Equipa, Digital
- **Categorias**: Jogos, Livros, Ferramentas

#### Suporte para Múltiplos Tipos de Conteúdo

**Imagens:**
- Suporte para imagens de destaque (featured image)
- Basta colocar uma imagem na pasta do conteúdo
- Imagens inline no texto markdown

**Vídeos YouTube:**
- Shortcode simples: `{{< youtube "VIDEO_ID" >}}`
- Integração nativa com player embutido

**Links Externos:**
- Suporte para links no conteúdo
- Opção `externalUrl` para criar cards que linkam diretamente

**Texto Rico:**
- Markdown completo
- Formatação, listas, citações
- Títulos e subtítulos

## Configuração

### Tema
- **Blowfish** - Tema Hugo moderno e funcional
- **Esquema de cores**: Emerald (verde escutista)
- **Modo**: Light por defeito, com switcher para dark mode

### Idioma
- Português (pt)
- Configurações localizadas

### Menu de Navegação
- Jogos
- Biblioteca
- Ferramentas
- Pesquisa (ícone)

## Arquivos de Template (Archetypes)

Criados templates para facilitar a adição de conteúdo:

- `archetypes/games.md` - Template para jogos
- `archetypes/library.md` - Template para livros
- `archetypes/tools.md` - Template para ferramentas

## Como Usar

### Executar Localmente
```bash
./.bin/hugo.exe server -D
```
Aceder: http://localhost:1313/uma-meia-na-tenda/

### Criar Novo Conteúdo
```bash
# Novo jogo
./.bin/hugo.exe new content/games/nome-do-jogo/index.md

# Novo livro
./.bin/hugo.exe new content/library/nome-do-livro/index.md --kind library

# Nova ferramenta
./.bin/hugo.exe new content/tools/nome-ferramenta/index.md --kind tools
```

### Build para Produção
```bash
./.bin/hugo.exe --cleanDestinationDir
```

## Próximos Passos Sugeridos

1. **Adicionar mais conteúdo**: Jogos, livros e ferramentas
2. **Adicionar imagens**: Colocar imagens nos recursos existentes
3. **Personalizar cores**: Ajustar o esquema de cores se necessário
4. **Adicionar logo**: Logo do agrupamento ou projeto
5. **Deploy**: Configurar GitHub Pages ou Netlify

## Ficheiros de Configuração Principais

- `config/_default/config.toml` - Configuração geral
- `config/_default/params.toml` - Parâmetros do tema
- `config/_default/languages.pt.toml` - Idioma português

## Estrutura de Pastas

```
uma-meia-na-tenda/
├── content/
│   ├── _index.md                    # Homepage
│   ├── games/
│   │   ├── _index.md               # Página da secção Jogos
│   │   ├── jogo-do-kim/
│   │   ├── jogo-da-bandeira/
│   │   └── nos-e-amarras/
│   ├── library/
│   │   ├── _index.md               # Página da secção Biblioteca
│   │   ├── manual-escuteiros/
│   │   └── livro-da-selva/
│   └── tools/
│       ├── _index.md               # Página da secção Ferramentas
│       └── gerador-programa/
├── config/
│   └── _default/
│       ├── config.toml
│       ├── params.toml
│       ├── languages.pt.toml
│       ├── module.toml
│       └── outputs.toml
├── archetypes/
│   ├── games.md
│   ├── library.md
│   └── tools.md
├── static/                          # Para ficheiros estáticos
├── themes/blowfish/                 # Tema Hugo
├── README.md                        # Documentação completa
├── QUICK_START.md                   # Guia rápido
└── PROJECT_SUMMARY.md              # Este ficheiro
```

## Exemplos de Conteúdo

Cada exemplo demonstra diferentes funcionalidades:

- **Jogo do Kim**: Exemplo básico com texto e links externos
- **Jogo da Bandeira**: Exemplo com YouTube embed
- **Nós e Amarras**: Exemplo com múltiplos recursos
- **Manual do Escuteiro**: Exemplo de livro com citações
- **Livro da Selva**: Exemplo rico com múltiplas secções
- **Gerador de Programas**: Exemplo de ferramenta com link externo

## Tecnologias Utilizadas

- **Hugo** v0.141.0 (incluído em `.bin/hugo.exe`)
- **Tema Blowfish** (via git submodule)
- **Markdown** para conteúdo
- **TOML** para configuração
- **GitHub Actions** para deploy (já configurado)

## Estado do Projeto

- ✅ Estrutura base criada
- ✅ Sistema de pesquisa funcional
- ✅ Grid layout implementado
- ✅ Tags e categorias configuradas
- ✅ Exemplos de conteúdo criados
- ✅ Templates (archetypes) prontos
- ✅ Documentação completa
- ✅ Site a compilar sem erros

**Build Status**: 57 páginas geradas com sucesso em ~1 segundo

## Notas

- O warning sobre "json layout" é normal e não afeta a funcionalidade
- A pesquisa funciona automaticamente através dos outputs JSON configurados
- O tema Blowfish é muito bem documentado em https://blowfish.page/

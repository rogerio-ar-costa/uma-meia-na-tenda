# Uma Meia na Tenda 🧦⛺

> Baú de recursos digitais para escuteiros do **Corpo Nacional de Escutas**:
> jogos, recursos pedagógicos e ferramentas, num só sítio, prontos a usar.

🌐 **Site publicado:** <https://rogerio-ar-costa.github.io/uma-meia-na-tenda/>

---

## O que vais encontrar

| Secção | O que é | Exemplos |
|--------|---------|----------|
| 🎯 **Jogos e Atividades** | Jogos prontos para qualquer secção, com objetivo, material, passos, dicas e segurança | Caça à Mola, Corrida de Cavaletes, Engenhos de Água |
| 📖 **Recursos Pedagógicos** | Livros, manuais e cancioneiros | Materiais de Lobitos, Manuais |
| 🛠️ **Ferramentas** | Apps e sites úteis no terreno | Cifras, Orientação, Trilhos |

Cada página foi escrita para ser lida por **pessoas**: explica o que é, quando usar,
para quem é útil e o que precisas de saber antes de imprimir ou partilhar.

---

## Ver o site no teu computador

O site é feito com [Hugo](https://gohugo.io/) (versão `0.141.0`, edição *extended*).

```bash
# Linux / macOS (Hugo instalado no sistema)
hugo server -D

# Windows (binário incluído no repositório)
.\.bin\hugo.exe server -D
```

Depois abre <http://localhost:1313/> no browser. O `-D` mostra também rascunhos.

### Construir para produção

```bash
hugo --cleanDestinationDir             # Linux / macOS
.\.bin\hugo.exe --cleanDestinationDir  # Windows
```

A build deve terminar **sem `WARN` nem `ERROR`**. Se aparecerem, há algo a corrigir.

---

## Estrutura do repositório

```
content/            ← todo o conteúdo do site (Markdown)
  games/<slug>/     ← um jogo = uma pasta com index.md + action.jpg
  library/<slug>/   ← recursos pedagógicos
  tools/<slug>/     ← ferramentas
config/_default/    ← configuração do Hugo
layouts/ assets/    ← personalizações por cima do tema Blowfish
scripts/            ← utilitários (ex: geração de imagens placeholder)
```

---

## Contribuir 🙌

**Todos são bem-vindos!** Para acrescentar um jogo, recurso ou ferramenta:

1. Lê o **[AI_GUIDELINES.md](./AI_GUIDELINES.md)** — os padrões de cada tipo de página.
2. Lê o **[CONTENT_WORKFLOW.md](./CONTENT_WORKFLOW.md)** — como trazer recursos soltos
   para o repositório sem criar duplicação.
3. Cria uma **branch própria** para a tua melhoria.
4. Cria a pasta em `content/<secção>/<slug>/` com o `index.md` e as imagens que a página usa.
5. Faz **preview local** e confirma a homepage, a página de detalhe e os botões de
   partilha/impressão.
6. Abre um **Pull Request**.

> 💡 As imagens dos jogos chamam-se `action.jpg` (1024×1024). Algumas ainda têm um
> *placeholder* à espera de uma imagem real — consulta
> [`scripts/image-prompts.md`](./scripts/image-prompts.md) para os prompts sugeridos.

Dúvidas ou sugestões? [Abre uma issue](https://github.com/rogerio-ar-costa/uma-meia-na-tenda/issues/new).

**Bom Escutismo!** 🏕️

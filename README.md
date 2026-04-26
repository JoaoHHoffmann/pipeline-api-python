# 🔍 Pipeline API Python

Pipeline de dados que consome a **API do GitHub** para coletar, analisar e armazenar as linguagens de programação mais utilizadas nos repositórios públicos de grandes empresas de tecnologia.

---

## 📋 Sobre o Projeto

Este projeto implementa um pipeline completo de dados usando Python e a API REST do GitHub. A partir do username de uma organização, o pipeline busca todos os repositórios públicos, extrai as linguagens de programação utilizadas, e salva os dados em arquivos `.csv` — prontos para análise.

As empresas analisadas neste projeto são:
- **Amazon** (`amzn`)
- **Netflix** (`netflix`)
- **Spotify** (`spotify`)

---

## 🗂️ Estrutura do Projeto

```
pipeline-api-python/
│
├── dados_repos.py          # Classe principal: consome a API do GitHub
├── extraindo_arquivos.py   # Script que executa o pipeline e salva os CSVs
├── manipula_repos.py       # Classe para criar repositórios e fazer upload de arquivos
├── linguagens_repos.ipynb  # Notebook com análise exploratória dos dados
│
├── data/                   # CSVs gerados pelo pipeline
│   ├── linguagens_amzn.csv
│   ├── linguagens_netflix.csv
│   └── linguagens_spotify.csv
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Como Funciona

O pipeline é dividido em três etapas:

**1. Coleta de dados (`dados_repos.py`)**  
A classe `DadosRepositorios` recebe o username de uma organização do GitHub e percorre até 20 páginas de repositórios via API, extraindo nome e linguagem principal de cada repositório.

**2. Extração e salvamento (`extraindo_arquivos.py`)**  
Instancia a classe para cada empresa, gera um DataFrame com os dados e salva um arquivo `.csv` na pasta `data/`.

**3. Manipulação de repositórios (`manipula_repos.py`)**  
A classe `ManipulaRepositorios` permite criar repositórios no GitHub e fazer upload dos arquivos `.csv` gerados, tudo via API.

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/JoaoHHoffmann/pipeline-api-python.git
cd pipeline-api-python
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
GITHUB_TOKEN=seu_token_aqui
GITHUB_USERNAME=seu_username_aqui
```

> 💡 Para gerar um token de acesso pessoal, acesse: [GitHub → Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)

### 4. Execute o pipeline

```bash
python extraindo_arquivos.py
```

Os arquivos `.csv` serão gerados na pasta `data/`.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| Python | Linguagem principal |
| Requests | Consumo da API do GitHub |
| Pandas | Manipulação e exportação dos dados |
| python-dotenv | Gerenciamento de variáveis de ambiente |
| Jupyter Notebook | Análise exploratória dos dados |

---

## 📦 Dependências

```
requests
pandas
python-dotenv
jupyter
```

> Instale tudo com: `pip install -r requirements.txt`

---

## 📊 Exemplo de Saída

Após rodar o pipeline, os CSVs gerados terão o seguinte formato:

| repository_name | language |
|---|---|
| aws-sdk-java | Java |
| amazon-kinesis | Python |
| alexa-skills-kit | JavaScript |

---

## 🔐 Segurança

- Nunca commite seu `.env` no repositório (já está no `.gitignore`)
- O token do GitHub deve ter permissão de leitura de repositórios públicos (`public_repo`)
- Para fazer upload de arquivos via `manipula_repos.py`, o token precisa de permissão de escrita (`repo`)
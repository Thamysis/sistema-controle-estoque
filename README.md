# Sistema de Controle de Estoque

## Descricao

Aplicacao web simples para controle de estoque, desenvolvida com Flask no backend e HTML/CSS com Bootstrap no frontend. O sistema possui autenticacao de usuarios e CRUD de produtos, incluindo cadastro, listagem, edicao e exclusao.

## Requisitos

- Python 3.11 ou superior
- MySQL
- pip

## Como executar o projeto

### 1. Criar e ativar um ambiente virtual

No Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar as dependencias

```bash
pip install -r requirements.txt
```

### 3. Criar o arquivo .env

Use o arquivo `.env.example` como base e crie um arquivo `.env` na raiz do projeto.

Exemplo:

```env
SECRET_KEY=troque_esta_chave
DB_USERNAME=root
DB_PASSWORD=
DB_SERVER=localhost
DB_NAME=sistemacontroleestoque
```

### 4. Configurar o banco MySQL

Crie um banco de dados MySQL com o nome configurado em `DB_NAME`.

Exemplo:

```sql
CREATE DATABASE sistemacontroleestoque;
```

Depois disso, ajuste no arquivo `.env` os valores de acesso ao banco:

- `DB_USERNAME`
- `DB_PASSWORD`
- `DB_SERVER`
- `DB_NAME`

O projeto usa essas variaveis para montar a conexao com o MySQL em tempo de execucao.

### 5. Executar a aplicacao

```bash
python app.py
```

Por padrao, a aplicacao sera iniciada localmente pelo servidor do Flask.

## Qualidade e automacao

O projeto possui automacoes configuradas com GitHub Actions para integracao continua e execucao de testes.

Tambem possui configuracao para analise de qualidade com SonarCloud.

## Autor

- Andre Felipe Pereira dos Santos

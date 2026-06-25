# Sistema de Controle de Estoque

## Descricao

Aplicacao web simples para controle de estoque, desenvolvida com Flask no backend e HTML/CSS com Bootstrap no frontend. O sistema possui autenticacao de usuarios e CRUD de produtos, incluindo cadastro, listagem, edicao e exclusao.

## Origem do projeto e organização dos forks

Este repositório é utilizado para o projeto da disciplina SSC0535 – Gerência de Configuração, Evolução e Manutenção de Software, do Bacharelado em Sistemas de Informação da Universidade de São Paulo.

O sistema de controle de estoque utilizado como base não foi desenvolvido do zero pela equipe. A proposta da disciplina é trabalhar sobre um sistema já existente, aplicando práticas de gerência de configuração, manutenção, evolução de software, análise de qualidade de código e integração contínua.

A organização dos repositórios ficou definida da seguinte forma:

* Repositório original do sistema: `https://github.com/liipeandre/sistema-controle-estoque-flask`
* Fork utilizado pela equipe: `https://github.com/Thamysis/sistema-controle-estoque`
* Fork individual utilizado para contribuições: `https://github.com/pyerryxavier0308/sistema-controle-estoque`

O repositório `Thamysis/sistema-controle-estoque` passou a ser tratado como o repositório principal da equipe para fins de documentação, análise no SonarCloud, integração contínua e registro das mudanças planejadas. O fork individual foi utilizado para desenvolvimento de alterações em branches separadas, que posteriormente foram propostas ao repositório da equipe por meio de pull requests.

As modificações feitas pela equipe têm foco em manutenção e evolução do sistema, incluindo melhorias de qualidade de código, ajustes de manutenibilidade, correções apontadas pelo SonarCloud, revisão de segurança e configuração de workflow de integração contínua.


## Requisitos

- Python 3.11 ou superior
- MySQL
- pip

## Primeira execucao do projeto

### 1. Clonar o repositorio e entrar na pasta

```bash
git clone <url-do-repositorio>
cd sistema-controle-estoque
```

### 2. Criar e ativar um ambiente virtual

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

Se o ambiente virtual estiver ativo, o terminal normalmente passa a mostrar o prefixo `.venv`.

### 3. Instalar as dependencias do projeto

```bash
pip install -r requirements.txt
```

### 4. Criar o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto a partir do `.env.example`.

Exemplo:

```env
SECRET_KEY=troque_esta_chave
DB_USERNAME=root
DB_PASSWORD=
DB_SERVER=localhost
DB_NAME=sistemacontroleestoque
```

### 5. Criar o banco de dados no MySQL

Abra o MySQL e crie o banco configurado no `.env`.

Exemplo:

```sql
CREATE DATABASE sistemacontroleestoque;
```

Se necessario, ajuste no `.env`:

- `DB_USERNAME`
- `DB_PASSWORD`
- `DB_SERVER`
- `DB_NAME`

### 6. Garantir que a estrutura do banco exista

O projeto espera que o banco MySQL ja esteja disponivel e com as tabelas necessarias para autenticacao e produtos. Se estiver rodando o sistema pela primeira vez em uma base vazia, crie as tabelas conforme a modelagem do projeto.

### 7. Executar a aplicacao

```bash
python app.py
```

Com a aplicacao em execucao, acesse no navegador:

```text
http://127.0.0.1:5000
```

## Execucoes seguintes

Depois da primeira configuracao, o fluxo normal costuma ser:

1. Ativar o ambiente virtual.
2. Garantir que o MySQL esteja em execucao.
3. Conferir se o arquivo `.env` continua presente.
4. Rodar `python app.py`.

## Testes

Para executar os testes localmente:

```bash
pytest
```

## Qualidade e automacao

O projeto possui automacoes configuradas com GitHub Actions para integracao continua e execucao de testes.

Tambem possui configuracao para analise de qualidade com SonarCloud.

## Autores

- [Pyerry Klyzlow Xavier](https://github.com/pyerryxavier0308)
- [Thamyres Santos](https://github.com/Thamysis)

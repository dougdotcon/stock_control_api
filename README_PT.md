# StockControlAPI

## Descrição

**StockControlAPI** é uma API RESTful profissional projetada para gerenciamento eficiente de inventário. Desenvolvida com **Django** e **Django Rest Framework (DRF)**, oferece endpoints abrangentes para gerenciar produtos, vendas, compras, fornecedores, clientes e níveis de estoque. O sistema inclui recursos avançados de relatórios, gerando arquivos de vendas em PDF e Excel.

## Funcionalidades Principais

*   **Operações CRUD:** Funcionalidade completa de Criar, Ler, Atualizar e Deletar para Produtos, Vendas, Compras, Fornecedores, Clientes e Estoque.
*   **Relatórios Avançados:** Gere relatórios detalhados de vendas em PDF e Excel de forma dinâmica.
*   **Testes Automatizados:** Garantia de código de alta qualidade com suíte robusta de testes de unidade e integração.
*   **Pipeline CI/CD:** Integrado com GitHub Actions para integração contínua, garantindo confiabilidade a cada commit.
*   **Fixtures de Dados:** Dados de teste pré-carregados para rápida configuração e demonstração.

## Tecnologias e Ferramentas

*   **Backend:** Python 3.8+, Django 3.2+, Django Rest Framework
*   **Banco de Dados:** MySQL
*   **Testes:** pytest, Factory Boy, Postman
*   **DevOps:** Git, GitHub Actions

## Pré-requisitos

*   Python 3.8+
*   Servidor MySQL
*   pip (Instalador de pacotes Python)

## Instalação e Configuração

### 1. Clone o Repositório

bash
git clone <url-do-repositorio>
cd StockControlAPI


### 2. Configure o Ambiente Virtual

bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate


### 3. Instale as Dependências

bash
pip install -r requirements.txt


### 4. Configure o Banco de Dados

Certifique-se de que o MySQL está rodando e crie o banco de dados:

sql
CREATE DATABASE stock_control_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


### 5. Configure as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

ini
DB_NAME=stock_control_db
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=3306


### 6. Aplique as Migrações

bash
python manage.py migrate


### 7. Carregue os Dados de Teste

bash
python manage.py loaddata app/stock_app/fixtures/test_data.json


### 8. Inicie o Servidor

bash
python manage.py runserver


## Endpoints da API

### Produtos
*   `GET /produtos/` - Listar todos os produtos
*   `POST /produtos/` - Criar um novo produto
*   `GET /produtos/<id>/` - Recuperar detalhes do produto
*   `PUT /produtos/<id>/` - Atualizar um produto
*   `DELETE /produtos/<id>/` - Excluir um produto

### Vendas
*   `GET /vendas/` - Listar todas as vendas
*   `POST /vendas/` - Criar uma nova venda
*   `GET /vendas/<id>/` - Recuperar detalhes da venda
*   `PUT /vendas/<id>/` - Atualizar uma venda
*   `DELETE /vendas/<id>/` - Excluir uma venda

### Relatórios
*   `GET /vendas/report-pdf/` - Gerar Relatório de Vendas (PDF)
*   `GET /vendas/report-excel/` - Gerar Relatório de Vendas (Excel)

## Testes

### Testes Automatizados

Execute a suíte de testes completa usando o runner do Django:

bash
python manage.py test


### Coleção do Postman

1.  Localize o arquivo `postman_collection.json` na raiz do projeto.
2.  Importe-o no Postman.
3.  Execute as requisições para interagir com a API em execução.

## CI/CD

Este projeto utiliza **GitHub Actions** para Integração Contínua. O fluxo de trabalho está configurado para executar todos os testes automatizados a cada push ou pull request para a branch principal, garantindo a estabilidade do código.
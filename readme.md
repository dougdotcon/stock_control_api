# Projeto de Controle de Estoque

## Descrição

Este projeto é uma API RESTful para controle de estoque, desenvolvida utilizando Django e Django Rest Framework. A API permite gerenciar produtos, vendas, compras, vendedores, compradores e estoque. Além disso, a API possui endpoints para geração de relatórios em PDF e Excel.

## Funcionalidades

- CRUD para Produtos, Vendas, Compras, Vendedores, Compradores e Estoque
- Geração de relatórios de vendas em PDF e Excel
- Testes automatizados para garantir a qualidade do código
- Integração com CI/CD usando GitHub Actions

## Ferramentas e Tecnologias Utilizadas

- Django
- Django Rest Framework
- MySQL
- Factory Boy
- Postman
- pytest
- Git
- GitHub Actions

## Requisitos

- Python 3.8+
- Django 3.2+
- MySQL
- pip (Python package installer)

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd projeto-controle-estoque
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados MySQL:**
   - Certifique-se de que o MySQL está instalado e rodando.
   - Crie um banco de dados para o projeto:
     ```sql
     CREATE DATABASE controle_estoque;
     ```

5. **Configure as variáveis de ambiente:**
   - Crie um arquivo `.env` na raiz do projeto com as seguintes configurações:
     ```
     DB_NAME=controle_estoque
     DB_USER=seu_usuario
     DB_PASSWORD=sua_senha
     DB_HOST=localhost
     DB_PORT=3306
     ```

6. **Aplique as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

7. **Carregue os dados de teste:**
   ```bash
   python manage.py loaddata app/stock_app/fixtures/test_data.json
   ```

8. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

## Endpoints Principais

- **Produtos:**
  - `GET /produtos/`: Listar produtos
  - `POST /produtos/`: Criar produto
  - `GET /produtos/<id>/`: Detalhar produto
  - `PUT /produtos/<id>/`: Atualizar produto
  - `DELETE /produtos/<id>/`: Excluir produto

- **Vendas:**
  - `GET /vendas/`: Listar vendas
  - `POST /vendas/`: Criar venda
  - `GET /vendas/<id>/`: Detalhar venda
  - `PUT /vendas/<id>/`: Atualizar venda
  - `DELETE /vendas/<id>/`: Excluir venda

- **Relatórios:**
  - `GET /vendas/report-pdf/`: Gerar relatório de vendas em PDF
  - `GET /vendas/report-excel/`: Gerar relatório de vendas em Excel

## Testes

### Testes Automatizados

Para rodar os testes automatizados, execute:

```bash
python manage.py test
```

### Testes com Postman

1. Importe o arquivo `postman_collection.json` no Postman.
2. Execute as requisições para testar os endpoints da API.

## CI/CD

Este projeto utiliza GitHub Actions para CI/CD. O pipeline está configurado para rodar os testes automaticamente em cada push ou pull request no branch principal.

Para configurar o CI/CD:

1. Garanta que o arquivo `.github/workflows/django.yml` esteja presente na estrutura do projeto.

### Conteúdo do arquivo `django.yml`:

```yaml
name: Django CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.8
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run Tests
      run: |
        python manage.py test
```

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).

---

## Contato

Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

- Nome: Douglas H. Machado
- Email: dougdotcon@gmail.com
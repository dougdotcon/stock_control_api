# StockControlAPI

## Description

**StockControlAPI** is a professional RESTful API designed for efficient inventory management. Developed using **Django** and **Django Rest Framework (DRF)**, it provides comprehensive endpoints to manage products, sales, purchases, suppliers, customers, and stock levels. The system includes advanced reporting capabilities, generating sales reports in both PDF and Excel formats.

## Key Features

*   **CRUD Operations:** Full Create, Read, Update, Delete functionality for Products, Sales, Purchases, Suppliers, Customers, and Inventory.
*   **Advanced Reporting:** Generate detailed sales reports in PDF and Excel formats dynamically.
*   **Automated Testing:** High-quality code assurance with a robust suite of unit and integration tests.
*   **CI/CD Pipeline:** Integrated with GitHub Actions for continuous integration, ensuring reliability with every commit.
*   **Data Fixtures:** Pre-loaded test data for quick setup and demonstration.

## Technologies & Tools

*   **Backend:** Python 3.8+, Django 3.2+, Django Rest Framework
*   **Database:** MySQL
*   **Testing:** pytest, Factory Boy, Postman
*   **DevOps:** Git, GitHub Actions

## Prerequisites

*   Python 3.8+
*   MySQL Server
*   pip (Python package installer)

## Installation & Setup

### 1. Clone the Repository

bash
git clone <repository-url>
cd StockControlAPI


### 2. Set Up Virtual Environment

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


### 3. Install Dependencies

bash
pip install -r requirements.txt


### 4. Configure Database

Ensure MySQL is running and create the database:

sql
CREATE DATABASE stock_control_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


### 5. Configure Environment Variables

Create a `.env` file in the project root:

ini
DB_NAME=stock_control_db
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306


### 6. Run Migrations

bash
python manage.py migrate


### 7. Load Test Data

bash
python manage.py loaddata app/stock_app/fixtures/test_data.json


### 8. Run the Server

bash
python manage.py runserver


## API Endpoints

### Products
*   `GET /produtos/` - List all products
*   `POST /produtos/` - Create a new product
*   `GET /produtos/<id>/` - Retrieve product details
*   `PUT /produtos/<id>/` - Update a product
*   `DELETE /produtos/<id>/` - Delete a product

### Sales
*   `GET /vendas/` - List all sales
*   `POST /vendas/` - Create a new sale
*   `GET /vendas/<id>/` - Retrieve sale details
*   `PUT /vendas/<id>/` - Update a sale
*   `DELETE /vendas/<id>/` - Delete a sale

### Reports
*   `GET /vendas/report-pdf/` - Generate Sales Report (PDF)
*   `GET /vendas/report-excel/` - Generate Sales Report (Excel)

## Testing

### Automated Tests

Run the full test suite using the Django test runner:

bash
python manage.py test


### Postman Collection

1.  Locate the `postman_collection.json` file in the project root.
2.  Import it into Postman.
3.  Execute the requests to interact with the live API.

## CI/CD

This project uses **GitHub Actions** for Continuous Integration. The workflow is configured to run all automated tests on every push or pull request to the main branch, ensuring code stability.
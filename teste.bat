@echo off
SET project_dir=stock_control_api
SET app_dir=%project_dir%\app
SET stock_app_dir=%project_dir%\stock_app

mkdir %project_dir%
mkdir %app_dir%
mkdir %app_dir%\migrations
mkdir %stock_app_dir%
mkdir %stock_app_dir%\migrations

echo from django.conf import settings > %app_dir%\__init__.py
echo from django.core.wsgi import get_wsgi_application > %app_dir%\wsgi.py
echo from django.core.asgi import get_asgi_application > %app_dir%\asgi.py

type nul > %app_dir%\settings.py
type nul > %app_dir%\urls.py

echo if __name__ == '__main__': > %project_dir%\manage.py
echo    execute_from_command_line(sys.argv) >> %project_dir%\manage.py

type nul > %stock_app_dir%\__init__.py
type nul > %stock_app_dir%\admin.py
type nul > %stock_app_dir%\apps.py
type nul > %stock_app_dir%\models.py
type nul > %stock_app_dir%\tests.py
type nul > %stock_app_dir%\views.py
type nul > %stock_app_dir%\serializers.py
type nul > %stock_app_dir%\urls.py

echo # Empty Dockerfile for now > %project_dir%\Dockerfile
echo # Empty docker-compose for now > %project_dir%\docker-compose.yml
echo # Requirements file > %project_dir%\requirements.txt
echo DJANGO_SECRET_KEY=your_secret_key_here > %project_dir%\.env

echo Estrutura de pastas criada com sucesso!
pause

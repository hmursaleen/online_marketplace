# Browse the live website at https://mursaleen.pythonanywhere.com/
# If you want to setup this project on your local computer, follow the instructions below
## Open Command Prompt and insert the corresponding commands 
## Clone the repository: 
```git clone https://github.com/hmursaleen/online_marketplace```
## Install Packages: 
```pip install -r requirements.txt```
## Setup Virtualenv: 
```python -m venv virtual_environment_name```
### Activate the virtual environment: 
```virtual_environment_name\Scripts\activate```

## Migrate the database:
### First change the directory: 
```cd ecommerce```
### Make Migrations: 
```py manage.py makemigrations```
### Run migrations: 
```py manage.py migrate```

## Run the server: 
```py manage.py runserver```
## Now browse to 127.0.0.1:8000 on your local machine to explore the website

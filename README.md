# Contact List

API for contact list

# API Structure:
This api implements the following endpoints:

| Endpoint  | HTTP Method | Result  |
| ------------- | ------------- | ------------- |
| /api/contact/  | GET  | List all contact
| /api/contact/  | POST  | Add a single contact
| /api/contact/:id  | GET  | Get a single contact
| /api/contact/:id  | PUT  | Update a single contact
| /api/contact/:id  | DELETE  | Delete a single contact

# How to run a API ?
1. Clone this repository
2. Create a vritualenv with python 3.6
3. Active your virtualenv
4. Install all dependencies
5. Install a Postgres database
5. Create database
6. Create a user and password from database
5. Configure all env vars with .env
6. Run tests
7. Run a instance

``` console
git clone git@github.com:marceloandriolli/contact-list-api.git contact_list_api
cd contact_list_ap
python -m venv .contact_list_ap
source .contact_list_ap/bin/activate
pip install -r requirements.txt
sudo apt-get update && sudo apt-get install postgresql postgresql-contrib
createdb <your_data_base>
createuser -P -s <yout_user>
cp contrib/env-sample .env
python manage.py test
python manage.py runserver
``` 

# Improvements:
1. Data model: Create a person model, remove "name" field from contact model and add foreign key to person
2. User DRF routers
3. Use uuid on person model instead sequencia id
4. Use generic CBV mixins from DRF om views
5. Add Travis CI on project
6. Add Codecov on project

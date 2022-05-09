# gemini

A minimal blog inspired by reddit and developed with Django and Tailwind CSS:

- use pip to install the dependencies: **pip3 install -r requirements.txt**

- then to run the project `python manage.py runserver`

- to run the project with tailwind, open 2 terminal window: 
    1. `python manage.py tailwind start` (if any css change is needed)
    2. `python manage.py runserver`
  
### Troubleshooting:

To solve this error:

`ERROR: Could not find a version that satisfies the requirement mysqlclient` \
`ERROR: No matching distribution found for mysqlclient`

just install the libraries with:

`sudo apt install libmariadb-dev-compat libmariadb-dev`


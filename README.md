# OpenStage API

## Setup

```
$ virtualenv openstage-api
$ cd openstage-api
$ source bin/activate
$ git clone {{repo_url}} app
$ cd app
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

## Settings

We are version controlling all config files except for the `__init__.py` that says which one to use. Run this command from the project root:

```
$ echo "from .dev import *" > ./openstage/settings/__init__.py
```

## Admin

Run this command and follow prompts

```
python manage.py createsuperuser
```

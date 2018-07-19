# OpenStage API

## Setup

```
$ virtualenv openstage-api
$ cd openstage-api
$ source bin/activate
$ git clone {{repo_url}} app
$ cd app
$ pip install -r requirements.txt
$ echo "from .dev import *" > ./openstage/settings/__init__.py
$ python manage.py migrate
$ python manage.py runserver
```


## Admin

Run this command and follow prompts

```
python manage.py createsuperuser
```

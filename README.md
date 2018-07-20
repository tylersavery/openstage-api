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

## About this Project

### Watch The Development

I am streaming the project from start to finish on LiveEDU. Here is a link to my [profile](https://www.liveedu.tv/tylersavery/settings/channel/).

### Overview

MyOpenStage is a handy website+app to help you find where you can perform tonight.
Data entry will be focused on Toronto at first, but will work anywhere in theory.

### Release Plan

MVP

- lists venues and events on a map an list view and lets you filter by date.
- only handling weekly recurring events currently.
- works without user authentication
- users can signup / login + general auth stuff
- data inputted from django backend

v 1.1

- users can rsvp/checkin to events (ahead of time or during)
- sharing to fb/twitter/etc. (perhaps generate a 1:1 / 9:16 graphic for Insta/Snap)
- users can add photos from the events
- adding facebook/google/twitter connect for authentication
- light dashboard for admins (making creating venues and events easier)

v1.2

- users can add events and venues through app
- users can become "hosts" of events and "managers" of venues
- social layer for following performers/hosts/etc.
- notifications / reminders
- dashboard for venue managers / hosts

### Models

Overall, trying to keep simple. Original intention was to have a "venue" model and an "event" model but there aren't really any cases in the real world where the same venue hosts different events... so KISS.

Also, considered using a complex date system for recurring, but again, generally Open Mics are consistantly the same day of the week every week.

#### Stage

- kind (comedy, music, any)
- start_time
- end_time
- signup_time
- signup_info
- included_gear
- {{thumb_image}} (fk: image)
- {{images}} (m2m: image)
- venue_name
- venue_address
- venue_city
- venue_state
- venue_country
- venue_latitude
- venue_longitude
- day_of_week (mon,tues,wed,etc.)

#### Image

- url
- width
- height

#### Profile

Note: using a one-to-one for profiles tied to the default Django User model.

https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone

- {{user}}
- is_performer
- is_host (will need to add m2m for hosts|stages)
- bio
- location
- etc.

Rsvp

- {{stage}}
- {{user}}
- date
- comment

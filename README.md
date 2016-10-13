# Geo-feedback (based on heroku django starter template)

## heroku environment variables

create a .env file ...

## Linux

$ heroku local

## Windows

### Setup notes

When we installed the heroku cli, it added a call the the MySQL binary to the %Path% variable ... !
Just remove it, and things start to work.

### Running

$ heroku local -f Procfile.windows

### Migrating

$ heroku local release -f Procfile.windows


### Running tests locally

$ heroku local:run python manage.py test
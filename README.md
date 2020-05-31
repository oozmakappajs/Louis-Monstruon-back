# Oozmakapajs Backend development workflow

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org).

```sh
$ git clone https://github.com/oozmakappajs/Louis-Monstruon-back.git
$ cd Louis-Monstruon-back

$ python3 -m venv .env
$ source .env/bin/activate

$ pip3 install -r requirements.txt
$ python3 manage.py runserver

```

Your app should now be running on [localhost:8000](http://localhost:8000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

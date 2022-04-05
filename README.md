# SimpleFastAPIExample

[![python](https://img.shields.io/pypi/pyversions/fastapi)]()

This is a simple API-REST created with FastApi. Could be a template for next projects or a simple example for learn.

This app use:

* [SQLite](http://www.sqlite.org/) (Database)
* [Alembic](https://alembic.sqlalchemy.org/en/latest/) (Migrations)
* [SQLAlchemy](https://www.sqlalchemy.org/) (ORM)
* [Pydantic](https://pydantic-docs.helpmanual.io/) (Schemas)
* [PyTest](https://docs.pytest.org/) (Tests)
* [python-jose](https://python-jose.readthedocs.io/en/latest/) (jwt for auth)
* [passlib](https://passlib.readthedocs.io/en/stable/) (encrypt passwords)

The idea of the app is simulate Users that create and participate in  Projects. So the schema of the database is a simple relation many-to-many between Users and Projects, using a Association model called UserProjects.

Trying to do some basic functionalities of an API REST like:

* Authentication:
    - Login
    - Forgot-password
    - Reset-password
* CRUD for resources
    - User
    - Project
* Send emails (pending)
    - Reset password email
* Background tasks (pending)
    - The reset password email render after return
* File storage system - upload files to aws maybe (pending)
    - Upload a avatar for users
* TESTS

## API Documentation

You can find the app running on heroku so the interactiv documentation can be found [here](https://simple-fastapi-example.herokuapp.com/docs).


## Installation

I recommend create your own virtual enviroment using [pipenv](https://pipenv.pypa.io). After that:

```bash
pipenv install
```

Or with other enviroment management tool:

```bash
pip install -r requirements.txt
```

## Test

For run tests go to the project folder and execute:

```bash
pytest
```

## Serve

For serve run:

```bash
uvicorn app.main:app
```

If you are going to make changes on the project use the --reload flag so you see the changes in the moment without restart the server:

```bash
uvicorn app.main:app --reload
```


## Release History

* 0.0.1
    * Work in progress

## Meta

Andres – andres.ch(at)protonmail(dot)com


[https://github.com/a-chacon/github-link](https://github.com/a-chacon/)

## Contributing

1. Fork it (<https://github.com/a-chacon/simple-fastapi-example/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

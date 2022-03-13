# SimpleFastAPIExample

[![python](https://img.shields.io/pypi/pyversions/fastapi)]()

This is a simple API-REST created with FastApi.

This app use:

* [SQLite](http://www.sqlite.org/) (Database)
* [Alembic](https://alembic.sqlalchemy.org/en/latest/) (Migrations)
* [SQLAlchemy](https://www.sqlalchemy.org/) (ORM)
* [Pydantic](https://pydantic-docs.helpmanual.io/) (Schemas)
* [PyTest](https://docs.pytest.org/) (Tests)
* [python-jose](https://python-jose.readthedocs.io/en/latest/) (jwt for auth)
* [passlib](https://passlib.readthedocs.io/en/stable/) (encrypt passwords)

Trying to do some basic functionalities of an API REST like:

* Authentication
* CRUD for resources (working)
* Send emails (pending)
* Background tasks (pending)
* File storage system - upload files to aws maybe (pending)
*TESTS




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


[https://github.com/a-chacon/github-link](https://github.com/dbader/)

## Contributing

1. Fork it (<https://github.com/a-chacon/simple-fastapi-example/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

# SimpleExampleFastAPI

[python-img]

This is a simple API-REST created with FastApi.

This app use:

* [SQLite](http://www.sqlite.org/) (Database)
* [Alembic](https://alembic.sqlalchemy.org/en/latest/) (Migrations)
* [SQLAlchemy](https://www.sqlalchemy.org/) (ORM)
* [Pydantic](https://pydantic-docs.helpmanual.io/) (Schemas)
* [PyTest](https://docs.pytest.org/) (Tests)
* [python-jose](https://python-jose.readthedocs.io/en/latest/) (jwt for auth)
* [passlib](https://passlib.readthedocs.io/en/stable/) (encrypt passwords)


## Installation

I recommend create your own virtual enviroment. After that:

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

If you are going to make changes on the project use the --reload flag.

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

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->

[python-img]: https://img.shields.io/pypi/pyversions/p.svg

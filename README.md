# Minyma Python+FastApi starter template
> Kickstart your backend application with a pre-configured FastAPI + SQLAlchemy template


## What's included?
- [x] [FastAPI](https://fastapi.tiangolo.com/) as web framework
- [x] [SQLAlchemy](https://www.sqlalchemy.org/) as the ORM
- [x] [PostreSQL](https://www.postgresql.org/) as database engine
- [x] [Alembic](https://alembic.sqlalchemy.org/en/latest/) for database migrations
- [x] [JWT](https://jwt.io/) for auth 
- [x] [Poetry](https://python-poetry.org/) as package manager
- [x] [PyTest](https://docs.pytest.org/en/7.2.x/) for unit testing
- [x] [Black](https://black.readthedocs.io/en/stable/) for code formatting
- [x] [Ruff](https://github.com/charliermarsh/ruff) for linting
- [x] [Docker](https://www.docker.com/) for containerization
- [x] Github Actions for CI checks (lint, test, coverage)
  
## Install
### Fetch the code
Clone repo, remove git history:
```
git clone https://github.com/minyma-technologies/python-fastapi-starter
cd python-fastapi-starter
rm -rf ./.git
git init
```

**Alternatively**, on GitHub hit `Use this template` to create a new repository based on this, but without the git history. You can then clone the new repository to your machine.

### Install dependencies
- this template uses Poetry. You can install it like so: `pip install poetry`
- once installed run `poetry install` to install the dependencies

### Run the application locally
```
poe dev
```
or, for live preloads:
```
poe watch
```

### Run application in Docker container
```
docker-compose up --build
```

## Usage

### Using Poetry
Poetry is an alternative python package manager. From experience, the default python package manager `pip` and the virtual environment tool `venv` are poorly designed and often cause package configuration issues. Enter poetry: a modern package manager with a more sane API.
- create virtual environment: `poetry shell`
- add dependency: `poetry add <pacakage>`
- add dev dependency: `poetry add <pacakage> -G dev`

### Running migrations
- the template is set up with alembic, an automatic migrations tool for SQLAlchemy. 
- To automatically run migrations against the database run `poe db_pull`
- To automatically genrate migrations against the database run `poe db_push <message>`


### Configuration and secrets
There are three different environments preconfigured: `test`, `dev`, and `prod`. To switch environments set `APP_ENV` to one of the above environment names. Use `dev.env` (default, for `dev`), `test.env` and `.prod.env` for storing the values. Note the `.` before `prod.env`: adding a dot before any file will automatically git ignore it.

### Development scripts
As a drop-in replacement for `npm run ...` you can use `poe`. This way you can change development scripts in one place and each collaborator can then use the updated script, without thinking about flags and options.
Avaialble scripts are:

| Command                 | Description                                        |
| ----------------------- | -------------------------------------------------- |
| `poe fix`               | Run black, ruff and mypy to fix lint issues        |
| `poe check`             | Run black, ruff and mypyp to check for lint issues |
| `poe test`              | Run unit tests                                     |
| `poe coverage`          | Run coverage test                                  |
| `poe prod`              | Start the app   in prod mode                       |
| `poe dev`               | Start the app in dev with mode                     |
| `poe watch`             | Start the app in dev mode with live reload         |
| `poe db_push <message>` | Autogenerate database migration                    |
| `poe db_pull`           | Apply migrations                                   |

## TODO:

- [ ] service layer tests
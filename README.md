# Minyma Python+FastApi starter template
> Kickstart your backend application with a pre-configured FastAPI + SQLAlchemy template


## What's included?
- [x] [FastAPI](https://fastapi.tiangolo.com/) as web framework
- [x] [SQLAlchemy](https://www.sqlalchemy.org/) as the ORM
- [x] [PostreSQL](https://www.postgresql.org/) as database engine
- [x] [JWT](https://jwt.io/) for auth 
- [x] [Poetry](https://python-poetry.org/) as package manager
- [x] [PyTest](https://docs.pytest.org/en/7.2.x/) for unit testing
- [x] [Black](https://black.readthedocs.io/en/stable/) for code formatting
- [x] [Ruff](https://github.com/charliermarsh/ruff) for linting
  
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
poetry run uvicorn app.main:app --port <port>
```
or, for live preloads:
```
poetry run uvicorn app.main:app --port <port> --reload
```

### Run application in Docker container
> Coming soon...

## Usage

### Using Poetry
Poetry is an alternative python package manager. From experience, the default python package manager `pip` and the virtual environment tool `venv` are poorly designed and often cause package configuration issues. Enter poetry: a modern package manager with a more sane API.
- create virtual environment: `poetry shell`
- add dependency: `poetry add <pacakage>`
- add dev dependency: `poetry add <pacakage> -G dev`

### Running migrations
- the template is set up with alembic, an automatic migrations tool for SQLAlchemy. To automagically update the database schema after making changes to the data model, run `alembic revision --autogenerate -m <message>`, then `alembic upgrade head`

### Configuration and secrets
There are three different environments preconfigured: `test`, `dev`, and `prod`. To switch environments set `APP_ENV` to one of the above environment names. Use `.env` (default, for `dev`), `.env.test` and `.env.prod` for storing the values. A sample configuration is provided in `.env.sample`

### Development scripts
As a jump-in replacement for `npm run ...` you can use `make`. This way you can change development scripts in one place and each collaborator can then use the updated script, without thinking about flags and options.
Avaialble scripts are:

| Command           | Description                                 |
| ----------------- | ------------------------------------------- |
| `make lint_fix`   | Run black and ruff to fix lint issues       |
| `make lint_check` | Run black and ruff to check for lint issues |
| `make test`       | Run unit tests                              |
| `make coverage`   | Run coverage test                           |
| `make start`      | Start the app                               |
| `make start_dev`  | Start the app with live reload              |

## TODO:

- [ ] create Dockerfile and docker-compose file
- [ ] setup pre-commit
- [ ] service layer tests
- [ ] auto changelog
- [ ] semantic versioning?
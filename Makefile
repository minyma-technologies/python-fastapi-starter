lint_fix:
	poetry run black app && poetry run ruff --fix app

lint_check:
	poetry run black app --check && poetry run ruff app

test:
	APP_ENV=test poetry run pytest tests
	
coverage:
	APP_ENV=test poetry run pytest tests --cov
	
start:
	poetry run uvicorn app.main:app
	
start_dev:
	poetry run uvicorn app.main:app --reload
	
install:
	poetry install && pre-commit install --hook-type pre-push
	
install_prod:
	poetry install --without dev
	
check_commit_msg:
	poetry run cz check --rev-range HEAD~..HEAD
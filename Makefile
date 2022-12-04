lint_fix:
	black app && ruff --fix app

lint_check:
	black app --check && ruff app

test:
	APP_ENV=test pytest tests
	
coverage:
	APP_ENV=test pytest tests --cov
	
start:
	poetry run uvicorn app.main:app
	
start_dev:
	poetry run uvicorn app.main:app --reload
	
install:
	poetry install && pre-commit install --hook-type pre-push
	
install_prod:
	poetry install --without dev
	
check_commit_msg:
	cz check --rev-range HEAD~..HEAD
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
lint_fix:
	black app && ruff --fix app

lint_check:
	black app --check && ruff app

test:
	APP_ENV=test pytest tests
	
coverage:
	APP_ENV=test pytest tests --cov
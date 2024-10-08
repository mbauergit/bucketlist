
install:
	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=test_*.py

format:	
	black *.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py modules/*.py

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format


install:
	
	pip install --upgrade pip &&\
	

test:
	python -m pytest -vv test_hello.py

lint:
	pylint --disable=R,C hello.py

all: install lint test

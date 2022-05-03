install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	|
test:
	python -m pytest -vv test_hello.py

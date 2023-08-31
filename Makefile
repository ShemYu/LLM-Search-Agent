.PHONY: run

run:
	uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload

lint:
	isort .
	black .

tree:
	tree -I *.pyc -I TSMC* -I test_chroma -I __pycache__ .
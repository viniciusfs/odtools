PYTHON = python3

.PHONY = run shell clean

run:
	${PYTHON} manage.py server

shell:
	${PYTHON} manage.py shell

clean:
	find . -name "*.pyc" -exec rm {} \;


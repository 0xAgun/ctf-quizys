
.PHONY : build
build:
	clear
	python3 -m pip install -r requirements.txt
	python3 manage.py runserver


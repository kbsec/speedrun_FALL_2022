.PHONY: dev

dev:
	export FLASK_APP=speedrun.app:app ;export FLASK_ENV=development;  flask run


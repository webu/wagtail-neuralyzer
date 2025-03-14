export DJANGO_SETTINGS_MODULE = tests.settings
export PYTHONPATH := $(shell pwd)


maketranslations:
	cd wagtail_neuralyzer; django-admin makemessages -a -v2

compiletranslations:
	cd wagtail_neuralyzer; django-admin compilemessages

translations:  maketranslations compiletranslations
	@echo "Making and compiling translations"


.PHONY: maketranslations compiletranslations

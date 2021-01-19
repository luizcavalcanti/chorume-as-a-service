.PHONY: help

help:
	@echo "available actions: deps, export, block"

deps:
	@pip3 install -r requirements.txt

export:
	@python3 -m chorume export

block:
	@python3 -m chorume block
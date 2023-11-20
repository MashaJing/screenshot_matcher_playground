export APP_URL ?= https://mashajing.github.io/screenshot_matcher_playground/
export TEST_APP_URL ?= http://localhost:8000/


.PHONY: install-dependencies
install-dependencies:
	@python3 -m venv .venv; \
	source .venv/bin/activate; \
	pip3 install -r requirements.txt; \
	playwright install


.PHONY: up
up:
	@python3 server.py


.PHONY: e2e
e2e:
	@cd tests; \
	python3 -m vedro run $(args)

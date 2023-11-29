export APP_URL ?= https://mashajing.github.io/screenshot_matcher_playground/
export TEST_APP_URL ?= http://localhost:8000/


.PHONY: install-dependencies
install-dependencies:
	@​​pip install -r requirements.in


.PHONY: up
up:
	@python3 server.py


.PHONY: e2e
e2e:
	@cd tests; \
	python3 -m vedro run $(args)

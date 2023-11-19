export APP_URL ?= http://localhost:8000/
export TEST_APP_URL ?= http://localhost:8001/


.PHONY: install-dependencies
install-dependencies:
	@python3 -m venv .venv; \
	source .venv/bin/activate; \
	pip3 install -r requirements.txt; \
	playwright install


.PHONY: master-up
master-up:
	@TARGET_COMMIT=`git merge-base origin/master HEAD`; \
	git diff --name-only --diff-filter=ACMT $$TARGET_COMMIT | python3 app/server.py


.PHONY: up
up:
	@python3 app/server.py


.PHONY: e2e
e2e:
	@python3 -m vedro run $(args)

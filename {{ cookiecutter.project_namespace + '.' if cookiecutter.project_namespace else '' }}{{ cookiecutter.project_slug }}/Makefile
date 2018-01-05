
REQUIREMENTS := $(wildcard requirements*.txt)

clean: clean-requirements
	make -C docs clean

clean-requirements: $(REQUIREMENTS)
	rm -f $(REQUIREMENTS)

requirements-compile:
	pip-compile requirements.in
	pip-compile requirements-doc.in
	pip-compile requirements-test.in
	pip-compile requirements-dev.in

requirements: requirements-compile
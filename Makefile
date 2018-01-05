
REQUIREMENTS := $(wildcard requirements*.txt)

clean: clean-requirements
	make -C docs clean
	rm -f .tested_requirements.txt

clean-requirements: $(REQUIREMENTS)
	rm -f $(REQUIREMENTS)

requirements:
	pip-compile requirements.in
	pip-compile requirements-doc.in
	pip-compile requirements-test.in
	pip-compile requirements-dev.in

	# Hack, because ruamel.ordereddict is a broken optional dependency
	# of ruamel.yaml, and cannot yet be excluded by pip-compile
	#
	# https://bitbucket.org/ruamel/ordereddict/issues/8/build-failures-with-python36
	# https://github.com/jazzband/pip-tools/issues/333

	sed -i '/ruamel.ordereddict/d' requirements-dev.txt
	sed -i '/ruamel.ordereddict/d' requirements-doc.txt
	sed -i '/ruamel.ordereddict/d' requirements.txt
	sed -i '/ruamel.ordereddict/d' requirements-test.txt

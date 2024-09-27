SRC="src/saleor_app"


lint:
	@black ${SRC}
	@isort -rc ${SRC}
	@autopep8 --in-place --aggressive --recursive ${SRC}
	@flake8 ${SRC}

docs:
	@mkdocs build -s

tox:
	tox -p -q

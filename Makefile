install: #install poetry
	poetry install

brain-games: #run brain-games
	poetry run brain-games

build: #run build package
	poetry build

publish: #run publish package in PyPI
	poetry publish --dry-run

package-install: #install package
	python3 -m pip install --user dist/*.whl

install: #install poetry
	poetry install

build: #run build package
	poetry build

publish: #run publish package in PyPI
	poetry publish --dry-run

package-install: #install package
	python3 -m pip uninstall dist/*.whl
	python3 -m pip install --user dist/*.whl

lint: #linter for code
	poetry run flake8 brain_games

brain-games: #run greeting
	poetry run brain-games

brain-even: #run brain-even
	poetry run brain-even

brain-calc: #run brain-calc
	poetry run brain-calc

brain-gcd: #run brain-gcd
	poetry run brain-gcd

brain-progression: #run brain-progression
	poetry run brain-progression

brain-prime: #run brain-prime
	poetry run brain-prime

install: venv-hiding

	poetry install

venv-hiding:

	echo ".venv" >> .gitignore

lint:

	poetry run flake8 brain_games

brain-games:

	poetry run brain-games

build:

	poetry build

publish:

	poetry publish --dry-run

package-install:

	python3 -m pip install --user dist/*.whl


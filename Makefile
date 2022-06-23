install:
	poetry install
	
build:
	poetry build
	
publish:
	poetry publish --dry-run
	
package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip uninstall dist/*.whl
	python3 -m pip install --user dist/*.whl

brain-games:
	poetry run brain-games

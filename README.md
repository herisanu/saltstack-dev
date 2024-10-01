# saltstack-dev
Saltstack development of modules and states


ipython, debugpy

GENERATE_SALT_SYSPATHS=1 pip install --global-option='--salt-root-dir=/path/to/your/virtualenv/' \
    -e ./salt   # the path to the salt git clone from above

(install) root@531db3c8e671:/code/salt# nox -e 'test-zeromq-3(coverage=False)'
nox > Running session test-zeromq-3(coverage=False)
nox > Creating virtual environment (virtualenv) using python3 in .nox/test-zeromq-3-coverage-false
nox > Session test-zeromq-3(coverage=False) was successful.
nox > Running session test-parametrized-3(crypto=None, transport='zeromq', coverage=False)
nox > Creating virtual environment (virtualenv) using python3 in .nox/test-parametrized-3-crypto-none-transport-zeromq-coverage-false
nox > python -m pip install --progress-bar=off -U setuptools pip wheel
nox > python -m pip install --progress-bar=off -r requirements/static/ci/py3.11/linux.txt
nox > python -m pytest --rootdir /code/salt --log-file-level=debug --show-capture=no -ra -s -vv --showlocals --log-file=/code/salt/artifacts/logs/runtests-20241001084215.963310.log --transport=zeromq
<frozen importlib._bootstrap>:1049: ImportWarning: NaclImporter.find_spec() not found; falling back to find_module()
============================================= test session starts ==============================================
platform linux -- Python 3.11.2, pytest-8.1.1, pluggy-1.4.0 -- /code/salt/.nox/test-parametrized-3-crypto-none-transport-zeromq-coverage-false/bin/python
cachedir: .pytest_cache
max open files: soft=1048576; hard=1048576
salt-transport: zeromq
rootdir: /code/salt
configfile: pytest.ini
testpaths: tests
plugins: httpserver-1.0.8, helpers-namespace-2021.12.29, timeout-2.3.1, pyfakefs-5.3.1, flaky-3.8.1, custom-exit-code-0.3.0, salt-factories-1.0.1, system-statistics-1.0.2, skip-markers-1.5.0, subtests-0.4.0, shell-utilities-1.8.0, anyio-4.1.0
collected 19664 items / 20 deselected / 6 skipped / 19644 selected

...

= 22 failed, 13327 passed, 6210 skipped, 20 deselected, 2 xfailed, 808 warnings, 97 errors in 955.99s (0:15:55) =
nox > Command python -m pytest --rootdir /code/salt --log-file-level=debug --show-capture=no -ra -s -vv --showlocals --log-file=/code/salt/artifacts/logs/runtests-20241001084215.963310.log --transport=zeromq failed with exit code 1
nox > Session test-parametrized-3(crypto=None, transport='zeromq', coverage=False) failed.
nox > Ran multiple sessions:
nox > * test-zeromq-3(coverage=False): success
nox > * test-parametrized-3(crypto=None, transport='zeromq', coverage=False): failed
(install) root@531db3c8e671:/code/salt#

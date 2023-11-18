from invoke import task


@task
def test(c):
    """
    Ejecución de las pruebas unitarias
    """
    c.run("pytest tests/tests.py")

@task
def clean(c):
    c.run("find . -name '*.pyc' -exec rm -f {} +")

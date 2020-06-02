from .pyguess import pyguess


def test():
    assert pyguess("1.0") == 1.0
    assert pyguess("1") == 1
    assert pyguess("true") is True
    assert pyguess("false") is False
    assert pyguess("None") is None
    assert pyguess("""{"name":"John"}""") == {"name": "John"}
    assert pyguess("some string") == "some string"

    assert pyguess("1.0", cast=False) == float
    assert pyguess("1", cast=False) == int
    assert pyguess("true", cast=False) == bool
    assert pyguess("false", cast=False) == bool
    assert pyguess("None", cast=False) == type(None)
    assert pyguess("""{"name":"John"}""", cast=False) == dict
    assert pyguess("some string", cast=False) == str


test()

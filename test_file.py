import pytest
from _pytest.python_api import approx


class TestMain:
    @classmethod
    def setup_class(cls):
        print("setup class")

    def setup_method(self, method):
        print("setup method")

    def teardown_method(self, method):
        print("teardown method")

    def test_main(self):
        print("test main")

    def test_InAssert(self):
        assert 1 == 1

    def test_StrAssert(self):
        assert "str" == "str"

    def test_arrayAssert(self):
        assert [1, 2, 3] == [1, 2, 3]

    def test_dictAssert(self):
        assert {"a": 1, "b": 2} == {"a": 1, "b": 2}

    def test_float(self):
        assert (0.1 + 0.2) == approx(0.3)

    def raiseValueException(self):
        raise ValueError

    def test_exception(self):
        with pytest.raises(ValueError):
            self.raiseValueException()
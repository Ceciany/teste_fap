import pytest
from menu import Calculator1

@pytest.fixture
def calc():
    return Calculator()

def test_adicao(calc: Calculator):
    assert calc.adicao(2, 3) == 5

def test_subtracao(calc: Calculator):
    assert calc.subtracao(5, 3) == 2

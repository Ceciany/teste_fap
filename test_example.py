import pytest
from menu import Calculator1

@pytest.fixture
def calc():
    return Calculator1()

def test_adicao(calc: Calculator1):
    assert calc.adicao(2, 3) == 5

def test_subtracao(calc: Calculator1):
    assert calc.subtracao(5, 3) == 2

import pytest
from main import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_adicao(calc):
    assert calc.adicao(2, 3) == 5

def test_subtracao(calc):
    assert calc.subtracao(5, 3) == 2
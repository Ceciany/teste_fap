import pytest
from menu import Calculator
@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(10,5)==15

def test_subtract(calc):
    assert calc.subtract(10,5)==5
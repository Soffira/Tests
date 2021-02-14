import pytest
from work_calc import Calc
# from hard_Calc import Calc_hard, Calc_hard2

NUMBER_1 = 3.0
NUMBER_2 = 2.0

@pytest.fixture
def calculator():
    return Calc()

# def test_add():
#     value = add(NUMBER_1, NUMBER_2)
#     assert value == 5.0
def test_add(calculator):
    examp = calculator.add(NUMBER_1, NUMBER_2)
    answer = NUMBER_1 + NUMBER_2
    assert examp == answer, 'Good job'

def test_minus(calculator):
    examp = calculator.min(NUMBER_1, NUMBER_2)
    answer = NUMBER_1 - NUMBER_2
    assert examp == answer, 'Good job'

def test_multiply(calculator):
    examp = calculator.mult(NUMBER_1, NUMBER_2)
    answer = NUMBER_1 * NUMBER_2
    assert examp == answer, 'Good job'

def test_divide(calculator):
    examp = calculator.div(NUMBER_1, NUMBER_2)
    answer = NUMBER_1 / NUMBER_2
    assert examp == answer, 'Good job'

def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionError) as e:
        div(NUMBER_1, 0)
    assert "division by zero" in str(e.value)

def test_divide_end(calculator):
    examp = calculator.div_end(NUMBER_1, NUMBER_2)
    answer = NUMBER_1 // NUMBER_2
    assert examp == answer, 'Good job'

def test_degree(calculator):
    examp = calculator.degree(NUMBER_1, NUMBER_2)
    answer = NUMBER_1 ** NUMBER_2
    assert examp == answer, 'Good job'

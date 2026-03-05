from calculator import Calculator

def test_full_addition_flow():
    calc = Calculator()
    result = calc.add(5, 3)
    assert result == 8

def test_clear_after_operation():
    calc = Calculator()
    calc.add(5,3)
    result = calc.clear()
    assert result == 0
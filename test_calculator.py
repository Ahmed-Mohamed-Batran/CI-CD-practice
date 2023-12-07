# test_calculator.py
import pytest
from calculator import calculator

# Test cases
test_case_1 = {'a': 5, 'b': 3, 'operation': 'addition', 'expected_result': 8}
test_case_2 = {'a': 8, 'b': 2, 'operation': 'subtraction', 'expected_result': 6}
test_case_3 = {'a': 4, 'b': 6, 'operation': 'multiplication', 'expected_result': 24}
test_case_4 = {'a': 9, 'b': 3, 'operation': 'division', 'expected_result': 3}

# Pytest test functions
def test_addition():
    result = calculator(test_case_1['a'], test_case_1['b'], 'addition')
    assert result == test_case_1['expected_result']

def test_subtraction():
    result = calculator(test_case_2['a'], test_case_2['b'], 'subtraction')
    assert result == test_case_2['expected_result']

def test_multiplication():
    result = calculator(test_case_3['a'], test_case_3['b'], 'multiplication')
    assert result == test_case_3['expected_result']

def test_division():
    result = calculator(test_case_4['a'], test_case_4['b'], 'division')
    assert result == test_case_4['expected_result']

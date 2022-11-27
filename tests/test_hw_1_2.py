import pytest
from hw_7_1_2 import Stack
from tests.fixtures import *

tester = Stack()

def test_is_empty():
    result = tester.is_empty()
    assert result == True

def test_is_empty_false():
    tester.push('test')
    result = tester.is_empty()
    assert result == False
    tester.pop()

@pytest.mark.parametrize('filler, exp_res', FIXTURES_FILLING)
def test_push(filler, exp_res):
    result = tester.push(filler)
    assert result == exp_res

@pytest.mark.parametrize('filler, exp_res', reversed(FIXTURES_FILLING))
def test_pop(filler, exp_res):
    result = tester.pop()
    assert result == exp_res

@pytest.mark.parametrize('filler, exp_res', FIXTURES_FILLING)
def test_peek(filler, exp_res):
    tester.push(filler)
    result = tester.peek()
    assert result == exp_res
    tester.pop()

@pytest.mark.parametrize('filler, exp_res', FIXTURES_SIZE)
def test_size(filler, exp_res):
    for i in filler:
        tester.push(i)
    result = tester.size()
    assert result == exp_res
    for i in filler:
        tester.pop()

@pytest.mark.parametrize('tested_list, exp_res', FIXTURES_BALANCE)
def test_check_balance(tested_list, exp_res):
    result = tester.check_balance(tested_list)
    assert result == exp_res


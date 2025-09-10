from main import count_a_letter
import pytest

from main import count_a_letter
import pytest
# def test_demo_one():
#     num_1 = 8
#     num_2 = 9
#     result = num_1 + num_2
#     assert result == 17
# def test_demo_two():
#     num_1 = 18
#     num_2 = 24
#     result = num_1 + num_2
#     assert result == 42
# # Delete the demo tests and add your tests here
def test_test_1():
    sentence = "hello, world"
    letter = "e"
    result = count_a_letter(sentence, letter)
    assert result == 1
def test_test_2():
    sentence = "hello, world"
    letter = "a"
    result = count_a_letter(sentence, letter)
    assert result == 0
def test_test_3():
    sentence = "hello, world"
    letter = "1"
    result = count_a_letter(sentence, letter)
    assert result == None
def test_test_4():
    sentence = None
    letter = "z"
    result = count_a_letter(sentence, letter)
    assert result == None
def test_test_5():
    sentence = "hello, world"
    letter = ""
    result = count_a_letter(sentence, letter)
    assert result == None
# def test_test_6():
#     sentence = "hello, world"
#     letter = None
#     result = count_a_letter(sentence, letter)
#     assert result == None
# def test_test_7():
#     sentence = "hello, world"
#     letter = False
#     result = count_a_letter(sentence, letter)
#     assert result == False
def test_test_8():
    sentence = "hello, world"
    letter = "ll"
    result = count_a_letter(sentence, letter)
    assert result == 0
def test_test_9():
    sentence = "bAnAna"
    letter = "A"
    result = count_a_letter(sentence, letter)
    assert result == 2
def test_test_10():
    sentence = "mañana"
    letter = "ñ"
    result = count_a_letter(sentence, letter)
    assert result == 1
def test_test_11():
    sentence = "Hello!!"
    symbol = "!"
    result = count_a_letter(sentence, symbol)
    assert result == None










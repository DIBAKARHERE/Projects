"""
specific test cases from different files as a group we can run by mark
1. import pytest
2. write @pytest.mark.smoke before start of a function [it is best practice to write meaningful name(custom mark). In place of smoke like regression,login etc.]
(cmd) "py.test -m smoke -v -s"
3. write @pytest.mark.xfail in case of skip any test case for some reasons
"""

import pytest

@pytest.mark.xfail
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because condition strings do not match"

#pass
def test_secondProgram():
    a = 6
    b = 4
    assert a + 2 == 8, "Addition matched"


def test_matchTest():
    msg = "Hello"
    assert msg == "Hello", "Test passed because condition strings are matched"

@pytest.mark.smoke
def test_thirdProgram():
    print("This is third test program")


@pytest.mark.xfail
def test_fourthTest():
    msg = "Hello"
    assert msg == "Hi", "Test failed because condition strings are not matched"
"""
1. Before yield keyword pre-execution is done & after yield post teardown execution will be done. It is used for teardown
2. For multiple test cases we can wrap fixtures like "setup" here in marker '@pytest.mark.usefixtures' in a single class "TestExample" here
3. It will invoke all testcases using same fixture in one shot which saves time & clean readable code
4. Here first setup fixture is called by TestExample class,
In that response conftest setup fixture is called & run first,
then method test_fixtureDemo will run & lastly test case execution will take place after yield keyword.
This process will continue until finish of all testmethod (i.e. test_fixtureDemo,test_fixtureDemo1,test_fixtureDemo2 .......)
"""

import pytest
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will be executing fixtureDemo")

    def test_fixtureDemo1(self):
        print("I will be executing fixtureDemo1")

    def test_fixtureDemo2(self):
        print("I will be executing fixtureDemo2")

    def test_fixtureDemo3(self):
        print("I will be executing fixtureDemo3")
"""
1. When we return the data from conftest dataLoad we have to pass the parameter like 'dataLoad' fixture is added
in the 'test_fixtureDemo' method (here returns the list)
2. We can print specific data from the list by list indexing
"""

import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:
    def test_editProfile(self, dataLoad):
        print(dataLoad)
        print(dataLoad[2])
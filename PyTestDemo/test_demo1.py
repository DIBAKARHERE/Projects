"""
1. In pytest filename should start with "test_*" or end with "*_test" while creating
2. For pytest testing standard we have to write every line of code inside a function
3. In pytest function name stated as test methods & it should followed by "test_*" not "*_test"
4. For these functions we don't need to call manually. pytest automatically calls it by default
5. If same method name or function name is defined the latest one's result will replace the previous one
6. To run all files at a time in a particular directory: (cmd) "py.test"
7. -v flag used for "verbose" means more info
   -s flag used for that printed output to see in cmd rather than we see in pycharm terminal
   -k flag used followed by <keyword>
    flags can be writen in any order

In case of particular file run (steps)
a. copy the path where project files are present,
b. open cmd,
c. cd <file path>,
d. (cmd) "py.test test_demo2.py -v -s"

8. markers are stack together. If smoke, xfail stacks test will still run
but if stack skip test case will not run as its priority is higher

In case of particular files run from different files (steps)
(cmd) "py.test -k <keyword i.e. matchTest here> -v -s"
"""

import pytest

def test_firstProgram():
    print("Hello World")

# overwrites above function as function name or method name are same
@pytest.mark.smoke
def test_firstProgram():
    print("Bye World")

@pytest.mark.smoke
@pytest.mark.skip
def test_matchTest():
    msg = "Hi"
    assert msg == "Hi User", "Test passed"


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
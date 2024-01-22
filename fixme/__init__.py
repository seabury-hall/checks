import check50

@check50.check()
def exists():
    """fixme.py exists"""
    check50.exists("fixme.py")

@check50.check(exists)
def single_sentence():
    """Handles valid Inputs"""
    check50.run("python fixme.py").stdin("2").stdin("4").stdout("The sum of 2.0 and 4.0 is: 6.0").stdin("2").stdin("4").stdout("The concatenated string is: 24\n").exit(0)
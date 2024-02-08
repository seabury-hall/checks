import check50

@check50.check()
def exists():
    """match.py exists"""
    check50.exists("match.py")

@check50.check(exists)
def square():
    """Checks Square"""
    check50.run("python match.py").stdin("square").stdin("3").stdout("9").exit(0)

@check50.check(exists)
def rectangle():
    """Checks Rectangle"""
    check50.run("python match.py").stdin("rectangle").stdin("3").stdin("9").stdout("27").exit(0)

@check50.check(exists)
def circle():
    """Checks Circle"""
    check50.run("python match.py").stdin("circle").stdin("3").stdout("28.274333882308138").exit(0)

@check50.check(exists)
def triangle():
    """Checks Triangle"""
    check50.run("python match.py").stdin("triangle").stdin("4").stdin("7").stdout("14").exit(0)

@check50.check(exists)
def elifs():
    """Checks for if/elif/else"""
    fails = ["if", "elif", "else"]
    output = check50.run("cat match.py").stdout()

    for fail in fails:
        if fail in output:
            raise check50.Failure("Still using if, elif or else")


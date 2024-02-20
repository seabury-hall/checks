import check50
from re import match

@check50.check()
def exists():
    """age_group.py exists"""
    check50.exists("age_group.py")

@check50.check(exists)
def negative():
    """Checks Negative"""
    check50.run("python age_group.py").stdin("-1").stdout("Please enter a valid age").exit(0)

@check50.check(exists)
def Toddler():
    """Checks Toddler"""

    expected = "Toddler\n"
   
    lower_bound = check50.run("python age_group.py").stdin("0").stdout()
    upper_bound = check50.run("python age_group.py").stdin("2").stdout()

    if expected != lower_bound:
        raise check50.Mismatch("Toddler", lower_bound, help=None)
    if expected != lower_bound:
        raise check50.Mismatch("Toddler", upper_bound, help=None)

@check50.check(exists)
def Child():
    """Checks Child"""

    expected = "Child\n"
   
    lower_bound = check50.run("python age_group.py").stdin("3").stdout()
    upper_bound = check50.run("python age_group.py").stdin("12").stdout()

    if expected != lower_bound:
        raise check50.Mismatch("Child", lower_bound, help=None)
    if expected != lower_bound:
        raise check50.Mismatch("Child", upper_bound, help=None)
        
@check50.check(exists)
def Teenager():
    """Checks Teenager"""

    expected = "Teenager\n"
   
    lower_bound = check50.run("python age_group.py").stdin("13").stdout()
    upper_bound = check50.run("python age_group.py").stdin("19").stdout()

    if expected != lower_bound:
        raise check50.Mismatch("Teenager", lower_bound, help=None)
    if expected != lower_bound:
        raise check50.Mismatch("Teenager", upper_bound, help=None)

@check50.check(exists)
def Adult():
    """Checks Adult"""

    expected = "Adult\n"
   
    lower_bound = check50.run("python age_group.py").stdin("20").stdout()
    upper_bound = check50.run("python age_group.py").stdin("64").stdout()

    if expected != lower_bound:
        raise check50.Mismatch("Adult", lower_bound, help=None)
    if expected != lower_bound:
        raise check50.Mismatch("Adult", upper_bound, help=None)

@check50.check(exists)
def Senior():
    """Checks Senior"""

    expected = "Senior\n"
   
    lower_bound = check50.run("python age_group.py").stdin("65").stdout()
    upper_bound = check50.run("python age_group.py").stdin("895").stdout()

    if expected != lower_bound:
        raise check50.Mismatch("Senior", lower_bound, help=None)
    if expected != lower_bound:
        raise check50.Mismatch("Senior", upper_bound, help=None)
        
@check50.check(exists)
def Yoda():
    """Checks Yoda"""

    expected = "Yoda"
   
    actual = check50.run("python age_group.py").stdin('896').stdout()
        
    if not match(expected, actual):
        raise check50.Mismatch("Yoda", actual, help=None)
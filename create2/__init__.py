import check50

@check50.check()
def exists():
    """any .py file exists"""
    files = check50.include("*.py")
    if not files:
        raise check50.Failure("no .py file found")
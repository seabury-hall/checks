import check50

@check50.check()
def exists():
    """clickbait.py exists"""
    check50.exists("clickbait.py")

'''@check50.check(exists)
def millenials():
    """Gets millenials headline"""
    check50.run("python clickbait.py").stdout("(.*?)", regex=True).stdout("(.*?)", regex=True).stdout("^Are Millenials", regex=True).stdout("(.*?)", regex=True).stdout("(.*?)", regex=True).stdout("(.*?)", regex=True).stdout("(.*?)", regex=True).stdout("(.*?)", regex=True).stdout("(.*?)", regex=True).stdout("(.*?)", regex=True).exit(0)

@check50.check(exists)
def dontKnow():
    """Gets don't know headline"""
    check50.run(("python clickbait.py")
                .stdout("(.*?)", regex=True)
                .stdout("^Without This", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .exit(0))
    
@check50.check(exists)
def bigCompanies():
    """Gets don't know headline"""
    check50.run(("python clickbait.py")
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("^Big Companies", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .exit(0))

@check50.check(exists)
def wontBelieve():
    """Gets you won't believe"""
    check50.run(("python clickbait.py")
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("^You Won't Believe", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .exit(0))
    
@check50.check(exists)
def dontWantYouToKnow():
    """Gets DontWantYouToKnow"""
    check50.run(("python clickbait.py")
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("^What", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .exit(0))

@check50.check(exists)
def giftIdea():
    """Gets GiftIdea Headline"""
    check50.run(("python clickbait.py")
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("^([1-9]|1[0-6])", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .exit(0))
    
def generateJobAutomated():
    """Gets generateJobAutomated"""
    check50.run(("python clickbait.py")
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("^This", regex=True)
                .stdout("(.*?)", regex=True)
                .exit(0))

def generateDeadline():
    """Gets generateDeadline"""
    check50.run(("python clickbait.py")
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("(.*?)", regex=True)
                .stdout("^Post", regex=True)
                .exit(0))'''

from check50 import *

class greet(Checks):

    @check()
    def exists(self):
        self.require("greet.c")

    @check("exists")
    def compiles(self):
        self.spawn("clang -o greet greet.c -lcs50 -lm").exit(0)


from check50 import *

class greet(Checks):

    @check()
    def exists(self):
        self.require("population.c")

    @check("exists")
    def compiles(self):
        self.spawn("clang -o population population.c -lcs50 -lm").exit(0)

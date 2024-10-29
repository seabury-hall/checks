
from check50 import *

class uppercase(Checks):

    @check()
    def exists(self):
        self.require("uppercase.c")

    @check("exists")
    def compiles(self):
        self.spawn("clang -o uppercase uppercase.c -lcs50 -lm").exit(0)

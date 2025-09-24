
from check50 import *

class greet(Checks):

    @check()
    def exists(self):
        self.require("practice.c")

    @check("exists")
    def compiles(self):
        self.spawn("clang -o practice practice.c -lcs50 -lm").exit(0)

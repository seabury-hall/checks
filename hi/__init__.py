
from check50 import *

class hi(Checks):

    @check()
    def exists(self):
        self.require("hi.c")

    @check("exists")
    def compiles(self):
        self.spawn("clang -o hi hi.c -lcs50 -lm").exit(0)

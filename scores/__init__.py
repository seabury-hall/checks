
from check50 import *

class scores(Checks):

    @check()
    def exists(self):
        self.require("scores.c")

    @check("exists")
    def compiles(self):
        self.spawn("clang -o scores scores.c -lcs50 -lm").exit(0)

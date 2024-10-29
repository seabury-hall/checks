
from check50 import *

class length(Checks):

    @check()
    def exists(self):
        self.require("length.c")

    @check("exists")
    def compiles(self):
        self.spawn("clang -o length length.c -lcs50 -lm").exit(0)

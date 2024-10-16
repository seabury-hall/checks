from check50 import *

class Prime(Checks):

	@check()
	def exists(self):
		"""daily13.c exists"""
		self.require("daily13.c")

	@check("exists")
	def compiles(self):
		"""daily13.c compiles"""
		self.spawn("clang -o daily13 daily13.c -lcs50 -lm").exit(0)
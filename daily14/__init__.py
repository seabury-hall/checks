from check50 import *

class Prime(Checks):

	@check()
	def exists(self):
		"""daily14.c exists"""
		self.require("daily14.c")

	@check("exists")
	def compiles(self):
		"""daily14.c compiles"""
		self.spawn("clang -o daily14 daily14.c -lcs50 -lm").exit(0)
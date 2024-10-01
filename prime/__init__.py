from check50 import *

class Prime(Checks):

	@check()
	def exists(self):
		"""prime.c exists"""
		self.require("prime.c")

	@check("exists")
	def compiles(self):
		"""prime.c compiles"""
		self.spawn("clang -o prime prime.c -lcs50 -lm").exit(0)

	@check("Checks prime number")
	def test_prime(self):
		"""input of 3 yields true"""
		self.spawn("./prime").stdin("3").stdout("false").exit(0)
	
	@check("checks non-prime number")
	def test_non_prime(self):
		"""input 6"""
		self.spawn("./prime").stdin("6").stdout("true").exit(0)
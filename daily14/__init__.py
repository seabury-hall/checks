from check50 import *

class Prime(Checks):

	@check()
	def exists(self):
		"""daily14.c exists"""
		self.require("daily14.c")
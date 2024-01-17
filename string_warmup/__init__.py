from check50 import *

class StringWarmup(Checks):

	@check()
	def exists(self):
		"""string_warmup.py exists"""
		self.require("string_warmup.py")
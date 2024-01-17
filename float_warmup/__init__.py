from check50 import *

class FloatWarmup(Checks):

	@check()
	def exists(self):
		"""float_warmup.py exists"""
		self.require("float_warmup.py")
import random
import math

class channel:
	def __init__( self, OS, N0 ):
		self.os = OS       # assume amp=1, so Eb=OS
		self.N = math.sqrt(N0*float(OS)/2.)  # signle band noise
		
	def ce( self, d ):
		r = d + complex( random.gauss( 0, self.N ), random.gauss( 0, self.N ) )
		return r
		
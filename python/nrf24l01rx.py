import Fir

class nrf24l01rx:
	def __init__(self,OS):
		self.coef = [ 1. for i in range(OS) ]
		self.os = OS
		if OS == 32:
			self.coef = [
			    0.06920849042567,-0.005755261204001,-0.006340193309937,-0.007386667797412,
			  -0.008798585030667, -0.01047498735927, -0.01228530755291, -0.01409434460374,
			   -0.01576257058642, -0.01715171250053, -0.01812357862317, -0.01854832989228,
			   -0.01831247087924, -0.01732400123922, -0.01551460603023, -0.01284114701564,
			  -0.009295247613566,-0.004904206032322,0.0002653449848267, 0.006130312186421,
			     0.0125549049137,  0.01952896134114,   0.0265251174719,  0.03371140129423,
			    0.04077391740718,  0.04750330884495,  0.05369268263331,  0.05916678654691,
			    0.06376345911252,  0.06734280851279,  0.06979166963315,   0.0710346869702,
			     0.0710346869702,  0.06979166963315,  0.06734280851279,  0.06376345911252,
			    0.05916678654691,  0.05369268263331,  0.04750330884495,  0.04077391740718,
			    0.03371140129423,   0.0265251174719,  0.01952896134114,   0.0125549049137,
			   0.006130312186421,0.0002653449848267,-0.004904206032322,-0.009295247613566,
			   -0.01284114701564, -0.01551460603023, -0.01732400123922, -0.01831247087924,
			   -0.01854832989228, -0.01812357862317, -0.01715171250053, -0.01576257058642,
			   -0.01409434460374, -0.01228530755291, -0.01047498735927,-0.008798585030667,
			  -0.007386667797412,-0.006340193309937,-0.005755261204001,  0.06920849042567
			]
		self.filterIn = Fir.Fir( self.coef, len(self.coef) )
		self.filterFD = Fir.Fir( self.coef, len(self.coef) )
		self.last = complex(0.,0.)
		
	def ce( self, d ):
		
		filterOut = self.filterIn.ce( d )
		FD = filterOut * self.last.conjugate()
		r = self.filterFD.ce( FD.imag )
		self.last = filterOut
		
		return r
		
	
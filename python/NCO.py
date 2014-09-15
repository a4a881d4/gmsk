import math
class NCO:
	def __init__(self,W,Fc,Fs):
		self.OSCF = 1<<W
		self.Acc = int(Fc/Fs*self.OSCF+0.5)
		self.state = 0
		self.VCO = 0
		
	def ce(self,p):
		self.State = (self.State+self.Acc+self.VCO+p)%self.OSCF
		return self.State
		
	def phase(self):
		d = float(self.State)/float(self.OSCF)*2.*math.pi
		
	def iq(self):
		d = self.phase()
		return complex(math.cos(d),math.sin(d))
		
	
		

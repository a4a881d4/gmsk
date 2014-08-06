import constants

class OSC:
	def __init__(self,f,Fs):
		self.Acc = int(f/Fs*constants.OSCF+0.5)
		self.State = 0
	
	def ce(self):
		self.State = (self.State+self.Acc)%constants.OSCF
		return self.State
		
		
	

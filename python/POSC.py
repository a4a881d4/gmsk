import constants
import math

class POSC:
	def __init__(self,f,Fs):
		self.f = f
		self.Fs = Fs
		self.Acc = int(f/Fs*constants.HighOSCF+0.5)
		self.State = []
		self.AccHigh = (self.Acc*constants.OverSampleRate) % constants.HighOSCF
		s = 0
		for i in range(0,constants.OverSampleRate):
			self.State.append(s)
			s = (s + self.Acc) % constants.HighOSCF
		
	def ce( self,inS ):
		ret = []
		for i in range(0,constants.OverSampleRate):
			self.State[i] = ( self.State[i] + self.AccHigh ) % constants.HighOSCF
			"""
			if (( self.State[i] + inS ) % constants.HighOSCF) >= constants.HighOSCF/2:
				ret.append(-1)
			else:
				ret.append(1)
			"""
			p = ( self.State[i] + inS )/float(constants.HighOSCF)*2.*math.pi
			ret.append(math.sin(p))
		return ret
		
	def report(self):
		print "f=",self.f,"Fs=",self.Fs,"Acc=",self.Acc
		
if __name__ == '__main__':
	po = POSC(1.5e6*512,6144e6)
	po.report()
	for T in range(0,10):
		r = po.ce(1024)
		print r
		
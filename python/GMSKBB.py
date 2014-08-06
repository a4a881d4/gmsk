import constants
import Qfunc
import random

class GMSKBB:
	def __init__(self,f,Fs):
		self.Acc = int((f/Fs)*constants.GMSKOSCF+0.5)
		self.AS = 0
		self.Table = Qfunc.Fserial(constants.BT,constants.GMSKOSCF,constants.GMSKRange,constants.GMSKP)
		self.State = []
		for T in range(-constants.GMSKRange,constants.GMSKRange):
			self.State.append(0)
		self.over = 0
		self.HState = 0
	
	def newD(self):
		return self.over
	
	def report(self):
		print "#",self.over,len(self.State),self.HState,"|",self.State[0],self.State[1],self.State[2],self.State[3],"|",self.Table[0*constants.GMSKOSCF+self.AS],self.Table[1*constants.GMSKOSCF+self.AS],self.Table[2*constants.GMSKOSCF+self.AS],self.Table[3*constants.GMSKOSCF+self.AS],self.AS
					
	def ce( self,inS ):
		# self.report()
		if self.over==1:
			self.over=0
			last = self.State.pop(0)
			if last == -1:
				self.HState = (self.HState-1)&3
			elif last == 1:
				self.HState = (self.HState+1)&3 
			if inS==0:
				self.State.append(1)
			else:
				self.State.append(-1)
				
		ret = constants.GMSKP*self.HState
		for T in range(-constants.GMSKRange,constants.GMSKRange):
			t = T + constants.GMSKRange
			ret = ret + self.Table[t*constants.GMSKOSCF+self.AS]*self.State[constants.GMSKRange*2-1-t]
				
		self.AS = self.AS + self.Acc
		if self.AS>=constants.GMSKOSCF:
			self.over=1
		self.AS = self.AS%constants.GMSKOSCF		
		
		return ret%(4*constants.GMSKP)
		
if __name__ == '__main__':
	gmsk = GMSKBB(5.2e6,192e6)
	data = []
	for i in range(0,384):
		d = random.randint(0,1)
		data.append(d)
	
	while data:
		phase=0
		if gmsk.newD()==1:
			phase=gmsk.ce(data.pop())
		else:
			phase=gmsk.ce(0)
		print phase
		
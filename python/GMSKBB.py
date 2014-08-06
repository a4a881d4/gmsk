import constants
import Qfunc

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
				
	def ce( self,inS ):
		if self.over==1:
			self.over=0
			last = self.State.pop()
			if last == -1:
				self.HState = (self.HState-1)&3
			elif last == 1:
				self.HState = (self.HState+1)&3 
			if inS==0:
				self.State.append(1)
			else:
				self.State.append(-1)
		
		ret = constants.GMSKP*(self.HState+4)
		for T in range(-constants.GMSKRange,constants.GMSKRange):
			t = T + constants.GMSKRange
			ret = ret + self.Table[t*constants.GMSKOSCF+self.AS]*self.State[t]
				
		self.AS = self.AS + self.Acc
		if self.AS>=constants.GMSKOSCF:
			self.over=1
		self.AS = self.AS%constants.GMSKOSCF		
		
		return ret%(4*constants.GMSKP)
		
if __name__ == '__main__':
	gmsk = GMSKBB(5.2e6,192e6)
	data = [0,1,0,1,0,1,1,0,0,1,1,1,1,1]
	
	while data:
		phase=0
		if gmsk.newD()==1:
			phase=gmsk.ce(data.pop())
		else:
			phase=gmsk.ce(0)
		print phase
		
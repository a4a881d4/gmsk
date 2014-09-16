import channel
import Fir


class nrf24l01Channel:
	def __init__(self,N0):
		self.ChannelCoef = [
			0.04043988737137,  0.02305723651795,  0.02835846576427,  0.03333274714846,
    	0.03779347565539,  0.04140897746597,   0.0439442278272,  0.04524606440035,
    	0.04524606440035,   0.0439442278272,  0.04140897746597,  0.03779347565539,
    	0.03333274714846,  0.02835846576427,  0.02305723651795,  0.04043988737137
		]

		self.chanFilter = Fir.Fir(self.ChannelCoef,len(self.ChannelCoef))
		self.chan = channel.channel(32,N0)
		
	def ce(self,d):
		r = self.chan.ce(d)
		#print "r:",r,"d:",d
		r2 = self.chanFilter.ce(r)
		#print "r2:",r2
		return r2
		
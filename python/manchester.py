
class manchesterCoding:
	def __init__(self):
		self.state = 0
		self.counter = 0
		
	def coding(self,data):
		self.counter = self.counter+1
		tureTable = {
			# in-> data state
			# out-> state freq
			# 1-> -1, 0-> 1
			( 0, 0 ):( 1, 0),
			( 0, 1 ):( 0, 1),
			( 0, 2 ):( 1, 1),
			( 0, 3 ):( 0, 0),
			( 1, 0 ):( 3, 1),
			( 1, 1 ):( 2, 0),
			( 1, 2 ):( 3, 0),
			( 1, 3 ):( 2, 1) }
		(self.state,r) = tureTable[(data,self.state)]
		return r
		
	def decode(self,state0,ss):
		r = []
		state = state0
		for s in ss:
			if s==0:
				state = state+1
			else:
				state = state+3
			if state>3:
				state = state-4
			if state>1:
				r.append(1)
			else:
				r.append(0)
		return r
		
if __name__ == '__main__':
	import random
	mc = manchesterCoding()
	data = []
	freq = []
	for i in range(0,50):
		d = random.randint(0,1)
		data.append(d)
		f = mc.coding(d)
		freq.append(f)
	print data
	print freq
	dec = mc.decode(0,freq)
	print dec
	
	
	

			
			
		
			
	 
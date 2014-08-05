import math

def Qfuncx(t):
	a = 0.
	T = int(t*10000)
	for x in range(T,100*10000):
		v = x/10000.
		a = a + (1/math.sqrt(2.*math.pi))*math.exp(0-v*v/2.)
	return a/10000.

def Qfunc(t):
	return 0.5-0.5*math.erf(t/math.sqrt(2.))

def Ffunc(t,B):
	a = 2.*math.pi*B/math.sqrt(math.log(2.))
	return 0.5*(Qfunc((t-0.5)*a)-Qfunc((t+0.5)*a))

def Fserial(B):
	X=[]
	for t in range(-1024*2,1024*2):
		X.append(Ffunc(t/1024.,B))
	return X

if __name__ == '__main__':
	S = Fserial(0.25)
	print "#",len(S)
	sum = 0.
	for T in range(0,len(S)):
		sum = sum + S[T]
	all = sum
	sum = 0.
	for T in range(0,len(S)):
		sum = sum + S[T]
		print T,int(sum/all*65535+.5)
	print "#",sum
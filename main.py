import os,threding
def F():
	os.system("python main2.py")

def G():
	os.system("python main1.py")
	
S=threding.Thread(traget=F,args=())
D=threding.Thread(traget=G,args=())

S.start()
D.start()

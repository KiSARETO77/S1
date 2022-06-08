import os,threading
def F():
	os.system("python main2.py")

def G():
	os.system("python main1.py")
	
S=threading.Thread(traget=F,args=())
D=threading.Thread(traget=G,args=())

S.start()
D.start()

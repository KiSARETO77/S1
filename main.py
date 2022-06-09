import aminofix,json
from os import system as V
from colorama import Fore as X
from pyfiglet import Figlet as Z
from os import path
IG = X.GREEN
IB = X.BLUE
IR = X.RED
IBL=X.RESET
IM = X.MAGENTA
IY = X.YELLOW
IC = X.CYAN
IK = Z(font='slant')
V("clear")
print(IB)
print(IK.renderText("Views"))
print("\n\n\n")
LINK1 = "http://aminoapps.com/p/ftctiv"
print("\n\n\n")
file = path.dirname(path.abspath(__file__))
ACCOUNT = path.join(file,"accounts.json")
dictlist=[]
with open(ACCOUNT) as ACCOUNTS:
	dictlist = json.load(ACCOUNTS)
	def threadit(ACCOUNTS : dict):
		EMAIL = ACCOUNTS["email"]
		DEVICE = ACCOUNTS["device"]
		P = ACCOUNTS["password"]
		Ç=aminofix.Client(deviceId=DEVICE)
		try:
			Ç.login(EMAIL,P)
			LINK2=Ç.get_from_code(LINK1)
			COMID=LINK2.path[1:LINK2.path.index("/")]
			LINK3=LINK2.objectId
			Ç.join_community(COMID)
			SUB=aminofix.SubClient(comId=COMID,profile=Ç.profile)
			SUB.join_chat(LINK3)
			Ç.join_video_chat_as_viewer(comId=COMID,chatId=LINK3)
			Ç.join_video_chat_as_viewer(comId=COMID,chatId=LINK3)
			print(IY," - ",IG,"✓ ",IM,EMAIL)
		except Exception as F:
			print(IY," - ",IR,"✘",IM,EMAIL,IR,F)
			pass
for amp in dictlist:
	threadit(amp)

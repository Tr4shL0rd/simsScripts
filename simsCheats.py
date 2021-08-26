from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
enter = Key.enter

class simsComs:
	def simsCheats_Motherlode(self):
		moneyCheat = list("motherlode")
		return moneyCheat
	
	def simsCheats_moveObjects(self):
		moveObjectsCheat = list("bb.moveobjects")
		return moveObjectsCheat
	
	def simsCheats_ignoreReqs(self):
		ignoreReqsCheat = list("bb.ignoregameplayunlocksentitlement")
		return ignoreReqsCheat




def confirm(Debug=False):
	if Debug:
		keyboard.press(enter)
		keyboard.release(enter)
	else:
		pass
def openConsole(Debug=False):
	if Debug:
		keyboard.press(Key.ctrl)
		keyboard.press(Key.alt)
		keyboard.press('c')
		keyboard.release(Key.ctrl)
		keyboard.release(Key.alt)
		time.sleep(0.5)
		EnableCheats = list("testingcheats on")
		for lets in EnableCheats:
			keyboard.press(lets)
	else:
		pass
Cheats = simsComs()

def wait(secs=0.5):
	time.sleep(secs)


class sims4Cheats():
	
	def Money(self):
		wait()
		openConsole()
		for lets in Cheats.simsCheats_Motherlode():
			keyboard.press(lets)
		confirm()
	
	def MoveObject(self):
		wait()
		openConsole()
		for lets in Cheats.simsCheats_moveObjects():
			keyboard.press(lets)
		confirm()
	
	def IgnoreReqs(self):
		wait()
		openConsole()
		for lets in Cheats.simsCheats_ignoreReqs():
			keyboard.press(lets)
		confirm()

	def allCheats(self):
		wait()
		openConsole()
		for lets in Cheats.simsCheats_Motherlode():
			keyboard.press(lets)
		confirm()
		for lets in Cheats.simsCheats_moveObjects():
			keyboard.press(lets)
		confirm()
		for lets in Cheats.simsCheats_ignoreReqs():
			keyboard.press(lets)
		confirm()

	

Cheat = sims4Cheats()
Cheat.allCheats()

import threading
import hashlib
import time

from client_data import *

pollRate = 0.05

class FrameThread(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.setDaemon(True)

	def run(self):

		while True:
			time.sleep(pollRate)
			self.poll()

	def poll(self):

		CHECK_MAX = 20

		if len(ClientData.uiInformation.waitingFrames) > 0 and len(ClientData.uiInformation.waitingFrameInformation) > 0:
			queuedFrame = ClientData.uiInformation.waitingFrames[0]

			if queuedFrame.checked > CHECK_MAX:
				ClientData.uiInformation.waitingFrames.pop(0)
			else:
				for i in ClientData.uiInformation.waitingFrameInformation:
					if (i.frameHash == queuedFrame.frameHash):
						waitingFrame = ClientData.uiInformation.waitingFrames.pop(0)
						ClientData.uiInformation.waitingFrameInformation.remove(i)
						print("found matching info")
						ClientData.rawFrames.append(RawFrameData(waitingFrame.image, i.location, i.rotation))
						return
				queuedFrame.checked += 1


		if len(ClientData.uiInformation.waitingFrames) > 0 and len(ClientData.uiInformation.waitingFrameInformation) > 0:
			queuedInformation = ClientData.uiInformation.waitingFrameInformation[0]

			if queuedInformation.checked > CHECK_MAX:
				ClientData.uiInformation.waitingFrameInformation.pop(0)
			else:
				for i in ClientData.uiInformation.waitingFrames:
					if i.frameHash == queuedInformation.frameHash:
						waitingFrameInformation = ClientData.uiInformation.waitingFrameInformation.pop(0)
						ClientData.uiInformation.waitingFrames.remove(i)
						print("found matching frame")
						ClientData.rawFrames.append(RawFrameData(i.image, waitingFrameInformation.location, waitingFrameInformation.rotation))
						return
				queuedInformation.checked += 1

	def mainThreadUpdate(self):
		pass


if __name__ == "__main__":

	u = FrameThread()
	u.start()
	time.sleep(100)
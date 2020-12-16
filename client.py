import time

from mapper_thread import *
from depth_thread import *
from ui_thread import *
from frame_thread import *
from recieve_thread import *
# from send_thread import *

from client_data import *

class Client:

	def __init__(self):
		self.threads = []

		self.mapperThread = MapperThread()
		self.threads.append(self.mapperThread)
		self.depthThread = DepthThread()
		self.threads.append(self.depthThread)
		self.uithread = UIThread()
		self.threads.append(self.uithread)
		self.recieveThread = RecieveThread()
		self.threads.append(self.recieveThread)
		self.frameThread = FrameThread()
		self.threads.append(self.frameThread)
		# self.sendThread = SendThread()

		self.setUpData()
		self.startThreads()

	def setUpData(self):
		ClientData.SetUpData()

	def startThreads(self):
		for i in self.threads:
			i.start()

		# k = 0

		while True:
			# k+=1
			time.sleep(0.1)
			for i in self.threads:
				i.mainThreadUpdate()
				# if k == 10:
				# 	ClientData.uiInformation.depthLoaded = True

	def showModel(self):
		self.mapperThread.showModel()

	def exportModel(self):
		self.mapperThread.exportModel()

	def exit(self):
		quit()

c = Client()
# c.showModel()
# c.exportModel()

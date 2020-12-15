import time

from mapper_thread import *
from depth_thread import *
from ui_thread import *

from client_data import *

class Client:

	def __init__(self):
		self.mapperThread = MapperThread()
		self.depthThread = DepthThread()
		self.uithread = UIThread()
		self.mapperThread.setDaemon(True)
		self.depthThread.setDaemon(True)
		self.uithread.setDaemon(True)
		self.setUpData()
		self.startThreads()

	def setUpData(self):
		ClientData.SetUpData()

	def startThreads(self):
		self.uithread.start()
		self.mapperThread.start()
		self.depthThread.start()

		while True:
			time.sleep(0.1)
			if (ClientData.uiInformation.depthLoaded):
				self.uithread.setupWindow()

	def showModel(self):
		self.mapperThread.showModel()

	def exportModel(self):
		self.mapperThread.exportModel()

	def exit(self):
		quit()

import os

c = Client()
time.sleep(30)
# c.showModel()
# c.exportModel()

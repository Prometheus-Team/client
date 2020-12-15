import time

from mapper_thread import *
from depth_thread import *
from ui_thread import *

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

		self.setUpData()
		self.startThreads()

	def setUpData(self):
		ClientData.SetUpData()

	def startThreads(self):
		for i in self.threads:
			i.start()

		while True:
			time.sleep(0.1)
			for i in self.threads:
				i.mainThreadUpdate()

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

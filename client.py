import time

from mapper_thread import *
from depth_thread import *

from client_data import *

class Client:

	def __init__(self):
		#self.mapperThread = MapperThread()
		self.depthThread = DepthThread()
		self.setUpData()
		self.startThreads()

	def setUpData(self):
		ClientData.SetUpData()

	def startThreads(self):
		#self.mapperThread.start()
		self.depthThread.start()

	def showModel(self):
		self.mapperThread.showModel()

	def exportModel(self):
		self.mapperThread.exportModel()

c = Client()
time.sleep(5)
#c.showModel()
#c.exportModel()

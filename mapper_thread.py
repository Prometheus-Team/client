import threading

from mapping.image_projection.aggregate import *
from client_data import *

pollRate = 0.05

class MapperThread(threading.Thread):

	showModelTrigger = False
	exportModelTrigger = False

	def __init__(self):
		threading.Thread.__init__(self)
		self.aggregate = Aggregate()
    
	def run(self):
		print('started mapper thread')
		while True:
			time.sleep(pollRate)
			self.poll()

	def poll(self):
		self.checkFrames()
		self.checkShowModel()
		self.checkExportModel()

	def checkExportModel(self):
		if MapperThread.exportModelTrigger:
			MapperThread.exportModelTrigger = False
			OBJExporter.exportModel(self.aggregate.projection.getModel(), ClientData.modelValues.exportPath)


	def checkShowModel(self):
		if MapperThread.showModelTrigger:
			MapperThread.showModelTrigger = False
			m = ModelPreview()	
			m.addRenderable(self.aggregate.projection.getModelRenderable())

			for i in self.aggregate.frames:
				m.addCamera(i.getCamera())

			m.addRenderables(self.aggregate.projection.cloudSet.getCloudRenderables())
			time.sleep(1)
			m.start()


	def checkFrames(self):
		if len(ClientData.depthFrames) > 0:
			newFrame = ClientData.depthFrames.pop()
			self.processFrame(newFrame)

	def getFrame(self, depthFrame):
		frame = Frame(depthFrame.rawFrameData.image, depthFrame.depth, matrixTR(depthFrame.rawFrameData.cameraPosition, (0, depthFrame.rawFrameData.cameraRotation, 0)))
		return frame

	def processFrame(self, depthFrame):
		frame = self.getFrame(depthFrame)
		self.aggregate.addFrame(frame)

	def showModel(self):
		print('Set showModelTrigger true')
		MapperThread.showModelTrigger = True

	def exportModel(self):
		MapperThread.exportModelTrigger = True


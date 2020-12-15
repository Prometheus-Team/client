import threading
import time
import cv2 as cv

from client_data import *

pollRate = 0.1

class DepthThread(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.setDaemon(True)

	def init_thread(self):
		from dense_depth.depth_extractor import DepthExtractor
		ClientData.uiInformation.loadingText = "Loading model"
		self.depthExtractor = DepthExtractor(ClientData.projectorValues.depthModelPath)
		ClientData.uiInformation.loadingText = "Initializing tensorflow"
		self.setUpEvaluator()

	def setUpEvaluator(self):
		ClientData.uiInformation.loadingText = "Running depth map"
		image = cv.imread('mapping/testdata/default.png')
		res = self.depthExtractor.getDepthMap(image)
		print("Loaded Depth")
		ClientData.uiInformation.loadingText = "Loading completed"
		ClientData.uiInformation.depthLoaded = True


	def mainThreadUpdate(self):
		pass

	def run(self):
		self.init_thread()
		while True:
			time.sleep(pollRate)
			self.poll()

	def poll(self):
		self.checkReducedFrames()

	def checkReducedFrames(self):
		if len(ClientData.reducedFrames) > 0:
			reducedFrame = ClientData.reducedFrames.pop()
			self.processDepth(reducedFrame)

	def processDepth(self, reducedFrame):
		t0 = time.time()
		image = reducedFrame.image.astype(np.float32)/255
		res = self.depthExtractor.getDepthMap(image)
		print("Time used: ",time.time() - t0)
		depth = (((res * 1666.7) - 66.7) / 100)
		self.addFrameData(reducedFrame, depth)

	def addFrameData(self, reducedFrame, depth):
		depthFrame = DepthFrameData()
		depthFrame.depth = depth
		depthFrame.rawFrameData = reducedFrame
		ClientData.depthFrames.append(depthFrame)



if __name__ == '__main__':

	d = DepthThread()
	d.init_thread()
	d.poll()
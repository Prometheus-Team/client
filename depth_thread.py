import threading
import time

from dense_depth.depth_extractor import DepthExtractor
from client_data import *

pollRate = 0.1

class DepthThread(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.depthExtractor = DepthExtractor(ClientData.projectorValues.depthModelPath)

	def run(self):
		while True:
			time.sleep(pollRate)
			self.poll()

	def poll(self):
		self.checkReducedFrames()

	def checkReducedFrames(self):
		if len(ClientData.reducedFrames) > 0:
			reducedFrame = ClientData.reducedFrames.pop()
			self.processDepth(reducedFrame)

	def processDepth(self, image):
		t0 = time.time()
		res = self.depthExtractor.getDepthMap(image)
		print("Time used: ",time.time() - t0)
		depth = ((res * 1666.7) - 66.7) / 100
		ClientData.depthFrames.append(depth)

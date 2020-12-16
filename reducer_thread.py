from frame_reduction import reducer_class
from client_data import *
import threading
import time
import sys
sys.path.append('../Frame-Reduction-Module')

pollRate = 0.1


class RecieveThread(threading.Thread):

    def __init__(self,):
        threading.Thread.__init__(self)
        self.setDaemon(True)
		self.imagesforProcessing = []

    def mainThreadUpdate(self):
        pass

    def run(self):
        print('started mapper thread')
        while True:
            time.sleep(pollRate)
            self.poll()

    def poll(self):
        if len(ClientData.rawFrames) > 10:
			for i in range(10):
				self.imagesforProcessing.append(ClientData.rawFrames.image)
			reducerClass = reducer_class.Reducer(self.imagesforProcessing, 5, 500)
            images = reducerClass.get_images()
			for eachImage in images:
				index = eachImage[1]
				ClientData.reducedFrames.append(RawFrameData(eachImage[0],ClientData.rawFrames[index].location, ClientData.rawFrames[index].rotation))

            del ClientData.rawFrames[:10]
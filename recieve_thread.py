import threading
import pickle
import socket
import time

from client_data import *

pollRate = 0.05
recievePort = 9998

class RecieveThread(threading.Thread):

	def __init__(self,):
		threading.Thread.__init__(self)
		self.setDaemon(True)
		self.fetchedInformation = {}

	def mainThreadUpdate(self):
		pass

	def run(self):
		while True:
			time.sleep(pollRate)
			self.poll()

	def poll(self):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			# s.bind(('', 9998))
			# s.listen()
			# conn, addr = s.accept()
			while True:
				try:
					s.connect(('192.168.0.134', recievePort))
					while True:
						data = s.recv(4096)
						print("D", data)
						if data == b'':
							break
						fetchedInformation = pickle.loads(data)
						self.assignValues(fetchedInformation)
				except:
					print("Cannot find info host")

	def assignValues(self, fetchedData):
		ClientData.uiInformation.distance = fetchedData["frontDistance"]
		ClientData.uiInformation.avg_speed = fetchedData["speed"]
		ClientData.uiInformation.ultrasonic = fetchedData["batteryLevel"]

		frameInformation = FrameInformation()

		frameInformation.location = fetchedData["location"]
		frameInformation.rotation = fetchedData["heading"]
		frameInformation.frameHash = fetchedData["imageSha"]

		ClientData.uiInformation.waitingFrameInformation.append(frameInformation)

		print(ClientData.uiInformation.motion, ClientData.uiInformation.distance)
		print(len(ClientData.uiInformation.waitingFrameInformation))
		print(frameInformation.frameHash)



if __name__ == "__main__":

	u = RecieveThread()
	u.start()

	while True:
		time.sleep(0.1)
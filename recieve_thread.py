import threading
import pickle
import socket
import time

from client_data import *

pollRate = 0.05


class RecieveThread(threading.Thread):

	def __init__(self,):
		threading.Thread.__init__(self)
		self.setDaemon(True)
		self.fetchedInformation = {}

	def mainThreadUpdate(self):
		pass

	def run(self):
		print('started mapper thread')
		while True:
			time.sleep(pollRate)
			self.poll()

	def poll(self):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind((ConnectionValues.ip, ConnectionValues.port2))
			while True:
				s.listen()
				conn, addr = s.accept()
				print('Connected by', addr)
				data = conn.recv(4096)
				if not data:
					pass
				fetchedInformation = pickle.loads(data)
				self.assignValues(fetchedInformation)

	def assignValues(self, fetchedData):
		UIInformation.motion = fetchedData["motion"]
		UIInformation.distance = fetchedData["distance"]
		UIInformation.avg_speed=fetchedData["avg_speed"]
		UIInformation.ultrasonic=fetchedData["ultrasonic"]
		UIInformation.location=fetchedData["location"]
		UIInformation.rotation=fetchedData["rotation"]

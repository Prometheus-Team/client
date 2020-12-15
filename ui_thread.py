import sys
import threading
import time

from client_data import *
from ui.final_ui import *
from ui.loader import *

class UIThread(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.loadComplete = False
		self.setDaemon(True)

	def setUpUI(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.Form = QtWidgets.QWidget()
		self.ui = Ui_Form()
		self.ui.setupUi(self.Form)

	def setUpLinks(self):
		self.links = {
			self.ui.INP_ip : ClientData.connectionValues.ip,
			self.ui.INP_port : ClientData.connectionValues.port,
			self.ui.INP_front_length : ClientData.navigationValues.frontLength,
			self.ui.INP_back_length : ClientData.navigationValues.backLength,
			self.ui.INP_left_length : ClientData.navigationValues.leftLength,
			self.ui.INP_right_length : ClientData.navigationValues.rightLength,
			self.ui.INP_model : ClientData.modelValues.modelThreshold,
			self.ui.INP_bubble : ClientData.cloudValues.fieldResolution,
			self.ui.INP_block : ClientData.cloudValues.cloudSetResolution,
			self.ui.INP_point : ClientData.cloudValues.pointScale,
			self.ui.INP_cloud : ClientData.cloudValues.cloudScale,
			self.ui.INP_slant : ClientData.projectorValues.slantSeparation
		}

	def mainThreadUpdate(self):
		if ClientData.uiInformation.depthLoaded:
			self.setupWindow()

	def updateLinkedValue(self, lineWidget):
		self.links[lineWidget].value = lineWidget.text()

	def run(self):
		self.showSplash()
		while True:
			time.sleep(0.1)
			if ClientData.uiInformation.depthLoaded and not self.loadComplete:
				self.loader.kill()

	def showSplash(self):
		self.loader = Loader("resources\\splash.png")

	def setupWindow(self):
		self.setUpUI()
		self.openWindow()
		self.setUpLinks()
		self.setValues()

		sys.exit(self.app.exec_())

	def openWindow(self):
		self.Form.show()
		# Threading added for the a socket server to recieve the information from the vehicle
		# DataUiThread = threading.Thread(
		# 	target=recieveInformationDataSocket, 
		# 	args=(DataUiIP, DataUiPort,), 
		# 	daemon=True)
		# DataUiThread.start()
		# end

	def setValues(self):
		for i in self.links:
			i.setText(str(self.links[i].value))
			i.textChanged.connect(lambda x, y = i: self.updateLinkedValue(y))


if __name__ == "__main__":

	u = UIThread()
	u.start()
	time.sleep(2)
	ClientData.uiInformation.depthLoaded = True
	u.mainThreadUpdate()

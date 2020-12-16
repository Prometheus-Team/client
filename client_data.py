import numpy as np
import cv2 as cv
from PIL import Image
import hashlib

class Value:

	def __init__(self, value):
		self.value = value

class RawFrameData:

	def __init__(self, image = None, location = None, rotation = None):

		if type(image) == str:
			self.image = cv.imread(image)
		else:
			self.image = image
			
		self.cameraPosition = location
		self.cameraRotation = rotation
		self.time = 0

class DepthFrameData:

	def __init__(self):
		self.rawFrameData = RawFrameData()
		self.depth = None

class ConnectionValues:

	ip = Value('127.0.0.1')
	port = Value(33456)
	port2 = Value(33457)
	port3 = Value(33458)

class NavigationValues:

	frontLength = Value(10)
	backLength = Value(10)
	rightLength = Value(10)
	leftLength = Value(10)

class ModelValues:

	modelThreshold = Value(1)
	exportPath = "Model.obj"


class CloudValues:

	fieldResolution = Value(7)
	edgeFieldResolution = 5
	cloudSetResolution = Value(100)
	cloudScale = Value(3)
	pointScale = Value(6)
	cloudVolumeColor = (0.5,1,0.8)
	cloudBoundsColor = (1,0.4,1)
	cloudEdgeColor = (0.9,0.8,0.4)

class ProjectorValues:

	depthModelPath = "dense_depth\\nyu.h5"
	slantSeparation = Value(4)
	projectionResolution = (96, 54)

#Raspberry pi camera
	#hfov = 62.2
	#vfov = 48.8

#Samsung A51s
	hfov = 71.5
	vfov = 53.6

#Test images
	#hfov = 57
	#vfov = 43

	# hfov = 50
	# vfov = 40




class CloudInformation:

	occupation = 23#%
	blocks = 3
	blockSize = (0.7, 0.7)#m
	mappedVolume = (0.3, 0.5, 0.1)#m


class ModelInformation:

	vertices = 234957
	edges = 18235
	faces = 8240

class VehicleInformation:

	location = (0.23, 0.41, -0.11)#X: Y: Z: m
	rotation = 23#degrees
	coveredDistance = 34#m
	averageSpeed = 22#m/s
	locationBitmap = np.ones((500,500))

class UIInformation:

	depthLoaded = False
	loadingText = "Initializing"
	viewType = 0

	waitingFrames = []
	waitingFrameInformation = []
	motion = 0
	distance = 0
	avg_speed = 0
	ultrasonic = 0

class FrameInformation:

	def __init__(self, frameHash = '', location = (0,0), rotation = 0):
		self.frameHash = frameHash
		self.location = location
		self.rotation = rotation
		self.checked = 0

class WaitingFrame:

	def __init__(self, image = None, frameHash = ''):
		self.image = image
		self.frameHash = frameHash
		self.checked = 0




class Triggers: 
	showModelTrigger = False
	exportModelTrigger = False









class ClientData:

	rawFrames = []#type: RawFrameData
	reducedFrames = []#type: RawFrameData
	depthFrames = []#type: DepthFrameData

	connectionValues = ConnectionValues
	navigationValues = NavigationValues
	modelValues = ModelValues
	cloudValues = CloudValues
	projectorValues = ProjectorValues

	cloudInformation = CloudInformation
	modelInformation = ModelInformation
	vehicleInformation = VehicleInformation
	uiInformation = UIInformation

	triggers = Triggers

	def SetUpData():
		CloudSetValues = ClientData.cloudValues
		ModelValues = ClientData.modelValues

		ClientData.vehicleInformation.locationBitmap[100:400, 100:400] = 0
		ClientData.vehicleInformation.locationBitmap[150:200, 0:200] = 1
		ClientData.vehicleInformation.locationBitmap[240:260, 240:260] = 2




###
# f1 = DepthFrameData()

# f1.depth = genfromtxt('mapping/testdata/depth3.csv', delimiter=',') * 10
# f1.rawFrameData.image = cv.imread('mapping/testdata/ClippedDepthNormal.png')
# f1.rawFrameData.cameraPosition = (-1,1,-1)
# f1.rawFrameData.cameraRotation = 20

# f2 = DepthFrameData()

# f2.depth = genfromtxt('mapping/testdata/depth3.csv', delimiter=',') * 10
# f2.rawFrameData.image = cv.imread('mapping/testdata/ClippedDepthNormal.png')
# f2.rawFrameData.cameraPosition = (-1,1,-1)
# f2.rawFrameData.cameraRotation = -40

# f1 = DepthFrameData()

# f1.depth = np.load('mapping/testdata/i1.npy')/1.5# * 10
# f1.rawFrameData.image = cv.imread('mapping/testdata/i1.jpg')
# f1.rawFrameData.cameraPosition = (0,0,0)
# f1.rawFrameData.cameraRotation = 0

# f2 = DepthFrameData()

# f2.depth = np.load('mapping/testdata/i2.npy')/1.5# * 10
# f2.rawFrameData.image = cv.imread('mapping/testdata/i2.jpg')
# f2.rawFrameData.cameraPosition = (0,0,1)
# f2.rawFrameData.cameraRotation = 0

# f3 = DepthFrameData()

# f3.depth = np.load('mapping/testdata/i3.npy')/1.5# * 10
# f3.rawFrameData.image = cv.imread('mapping/testdata/i3.jpg')
# f3.rawFrameData.cameraPosition = (0,0,0)
# f3.rawFrameData.cameraRotation = 45

# f4 = DepthFrameData()

# f4.depth = np.load('mapping/testdata/i4.npy')/1.5# * 10
# f4.rawFrameData.image = cv.imread('mapping/testdata/i4.jpg')
# f4.rawFrameData.cameraPosition = (0,0,2)
# f4.rawFrameData.cameraRotation = 45


# f1 = RawFrameData()

# f1.image = cv.imread('mapping/testdata/default.png')
# f1.cameraPosition = (0,0,0)
# f1.cameraRotation = 0

image = cv.imread('mapping/testdata/default.png')
ClientData.uiInformation.waitingFrames.append(WaitingFrame(image, hashlib.sha1(image).hexdigest()))
image = cv.imread('mapping/testdata/i2.jpg')
ClientData.uiInformation.waitingFrames.append(WaitingFrame(image, hashlib.sha1(image).hexdigest()))
image = cv.imread('mapping/testdata/i3.jpg')
ClientData.uiInformation.waitingFrames.append(WaitingFrame(image, hashlib.sha1(image).hexdigest()))
image = cv.imread('mapping/testdata/i4.jpg')
ClientData.uiInformation.waitingFrames.append(WaitingFrame(image, hashlib.sha1(image).hexdigest()))


image = cv.imread('mapping/testdata/1_image.png')
ClientData.uiInformation.waitingFrameInformation.append(FrameInformation(hashlib.sha1(image).hexdigest(), (1,1), 3))
image = cv.imread('mapping/testdata/i2.jpg')
ClientData.uiInformation.waitingFrameInformation.append(FrameInformation(hashlib.sha1(image).hexdigest(), (1,6), 0))
image = cv.imread('mapping/testdata/i3.jpg')
ClientData.uiInformation.waitingFrameInformation.append(FrameInformation(hashlib.sha1(image).hexdigest(), (3,8), -3))
image = cv.imread('mapping/testdata/i4.jpg')
ClientData.uiInformation.waitingFrameInformation.append(FrameInformation(hashlib.sha1(image).hexdigest(), (-4,0), 6))


# ClientData.reducedFrames.append(RawFrameData('mapping/testdata/default.png', (0,0,0), 0))


# ClientData.reducedFrames.append(RawFrameData('mapping/testdata/i1.jpg', (0,0,0), 0))
# ClientData.reducedFrames.append(RawFrameData('mapping/testdata/i2.jpg', (0,0,1), 0))
# ClientData.reducedFrames.append(RawFrameData('mapping/testdata/i3.jpg', (0,0,0), 45))
# ClientData.reducedFrames.append(RawFrameData('mapping/testdata/i4.jpg', (0,0,4), 45))

ClientData.reducedFrames.append(RawFrameData('../samples/1_1.jpg', (0,0,0), 0))
# ClientData.reducedFrames.append(RawFrameData('../samples/1_2.jpg', (0,0,0), 45))
# ClientData.reducedFrames.append(RawFrameData('../samples/1_3.jpg', (0,0,0), 90))
# ClientData.reducedFrames.append(RawFrameData('../samples/2_1.jpg', (0,0,1), -45))
# ClientData.reducedFrames.append(RawFrameData('../samples/2_2.jpg', (0,0,1), 0))
# ClientData.reducedFrames.append(RawFrameData('../samples/2_3.jpg', (0,0,1), 45))
# ClientData.reducedFrames.append(RawFrameData('../samples/2_4.jpg', (0,0,1), 90))
# ClientData.reducedFrames.append(RawFrameData('../samples/3_1.jpg', (0,0,2), -45))
# ClientData.reducedFrames.append(RawFrameData('../samples/3_2.jpg', (0,0,2), 0))
# ClientData.reducedFrames.append(RawFrameData('../samples/3_3.jpg', (0,0,2), 45))
# ClientData.reducedFrames.append(RawFrameData('../samples/3_4.jpg', (0,0,2), 90))
# ClientData.reducedFrames.append(RawFrameData('../samples/4_1.jpg', (1,0,2), -45))
# ClientData.reducedFrames.append(RawFrameData('../samples/4_2.jpg', (1,0,2), 0))
# ClientData.reducedFrames.append(RawFrameData('../samples/4_3.jpg', (1,0,2), 45))
# ClientData.reducedFrames.append(RawFrameData('../samples/4_4.jpg', (1,0,2), 90))
# ClientData.reducedFrames.append(RawFrameData('../samples/4_5.jpg', (1,0,2), 135))
# ClientData.reducedFrames.append(RawFrameData('../samples/4_6.jpg', (1,0,2), 180))
# ClientData.reducedFrames.append(RawFrameData('../samples/5_1.jpg', (1,0,1), -45))
# ClientData.reducedFrames.append(RawFrameData('../samples/5_2.jpg', (1,0,1), 0))
# ClientData.reducedFrames.append(RawFrameData('../samples/5_3.jpg', (1,0,1), 45))
# ClientData.reducedFrames.append(RawFrameData('../samples/5_4.jpg', (1,0,1), 90))
# ClientData.reducedFrames.append(RawFrameData('../samples/5_5.jpg', (1,0,1), 135))
# ClientData.reducedFrames.append(RawFrameData('../samples/5_6.jpg', (1,0,1), 180))
# ClientData.reducedFrames.append(RawFrameData('../samples/6_1.jpg', (1,0,0), 0))
# ClientData.reducedFrames.append(RawFrameData('../samples/6_2.jpg', (1,0,0), 45))
# ClientData.reducedFrames.append(RawFrameData('../samples/6_3.jpg', (1,0,0), 90))
# ClientData.reducedFrames.append(RawFrameData('../samples/6_4.jpg', (1,0,0), 135))




# cvi = cv.imread('mapping/testdata/default.png'5
# pili = np.clip(np.asarray(Image.open('mapping/testdata/default.png'), dtype=float) / 255, 0, 1)

# print(cvi)
# print(pili)

# ClientData.reducedFrames.extend([f1 for i in range(1)])
# ClientData.depthFrames.extend([f1, f2])

# ClientData.SetUpData()

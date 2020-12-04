import numpy as np
import cv2 as cv

class RawFrameData:

	def __init__(self):
		self.image = None
		self.cameraPosition = None
		self.cameraRotation = 0
		self.time = 0


class DepthFrameData:

	def __init__(self):
		self.rawFrameData = RawFrameData()
		self.depth = None


class ModelValues:

	modelThreshold = 1
	exportPath = "Model.obj"


class CloudValues:

	fieldResolution = 7
	edgeFieldResolution = 5
	cloudSetResolution = 100
	cloudScale = 3
	pointScale = 6
	cloudVolumeColor = (0.5,1,0.8)
	cloudBoundsColor = (1,0.4,1)
	cloudEdgeColor = (0.9,0.8,0.4)

class ProjectorValues:

	slantSeparation = 4
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





class ClientData:

	rawFrames = []#type: RawFrameData
	reducedFrames = []#type: RawFrameData
	depthFrames = []#type: DepthFrameData

	modelValues = ModelValues
	cloudValues = CloudValues
	projectorValues = ProjectorValues

	cloudInformation = CloudInformation
	modelInformation = ModelInformation
	vehicleInformation = VehicleInformation

	def SetUpData():
		CloudSetValues = ClientData.cloudValues
		ModelValues = ClientData.modelValues


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

f1 = DepthFrameData()

f1.depth = np.load('mapping/testdata/i1.npy')/1.5# * 10
f1.rawFrameData.image = cv.imread('mapping/testdata/i1.jpg')
f1.rawFrameData.cameraPosition = (0,0,0)
f1.rawFrameData.cameraRotation = 0

f2 = DepthFrameData()

f2.depth = np.load('mapping/testdata/i2.npy')/1.5# * 10
f2.rawFrameData.image = cv.imread('mapping/testdata/i2.jpg')
f2.rawFrameData.cameraPosition = (0,0,1)
f2.rawFrameData.cameraRotation = 0

f3 = DepthFrameData()

f3.depth = np.load('mapping/testdata/i3.npy')/1.5# * 10
f3.rawFrameData.image = cv.imread('mapping/testdata/i3.jpg')
f3.rawFrameData.cameraPosition = (0,0,0)
f3.rawFrameData.cameraRotation = 45

f4 = DepthFrameData()

f4.depth = np.load('mapping/testdata/i4.npy')/1.5# * 10
f4.rawFrameData.image = cv.imread('mapping/testdata/i4.jpg')
f4.rawFrameData.cameraPosition = (0,0,2)
f4.rawFrameData.cameraRotation = 45

ClientData.depthFrames.extend([f1, f2, f3, f4])
# ClientData.depthFrames.extend([f1, f2])

from numpy import genfromtxt
import cv2 as cv

from mapping.image_projection.cloudset import *

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

	modelThreshold = 0.1
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


class VehicleValues:

	hfov = 57
	vfov = 43




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






class ClientData:

	rawFrames = []
	reducedFrames = []
	depthFrames = []

	modelValues = ModelValues
	cloudValues = CloudValues
	projectorValues = ProjectorValues
	vehicleValues = VehicleValues

	cloudInformation = CloudInformation
	modelInformation = ModelInformation
	vehicleInformation = VehicleInformation


	def SetUpData():
		CloudSetValues = ClientData.cloudValues


###
f1 = DepthFrameData()

f1.depth = genfromtxt('mapping/testdata/depth3.csv', delimiter=',') * 10
f1.rawFrameData.image = cv.imread('mapping/testdata/ClippedDepthNormal.png')
f1.rawFrameData.cameraPosition = (-1,1,-1)
f1.rawFrameData.cameraRotation = 20

f2 = DepthFrameData()

f2.depth = genfromtxt('mapping/testdata/depth3.csv', delimiter=',') * 10
f2.rawFrameData.image = cv.imread('mapping/testdata/ClippedDepthNormal.png')
f2.rawFrameData.cameraPosition = (-1,1,-1)
f2.rawFrameData.cameraRotation = -40

ClientData.depthFrames.extend([f1, f2])

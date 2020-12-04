import sys
import os

from mapper_thread import *

mainDirectory = os.getcwd()

sys.path.append(mainDirectory + r'\mapping\image_projection')
sys.path.append(mainDirectory + r'\mapping\ui')

os.chdir(mainDirectory + r'\mapping\image_projection')

from aggregate import * 
from ui import *

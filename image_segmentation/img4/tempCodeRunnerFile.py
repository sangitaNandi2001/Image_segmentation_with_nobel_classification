# SEGMENTATION
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math
im = cv2.imread(r'D:\\PROJECT\\image\\moutain.jpg')
height, width, channel = im.shape

# seed points
sky_seed=(im[56,205])
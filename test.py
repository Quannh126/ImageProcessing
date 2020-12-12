import sys
import numpy as np
import skimage.color
import skimage.io
import skimage.viewer
from matplotlib import pyplot as plt
import cv2 as cv
from PIL import Image, ImageEnhance

img = Image.open('img4.png')
pixels = img.load()

img1 = cv.imread('img4.png')

plt.figure()
plt.subplot(121), plt.imshow(img1)
plt.title('CV'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(img)
plt.title('PIL'), plt.xticks([]), plt.yticks([])

plt.show()

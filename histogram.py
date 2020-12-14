# """
#  * Generate a grayscale histogram for an image.
#  *
#  * Usage: python GrayscaleHistogram.py <fiilename>
# """
# import sys
# import numpy as np
# import skimage.color
# import skimage.io
# import skimage.viewer
# from matplotlib import pyplot as plt
# import cv2 as cv
# from PIL import Image, ImageEnhance
# # read image, based on command line filename argument;
# # read the image as grayscale from the outset


# arr = [[6, 6, 7, 7, 2, 1, 1, 1],
#        [7, 7, 6, 6, 2, 1, 1, 1],
#        [7, 7, 6, 6, 1, 1, 2, 0],
#        [7, 7, 6, 6, 7, 7, 8, 8],
#        [7, 7, 7, 7, 8, 9, 8, 7],
#        [7, 6, 7, 7, 7, 8, 9, 7],
#        [7, 7, 7, 7, 1, 1, 1, 2],
#        [6, 6, 6, 7, 1, 1, 0, 0],
#        ]
# # img = Image.open('img3.jpg')

# # pixels = img.load()
# # img1 = img.convert('L')

# # img2 = cv.imread('img3.jpg')
# # dst_final = cv.medianBlur(img2, 3)
# # img_rgb = cv.cvtColor(img2, cv.COLOR_BGR2RGB)
# # create the histogram gray
# # histogram, bin_edges = np.histogram(img1, bins=256, range=(0, 255))
# histogram, bin_edges = np.histogram(, bins=256, range=(0, 255))

# # colors = ("b", "g", "r")
# # channel_ids = (0, 1, 2)

# # # create the histogram plot, with three lines, one for
# # # each color

# # plt.figure()
# # plt.subplot(121), plt.imshow(img_rgb)
# # plt.title('Anh goc'), plt.xticks([]), plt.yticks([])

# # plt.subplot(122)
# # plt.xlim([0, 256])
# # for channel_id, c in zip(channel_ids, colors):
# #     histogram, bin_edges = np.histogram(
# #         img_rgb[:, :, channel_id], bins=256, range=(0, 256)
# #     )
# #     plt.plot(bin_edges[0:-1], histogram, color=c)

# # plt.xlabel("Color value")
# # plt.ylabel("Pixels")


# # configure and draw the histogram figure
# # plt.figure()
# # plt.subplot(341), plt.imshow(img1, cmap='gray')
# # plt.title('Anh goc'), plt.xticks([]), plt.yticks([])
# # plt.subplot(342)
# # plt.title("Grayscale Histogram")
# # plt.xlabel("grayscale value"), plt.ylabel("pixels")
# # plt.xlim([0, 255])  # <- named arguments do not work here
# # plt.plot(bin_edges[0:-1], histogram)  # <- or here


# # plt.subplot(121), plt.imshow(dst_final, cmap='gray')
# # plt.title('Filter'), plt.xticks([]), plt.yticks([])
# # plt.subplot(122)
# # plt.title("Grayscale Histogram")
# # plt.xlabel("grayscale value"), plt.ylabel("pixels")
# # plt.xlim([0, 255])  # <- named arguments do not work here
# # plt.plot(bin_edges1[0:-1], histogram1)  # <- or here

# # plt.plot(arr)
# # plt.show()

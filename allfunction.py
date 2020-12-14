
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np


def show5(img, magnitude_spectrum, showmask, fshift_mask_mag, img_back):
    fig = plt.figure(figsize=(12, 12))
    ax1 = fig.add_subplot(2, 3, 1)
    ax1.imshow(img, cmap='gray')
    ax1.title.set_text('Input Image')
    ax2 = fig.add_subplot(2, 3, 2)
    ax2.imshow(magnitude_spectrum, cmap='gray')
    ax2.title.set_text('FFT of image')
    ax4 = fig.add_subplot(2, 3, 4)
    ax4.imshow(fshift_mask_mag, cmap='gray')
    ax4.title.set_text('FFT * Mask')
    ax5 = fig.add_subplot(2, 3, 5)
    ax5.imshow(img_back, cmap='gray')
    ax5.title.set_text('After inverse FFT')
    ax3 = fig.add_subplot(2, 3, 3)
    ax3.imshow(showmask, cmap='gray')
    ax3.title.set_text('Mask')
    plt.show()


def show4(img, magnitude_spectrum, showmask, fshift_mask_mag):
    fig = plt.figure(figsize=(12, 12))
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.imshow(img, cmap='gray')
    ax1.title.set_text('Input Image')
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.imshow(magnitude_spectrum, cmap='gray')
    ax2.title.set_text('FFT of image')
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.imshow(showmask, cmap='gray')
    ax3.title.set_text('Mask')
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.imshow(fshift_mask_mag, cmap='gray')
    ax4.title.set_text('Output Image')

    plt.show()


def show2(img, title1, magnitude_spectrum, title2):
    fig = plt.figure(figsize=(12, 12))
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.imshow(img, cmap='gray')
    ax1.title.set_text(title1)
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.imshow(magnitude_spectrum, cmap='gray')
    ax2.title.set_text(title2)
    plt.show()


def HPF(M, N, Do):
   # M, N = img.shape
    crow, ccol = int(M / 2), int(N / 2)

    mask = np.ones((M, N, 2), np.uint8)
    r = Do
    center = [crow, ccol]
    x, y = np.ogrid[:M, :N]
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
    mask[mask_area] = 0
    return mask


def LPF(M, N, Do):
   # M, N = img.shape
    crow, ccol = int(M / 2), int(N / 2)
    mask = np.zeros((M, N, 2), np.uint8)
    r = Do
    center = [crow, ccol]
    x, y = np.ogrid[:M, :N]
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
    mask[mask_area] = 1
    return mask


def BPF(M, N, d_in, d_out):
    mask = np.ones((M, N, 2), np.uint8)
    crow, ccol = int(M / 2), int(N / 2)
    r_out = d_out  # 80
    r_in = d_in  # 10
    center = [crow, ccol]
    x, y = np.ogrid[:M, :N]
    mask_area = np.logical_and(((x - center[0]) ** 2 + (y - center[1]) ** 2 >= r_in ** 2),
                               ((x - center[0]) ** 2 + (y - center[1]) ** 2 <= r_out ** 2))
    mask[mask_area] = 0
    return mask


def LGaussian(M, N, Do):
    # Mặt nạ bộ lọc thông thấp Gausian
    #M, N = img.shape
    crow, ccol = int(M / 2), int(N / 2)
    mask = np.zeros((M, N, 2), np.float32)
    r = Do
    b = 2*(r**2)
    center = [crow, ccol]
    for i in range(M):
        for j in range(N):
            D = (i-center[0])**2 + (j-center[1])**2
            mask[i, j] = np.exp(-D/b)
    return mask


def LButterworth(M, N, Do, n):
    #M, N = img.shape
    crow, ccol = int(M / 2), int(N / 2)
    mask = np.zeros((M, N, 2), np.float32)
    r = Do
    do2 = (r**2)
    center = [crow, ccol]
    for i in range(M):
        for j in range(N):
            D = (i-center[0])**2 + (j-center[1])**2
            mask[i, j] = (1+((D**n)/(do2**n)))**(-1)
    return mask


def addBTWnot(M, N, Do, x, y, n=1):
    Hlp = LButterworth(M, N, Do, n)
    H = 1-Hlp
    H = np.roll(H, x-1-int(N/2), axis=1)
    H = np.roll(H, y-1-int(M/2), axis=0)

    return H
# def Laplace(img):
#     mask = np.array([[0, 1, 0],
#                      [1, -4, 1],
#                      [0, 1, 0]])
#     return mask

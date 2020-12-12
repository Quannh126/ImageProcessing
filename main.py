import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv2

img = cv2.imread('./numpy.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(231)
plt.title('Ảnh gốc')
plt.imshow(img, cmap='gray')

plt.subplot(232)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
plt.title('Ảnh xám')
plt.imshow(gray, cmap='gray')


def filter_f2(img, a, b, beta, L):
    w, h, c = img.shape
    ret = np.zeros(img.shape, dtype=np.uint8)
    for z in range(c):
        for i in range(w):
            for j in range(h):
                if 0 <= img[i][j][z] and img[i][j][z] < a:
                    ret[i][j] = 0
                elif a <= img[i][j][z] and img[i][j][z] < b:
                    ret[i][j][z] = beta*(img[i][j][z] - a)
                elif b <= img[i][j][z] and img[i][j][z] < L:
                    ret[i][j][z] = beta*(b - a)
    return ret


def tangTuongPhan():
    img_1 = filter_f2(img, a=50, b=100, beta=3, L=255)

    plt.subplot(233)
    plt.title('Tăng độ tương phản')
    plt.imshow(img_1)


tangTuongPhan()

src = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
src[:,:,0] = cv2.equalizeHist(src[:,:,0])

# convert the YUV image back to RGB format
img_output = cv2.cvtColor(src, cv2.COLOR_YUV2BGR)

plt.subplot(234)
plt.title('Cân bằng sáng')
plt.imshow(img_output)

kernel = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])
trungbinh = cv2.blur(img, (3,3))


plt.subplot(235)
plt.imshow(trungbinh)
plt.title('Lọc trung bình')

trungvi = cv2.medianBlur(img, 3)
plt.subplot(236)
plt.imshow(trungvi)
plt.title('Lọc trung vị')


plt.show()

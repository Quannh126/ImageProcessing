import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('img5.png', 0)
# imgarr = [[9, 7, 1, 1, 1, 2, 2, 1],
#           [8, 9, 9, 7, 1, 1, 1, 1],
#           [7, 8, 9, 7, 1, 2, 1, 1],
#           [8, 9, 9, 9, 9, 1, 1, 2],
#           [8, 9, 9, 7, 7, 2, 1, 3],
#           [9, 91, 89, 9, 8, 2, 2, 1],
#           [9, 9, 8, 8, 7, 1, 2, 1],
#           [8, 9, 8, 6, 5, 1, 1, 3]]
# Bo loc trung binh
# dst_final = cv.blur(img, (3, 3))
# Bo loc gaussian
# dst_final = cv.GaussianBlur(img, (3, 3), 0)
# Bo loc trung vi
dst_final = cv.medianBlur(imgarr, 3)

# dst_final = cv.bilateralFilter(dst2, 9, 75, 75)
# dst_final = cv.medianBlur(dst2, 3)
# img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# dst_final_rgb = cv.cvtColor(dst_final, cv.COLOR_BGR2RGB)

plt.subplot(121), plt.imshow(img_rgb), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst_final_rgb), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

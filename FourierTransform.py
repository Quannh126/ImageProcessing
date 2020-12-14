

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
from allfunction import LButterworth, LGaussian, HPF, LPF, BPF, addBTWnot, show2, show5, show4
# Load ảnh
img = cv.imread('noiseball.png', 0)

# Đầu ra là một mảng hai chiều có 1 chiều là thực và 1 chiều là ảo
# Để biến đổi FFT trong openCV cần chuyển ảnh về  thành float32
dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)

# Sắp xếp lại phép biến đổi Fourier bằng cách dịch chuyển thành phần tần số 0 về trung tâm mảng
# Nếu không nó sẽ bắt đầu từ trên cùng bên trai của mảng
dft_shift = np.fft.fftshift(dft)

# Magnitude of the function is 20.log(abs(f))
# For values that are 0 we may end up with indeterminate values for log.
# So we can add 1 to the array to avoid seeing a warning.
magnitude_spectrum = 20 * \
    np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
M, N = img.shape

H1 = addBTWnot(M, N, 10, 138, 80, 1)
H2 = addBTWnot(M, N, 10, 172, 78, 1)
H3 = addBTWnot(M, N, 10, 150, 178, 1)
H4 = addBTWnot(M, N, 10, 185, 178, 1)
mask = H1
# mask = H1 + H2 + H3 + H4
# Mặt nạ lọc thôn cao (HPF- High pass filter)
# Sử dụng để phát hiện cạnh của vật thể
# Các cạnh hầu hết có tần số cao
# Khuếch đại nhiễu

# ------------------------------------------------------------------------------------
# Mặt nạ lọc thông thấp (LPF-low pass filter)
# Nhận đc các tần số thấp và vùng mịn
# Có thể làm mịn nhiễu nhưng lại làm mờ cạnh


# --------------------------------------------------------------------------------
# Mặt nạ lọc thông dải (BPF- Band pass filter) loại bỏ tần số bên ngoài phạm vi
# rows, cols = img.shape
# crow, ccol = int(rows / 2), int(cols / 2)


# ------------------------------------------------------------------------------------
# Mặt nạ bộ lọc thông thấp Gausian

# --------------------------------------------------------------------------------------
# Lọc thông thấp Butterworth

# -------------------------------------------------------------------------------------
# Lọc thông Cao Butterworth

# -------------------------------------------------------------------------------------
# Nhân ảnh sau khi biến đổi fourier với mặt nạ
fshift = dft_shift * H1

# Nhân phổ  cường độ để vẽ biểu đồ
fshift_mask_mag = 20 * np.log(cv.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

# Chuyển điểm gốc về vị trí cũ
f_ishift = np.fft.ifftshift(fshift)

# Biển đổi Fourier nghịch để đưa ảnh về miền không gian
# mà trận Số phức
img_back = cv.idft(f_ishift)

# Phổ độ lớn của miền ảnh
img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])

showmask = mask[:, :, :1]
#show2(img, 'Ảnh Gốc', magnitude_spectrum, "FFT cua ảnh")
show5(img, magnitude_spectrum, showmask, fshift_mask_mag, img_back)

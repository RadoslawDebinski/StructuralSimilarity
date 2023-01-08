import math
import numpy as np
import cv2

class StructuralSimilarity:
    def __init__(self):
        pass
    def ssim(self, img1, img2):
        self.img1 = img1.astype(np.float64)
        self.img2 = img2.astype(np.float64)
        #For kernel any positive, rational size is acceptable, sigma = 1 is average choice
        kernel = cv2.getGaussianKernel(3, 1)
        #Creating matrix of gaussian filter coefficient 2D
        k2d = np.outer(kernel, kernel.transpose())
        #Calculating params
        mx = cv2.filter2D(self.img1, -1, k2d)
        my = cv2.filter2D(self.img2, -1, k2d)
        sigmax = cv2.filter2D(self.img1**2, -1, k2d) - np.square(mx)
        sigmay = cv2.filter2D(self.img2**2, -1, k2d) - np.square(my)
        sigma = cv2.filter2D(self.img1 * self.img2, -1, k2d) - (mx * my)
        #Constants usual for alghorithm
        bitPerPx = np.dtype(np.array(self.img1)[0][0]).itemsize
        c1 = (0.01*((2 ** bitPerPx) - 1)) ** 2
        c2 = (0.03*((2 ** bitPerPx) - 1)) ** 2
        #Gradient mask
        gradMask = ((2 * mx * my + c1) * (2 * sigma + c2)) / ((np.square(mx) + np.square(my) + c1) * (sigmax + sigmay + c2))
        return gradMask

import cv2
import numpy as np


if __name__ == "__main__":

    # First we will test it with the grayscale.
    img = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)
    rows, cols = img.shape

    image = np.sqrt(img)

    gx = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0, ksize=1)
    gy = cv2.Sobel(np.float32(image), cv2.CV_32F, 0, 1, ksize=1)

    cv2.imshow('Original', img)
    cv2.imshow('Sobel vertical', gx)
    cv2.imshow('Sobel horizontal', gy)

    print(gx)

    mag, ang = cv2.cartToPolar(gx, gy)
    cv2.waitKey(0)

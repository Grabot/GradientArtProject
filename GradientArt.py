import cv2
import numpy as np


def load_image_grey(image_name):
    return cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)


def load_image_colour(image_name, colour):
    c = []
    image = cv2.imread(image_name)

    for x in image:
        line = []
        for y in x:
            line.append(y[colour])
        c.append(line)

    return c


if __name__ == "__main__":
    # First we will test it with the grayscale.
    img = load_image_grey('Lenna.png')

    img_red = load_image_colour('Lenna.png', 0)
    img_green = load_image_colour('Lenna.png', 1)
    img_blue = load_image_colour('Lenna.png', 2)
    rows, cols = img.shape

    image = np.sqrt(img_blue)

    gx = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0, ksize=1)
    gy = cv2.Sobel(np.float32(image), cv2.CV_32F, 0, 1, ksize=1)

    cv2.imshow('Original', img)
    cv2.imshow('Sobel vertical', gx)
    cv2.imshow('Sobel horizontal', gy)

    # print(gx)
    mag, ang = cv2.cartToPolar(gx, gy)
    cv2.waitKey(0)

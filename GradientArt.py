import cv2
import numpy as np
from MainWindow import MainWindow

def load_image_grey(image_name):
    return cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)


def load_image(image_name):
    return cv2.imread(image_name)


def load_image_colour(image_name, colour):
    c = []
    image = cv2.imread(image_name)

    for x in image:
        line = []
        for y in x:
            line.append(y[colour])
        c.append(line)

    return c


def create_vector_array(gradient_x, gradient_y):
    vector_array = []
    for x in range(0, len(gradient_x)):
        line = []
        for y in range(0, len(gradient_y)):
            entry = [gradient_x[x][y], gradient_y[x][y]]
            line.append(entry)
        vector_array.append(line)
    return vector_array


# reducing the vector array by 2 (call this more times if you want to reduce it more.
def reduce_vector_array(array):
    vector_array = []
    for x in range(0, len(array), 2):
        line = []
        for y in range(0, len(array[x]), 2):
            total = [0, 0]
            total[0] += array[x][y][0]
            total[0] += array[x+1][y][0]
            total[0] += array[x][y+1][0]
            total[0] += array[x+1][y+1][0]
            total[1] += array[x][y][1]
            total[1] += array[x+1][y][1]
            total[1] += array[x][y+1][1]
            total[1] += array[x+1][y+1][1]
            line.append(total)
        vector_array.append(line)
    return vector_array


if __name__ == "__main__":
    # First we will test it with the grayscale.
    img = load_image('Lenna.png')
    img_grey = load_image_grey('Lenna.png')

    img_red = load_image_colour('Lenna.png', 0)
    img_green = load_image_colour('Lenna.png', 1)
    img_blue = load_image_colour('Lenna.png', 2)
    rows, cols = img_grey.shape

    image = np.sqrt(img_grey)
    image_red = np.sqrt(img_red)
    image_green = np.sqrt(img_green)
    image_blue = np.sqrt(img_blue)

    gx = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0, ksize=1)
    gy = cv2.Sobel(np.float32(image), cv2.CV_32F, 0, 1, ksize=1)

    red_x = cv2.Sobel(np.float32(image_red), cv2.CV_32F, 1, 0, ksize=1)
    red_y = cv2.Sobel(np.float32(image_red), cv2.CV_32F, 0, 1, ksize=1)
    green_x = cv2.Sobel(np.float32(image_green), cv2.CV_32F, 1, 0, ksize=1)
    green_y = cv2.Sobel(np.float32(image_green), cv2.CV_32F, 0, 1, ksize=1)
    blue_x = cv2.Sobel(np.float32(image_blue), cv2.CV_32F, 1, 0, ksize=1)
    blue_y = cv2.Sobel(np.float32(image_blue), cv2.CV_32F, 0, 1, ksize=1)

    red = create_vector_array(red_x, red_y)
    green = create_vector_array(green_x, green_y)
    blue = create_vector_array(blue_x, blue_y)

    red = reduce_vector_array(red)
    red = reduce_vector_array(red)
    red = reduce_vector_array(red)
    red = reduce_vector_array(red)
    red = reduce_vector_array(red)
    red = reduce_vector_array(red)

    green = reduce_vector_array(green)
    green = reduce_vector_array(green)
    green = reduce_vector_array(green)
    green = reduce_vector_array(green)
    green = reduce_vector_array(green)
    green = reduce_vector_array(green)

    blue = reduce_vector_array(blue)
    blue = reduce_vector_array(blue)
    blue = reduce_vector_array(blue)
    blue = reduce_vector_array(blue)
    blue = reduce_vector_array(blue)
    blue = reduce_vector_array(blue)

    # cv2.imshow('Original', img)
    # cv2.imshow('Sobel vertical', gx)
    # cv2.imshow('Sobel horizontal', gy)
    # cv2.imshow('Sobel vertical red', red_x)
    # cv2.imshow('Sobel horizontal red', red_y)
    # cv2.imshow('Sobel vertical green', green_x)
    # cv2.imshow('Sobel horizontal green', green_y)
    # cv2.imshow('Sobel vertical blue', blue_x)
    # cv2.imshow('Sobel horizontal blue', blue_y)

    # mag, ang = cv2.cartToPolar(gx, gy)
    # cv2.waitKey(0)

    window = MainWindow(512, 512, red, green, blue, "Gradient art project")
    window.main_loop()


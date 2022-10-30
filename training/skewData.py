import os
import cv2
import imghdr

dir = './PokemonData'
image_ext = ['jpeg', 'jpg', 'png']


def saveImage(image, folderPath, fileName, prefix):
    try:
        fullpath = os.path.join(folderPath, prefix+fileName)
        cv2.imwrite(fullpath, image)
        cv2.waitKey(0)
        return
    except Exception as e:
        print("failed to save"+fullpath)
        return


def greyscale(image, folderPath, fileName):
    print("greyscaling "+fileName)
    greyscaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    saveImage(greyscaled, folderPath, fileName, "greyscaled_")
    return


def flip_horizontally(image, folderPath, fileName):
    print("flipping horizontally "+fileName)
    flipped = cv2.flip(image, 1)
    saveImage(flipped, folderPath, fileName, "flipped_horizontal_")
    return


def flip_vertically(image, folderPath, fileName):
    print("flipping vertically "+fileName)
    flipped = cv2.flip(image, 0)
    saveImage(flipped, folderPath, fileName, "flip_vertically_")
    return


for folder in os.listdir(dir):
    folderPath = os.path.join(dir, folder)
    for fileName in os.listdir(folderPath):
        filePath = os.path.join(folderPath, fileName)
        tip = imghdr.what(filePath)

        if tip in image_ext:
            image = cv2.imread(filePath)
            print(filePath)
            greyscale(image, folderPath, fileName)
            flip_horizontally(image, folderPath, fileName)
            flip_vertically(image, folderPath, fileName)

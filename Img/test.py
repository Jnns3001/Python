import sys

import cv2
import numpy as np

filetype = ".png"
img_size = [2000, 1150]

directory = "C:/Users/Jannis/Documents/HLL/PanzerTaschenBuch/Bilder/Skaliert/ISO - Kopie/"
img = cv2.imread(directory + 'Allies.png')
# np.set_printoptions(threshold=sys.maxsize)
print(img)
cv2.imwrite(directory + "test.png",np.full((1125, 2000, 3), 255, "uint8"))
"""
def cg(name, img_names, axis=1):
    images = []
    for img_name in img_names:
        images.append(cv2.imread(directory + img_name + filetype))
    concat = np.concatenate(images, axis=axis)

    cv2.imwrite(directory + name + filetype, concat)


directory = "C:/Users/Jannis Z30-C/Documents/HLL/PanzerTaschenBuch/Bilder/Skaliert/ISO - Kopie/"
cv2.imwrite(directory + "white.png",np.full((1125, 2000, 3), 255, "uint8"))
cg("Germany", ['Tiger', 'Panther', 'P4', 'Luchs', 'Puma'])
cg("America", ['j76', 'j75', 'm75', 'Stuart', 'Greyhound'])
cg("Russia", ['is1', 't34', 't70', 'ba10'])
cg("British", ['Churchill', 'Firefly', 'Crusader', 'Cromwell', 'Honey', 'Tetrarch', 'Daimler'])
cg("AlliesRecon", ["Greyhound", "ba10", "Daimler", "white", "white"])
cg("AlliesLight", ["Stuart", "t70", "Honey", "Tetrarch", "white"])
cg("AlliesMedium", ["m75", "t34", "Crusader", "Cromwell", "white"])
cg("AlliesHeavy", ["j76", "j75", "is1", "Churchill", "Firefly"])
cg("Allies", ["AlliesRecon", "AlliesLight", "AlliesMedium", "AlliesHeavy"], axis=0)
cg("Axis", ["Puma", "Luchs", "P4", "Panther", "Tiger"], axis=0)

"""
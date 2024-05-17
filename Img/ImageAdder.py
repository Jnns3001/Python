import cv2
import numpy as np

filetype = ".png"
img_size = [2000, 1150]


def cg(name, img_names, axis=1):
    images = []
    for img_name in img_names:
        images.append(cv2.imread(directory + img_name + filetype))
    concat = np.concatenate(images, axis=axis)

    cv2.imwrite(directory + name + filetype, concat)


#"""
directory = "C:/Users/Jannis Z30-C/Documents/HLL/PanzerTaschenBuch/Bilder/Skaliert/ISO/"
# directory = "C:/Users/Jannis/Documents/HLL/PanzerTaschenBuch/Bilder/Skaliert/ISO/"
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
"""
directory = "C:/Users/Jannis Z30-C/Documents/HLL/PanzerTaschenBuch/Bilder/Skaliert/HE/"
# directory = "C:/Users/Jannis/Documents/HLL/PanzerTaschenBuch/Bilder/Skaliert/HE/"
cg("HELuchs", ["Luchs back", "Luchs side"], axis=0)
cg("HEStuart", ["Stuart back", "Stuart side"], axis=0)
cg("HEt70", ["t70 back", "t70 side"], axis=0)
cg("HEHoney", ["Honey back", "Honey side"], axis=0)
cg("HETetrarch", ["Tetrarch back", "Tetrarch side"], axis=0)
cg("HE", ["HELuchs", "HEStuart", "HEt70", "HEHoney", "HETetrarch"])
#"""

directory = "C:/Users/Jannis Z30-C/Documents/HLL/PanzerTaschenBuch/Bilder/Skaliert/Motor/"
# directory = "C:/Users/Jannis/Documents/HLL/PanzerTaschenBuch/Bilder/Skaliert/Motor/"
#"""


cg("EngineGerman", ["EngineLuchs", "EngineP4", "EngineTiger", "EnginemPanther", "white", "white"])
cg("EngineAmerican", ["EngineStuart", "Enginem75", "Enginetj76", "white", "white", "white"])
cg("EngineRussian", ["Enginet70", "Enginet34", "Engineis1", "white", "white", "white"])
cg("EngineBritish", ["EngineHoney", "EngineTetrarch", "EngineCrusader", "EngineCromwell", "EngineChurchill", "EngineFirefly"])
#"""


cg("EngineLuchs", ["Luchs back", "Luchs side"], axis=0)
cg("EngineStuart", ["Stuart back", "Stuart side"], axis=0)
cg("Enginet70", ["t70 back", "t70 side"], axis=0)
cg("EngineHoney", ["Honey back", "Honey side"], axis=0)
cg("EngineTetrarch", ["Tetrarch back", "Tetrarch side"], axis=0)

cg("EngineLight", ["EngineLuchs", "EngineStuart", "Enginet70", "EngineHoney", "EngineTetrarch", "white"])

cg("EngineP4", ["P4 back", "P4 side"], axis=0)
cg("Enginem75", ["m75 back", "m75 side"], axis=0)
cg("Enginet34", ["t34 back", "t34 side"], axis=0)
cg("EngineCrusader", ["Crusader back", "Crusader side"], axis=0)
cg("EngineCromwell", ["Cromwell back", "Cromwell side"], axis=0)

cg("EngineMedium", ["EngineP4", "Enginem75", "Enginet34", "EngineCrusader", "EngineCromwell", "white"])

cg("EngineTiger", ["Tiger back", "Tiger side"], axis=0)
cg("EnginemPanther", ["Panther back", "Panther side"], axis=0)
cg("Enginetj76", ["j76 back", "j76 side"], axis=0)
cg("Engineis1", ["is1 back", "is1 side"], axis=0)
cg("EngineChurchill", ["Churchill back", "Churchill side"], axis=0)

cg("EngineFirefly", ["Firefly back", "Firefly side"], axis=0)

cg("EngineHeavy", ["EngineTiger", "EnginemPanther", "Enginetj76", "Engineis1", "EngineChurchill", "EngineFirefly"])

cg("Engine", ["EngineLight", "EngineMedium", "EngineHeavy"], axis=0)


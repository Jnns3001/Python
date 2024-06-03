import cv2
import numpy as np

# std_path = "C:/Users/Jannis Z30-C/Documents/HLL/PanzerTaschenBuch/"
std_path = "C:/Users/Jannis/Documents/HLL/PanzerTaschenBuch/"
filetype = ".png"
img_size = [2000, 1150]


def cg(name, img_names, axis=1):
    images = []
    for img_name in img_names:
        images.append(cv2.imread(std_path + directory + img_name + filetype))
    concat = np.concatenate(images, axis=axis)

    cv2.imwrite(std_path + directory + "out/" + name + filetype, concat)


#"""
directory = "Bilder/Skaliert/ISO/"
cv2.imwrite(std_path + directory + "out/white.png", np.full((1125, 2000, 3), 255, "uint8"))
cg("IsoGerman", ['Puma', 'Luchs', 'P4', 'Panther', 'Tiger'], axis=0)
cg("IsoAmericanFilled", ['Greyhound', 'Stuart', 'm75', 'j75', 'j76'], axis=0)  # , 'j75'
cg("IsoRussianFilled", ['ba10', 't70', 't34', 'is1', "out/white"], axis=0)
cg("IsoBritainFilled", ['Daimler', 'Honey', 'Crusader', 'Churchill', "out/white"], axis=0)
cg("IsoBritainLWFilled", ["out/white", 'Tetrarch', 'Cromwell', 'Firefly', "out/white"], axis=0)
cg("IsoAmerican", ['Greyhound', 'Stuart', 'm75', 'j76'], axis=0)  # , 'j75'
cg("IsoRussian", ['ba10', 't70', 't34', 'is1'], axis=0)
cg("IsoBritain", ['Daimler', 'Honey', 'Crusader', 'Churchill'], axis=0)
cg("IsoBritainLW", ["out/white", 'Tetrarch', 'Cromwell', 'Firefly'], axis=0)
cg("IsoAllies", ["out/IsoAmerican", "out/IsoRussian", "out/IsoBritain", "out/IsoBritainLW"])
cg("IsoAlliesFilled", ["out/IsoAmericanFilled", "out/IsoRussianFilled", "out/IsoBritainFilled", "out/IsoBritainLWFilled"])
cg("IsoAll", ["out/IsoGerman", "out/IsoAlliesFilled"])
cg("Iso Heavy", ["Tiger", "j76", "is1", "Panther"])

#"""
"""
directory = "Bilder/Skaliert/HE/"
cg("HELuchs", ["Luchs back", "Luchs side"], axis=0)
cg("HEStuart", ["Stuart back", "Stuart side"], axis=0)
cg("HEt70", ["t70 back", "t70 side"], axis=0)
cg("HEHoney", ["Honey back", "Honey side"], axis=0)
cg("HETetrarch", ["Tetrarch back", "Tetrarch side"], axis=0)
cg("HE", ["out/HELuchs", "out/HEStuart", "out/HEt70", "out/HEHoney", "out/HETetrarch"])
"""

"""
directory = "Bilder/Skaliert/Motor/"

cv2.imwrite(std_path + directory + "out/vwhite.png", np.full((1800, 1200, 3), 255, "uint8"))
cv2.imwrite(std_path + directory + "out/hwhite.png", np.full((900, 2400, 3), 255, "uint8"))

cg("vEngineLuchs", ["Luchs back", "Luchs side"], axis=0)
cg("vEngineStuart", ["Stuart back", "Stuart side"], axis=0)
cg("vEnginet70", ["t70 back", "t70 side"], axis=0)
cg("vEngineHoney", ["Honey back", "Honey side"], axis=0)
cg("vEngineTetrarch", ["Tetrarch back", "Tetrarch side"], axis=0)
cg("hEngineLuchs", ["Luchs back", "Luchs side"])
cg("hEngineStuart", ["Stuart back", "Stuart side"])
cg("hEnginet70", ["t70 back", "t70 side"])
cg("hEngineHoney", ["Honey back", "Honey side"])
cg("hEngineTetrarch", ["Tetrarch back", "Tetrarch side"])

cg("vEngineP4", ["P4 back", "P4 side"], axis=0)
cg("vEnginem75", ["m75 back", "m75 side"], axis=0)
cg("vEnginet34", ["t34 back", "t34 side"], axis=0)
cg("vEngineCrusader", ["Crusader back", "Crusader side"], axis=0)
cg("vEngineCromwell", ["Cromwell back", "Cromwell side"], axis=0)
cg("hEngineP4", ["P4 back", "P4 side"])
cg("hEnginem75", ["m75 back", "m75 side"])
cg("hEnginet34", ["t34 back", "t34 side"])
cg("hEngineCrusader", ["Crusader back", "Crusader side"])
cg("hEngineCromwell", ["Cromwell back", "Cromwell side"])

cg("vEngineTiger", ["Tiger back", "Tiger side"], axis=0)
cg("vEnginemPanther", ["Panther back", "Panther side"], axis=0)
cg("vEnginetj76", ["j76 back", "j76 side"], axis=0)
cg("vEnginetj75", ["j75 back", "j75 side"], axis=0)
cg("vEngineis1", ["is1 back", "is1 side"], axis=0)
cg("vEngineChurchill", ["Churchill back", "Churchill side"], axis=0)
cg("vEngineFirefly", ["Firefly back", "Firefly side"], axis=0)
cg("hEngineTiger", ["Tiger back", "Tiger side"])
cg("hEnginemPanther", ["Panther back", "Panther side"])
cg("hEnginetj76", ["j76 back", "j76 side"])
cg("hEnginetj75", ["j75 back", "j75 side"])
cg("hEngineis1", ["is1 back", "is1 side"])
cg("hEngineChurchill", ["Churchill back", "Churchill side"])
cg("hEngineFirefly", ["Firefly back", "Firefly side"])
"""

"""
cg("hvEngineMedium", ["out/vEngineP4", "out/vEnginem75", "out/vEnginet34", "out/vEngineCrusader", "out/vEngineCromwell", "out/vwhite"])
cg("hvEngineLight", ["out/vEngineLuchs", "out/vEngineStuart", "out/vEnginet70", "out/vEngineHoney", "out/vEngineTetrarch", "out/vwhite"])
cg("hvEngineHeavy", ["out/vEngineTiger", "out/vEnginemPanther", "out/vEnginetj76", "out/vEngineis1", "out/vEngineChurchill", "out/vEngineFirefly"])

cg("vhEngineGerman", ["out/hEngineLuchs", "out/hEngineP4", "out/hEnginemPanther", "out/hEngineTiger"], axis=0)
cg("vhEngineAmerican", ["out/hEngineStuart", "out/hEnginem75", "out/hEnginetj75", "out/hEnginetj76"], axis=0)
cg("vhEngineRussian", ["out/hEnginet70", "out/hEnginet34", "out/hEngineis1", "out/hwhite"], axis=0)
cg("vhEngineBritain", ["out/hEngineHoney", "out/hEngineCrusader", "out/hEngineChurchill", "out/hwhite"], axis=0)
cg("vhEngineBritainLW", ["out/hEngineTetrarch", "out/hEngineCromwell", "out/hEngineFirefly", "out/hwhite"], axis=0)

cg("hhEngineGerman", ["out/hEngineLuchs", "out/hEngineP4", "out/hEnginemPanther", "out/hEngineTiger"])
cg("hhEngineAmerican", ["out/hEngineStuart", "out/hEnginem75", "out/hEnginetj75", "out/hEnginetj76"])
cg("hhEngineRussian", ["out/hEnginet70", "out/hEnginet34", "out/hEngineis1", "out/hwhite"])
cg("hhEngineBritain", ["out/hEngineHoney", "out/hEngineCrusader", "out/hEngineChurchill", "out/hwhite"])
cg("hhEngineBritainLW", ["out/hEngineTetrarch", "out/hEngineCromwell", "out/hEngineFirefly", "out/hwhite"])
"""
"""
cg("Engine1", ["out/hvEngineLight", "out/hvEngineMedium", "out/hvEngineHeavy"], axis=0)
cg("Engine2", ["out/vhEngineGerman", "out/vhEngineAmerican", "out/vhEngineRussian", "out/vhEngineBritain", "out/vhEngineBritainLW"]) # Complete
cg("Engine3", ["out/hhEngineGerman", "out/hhEngineAmerican", "out/hhEngineRussian", "out/hhEngineBritain", "out/hhEngineBritainLW"], axis=0) # Missing Panther j75
#"""

"""
directory = "Bilder/Skaliert/Sonderzonen/"

cg("top", ["Panther front", "is1 front", "Firefly front"])
cg("bottom", ["Tiger front", "is1 top", "t34 top"])
#"""

"""
directory = "Bilder/Skaliert/AT/Minen/"

cg("Mines", ["Mine German", "Mine US", "Mine Soviet", "Mine British"])

#"""
import cv2
import numpy as np

directory = "../../HLL/PanzerTaschenBuch/Bilder/Skaliert/ISO/"
outdir = directory + "out/"


def create_gallery(img_names, name):
    images = []
    for img_name in img_names:
        images.append(cv2.imread(directory + img_name))

    print(images)
    vis = np.concatenate(images, axis=1)
    cv2.imshow(name, vis)
    cv2.imwrite(outdir + name, vis)


deutsche = ('Tiger.png', 'Panther.png', 'P4.png', 'P4.png', 'Puma.png')  # Luchs placeholder
#create_gallery(deutsche, "Deutsche")

img1 = cv2.imread(directory + 'j76.png')
img2 = cv2.imread(directory + 'j75.png')
img3 = cv2.imread(directory + 'm75.png')
img4 = cv2.imread(directory + 'Stuart.png')
img5 = cv2.imread(directory + 'Greyhound.png')
vis = np.concatenate([img1, img2, img3, img4, img5], axis=1)
cv2.imwrite(directory + 'out/Amerikaner.png', vis)

img1 = cv2.imread(directory + 'is1.png')
img2 = cv2.imread(directory + 't34.png')
img3 = cv2.imread(directory + 't70.png')
img4 = cv2.imread(directory + 'ba10.png')
vis = np.concatenate((img1, img2, img3, img4), axis=1)
cv2.imwrite(directory + 'out/Russen.png', vis)

img1 = cv2.imread(directory + 'Churchill.png')
img2 = cv2.imread(directory + 'Firefly.png')
img3 = cv2.imread(directory + 'Crusader.png')
img4 = cv2.imread(directory + 'Cromwell.png')
img5 = cv2.imread(directory + 'Honey.png')
img6 = cv2.imread(directory + 'Tetrarch.png')
img7 = cv2.imread(directory + 'Daimler.png')
vis = np.concatenate((img1, img2, img3, img4, img5, img6, img7), axis=1)
cv2.imwrite(directory + 'out/Briten.png', vis)

from PIL import Image
import numpy as np

img = Image.open("귀여운개구리.png")

imgarray = np.asarray(img)


def randomizer1(img):
    x, y, c = img.shape
    for w in range(51):
        for q in range(51):
            for i in range(51):
                canvas = np.zeros_like(img)
                for j in range(x):
                    for k in range(y):
                        c = img[j, k]
                        c[0] += w*5
                        c[1] += q*5
                        c[2] += i*5
                        c[:3] %= 255
                        canvas[j, k] = c
                rndimage = Image.fromarray(canvas)
                filename = "randomizer1_" + str(w) + "_" + str(q) + "_" + str(i) + ".png"
                rndimage.save(filename)
                print(filename) 

randomizer1(imgarray)

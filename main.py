import numpy as np
import cv2
import matplotlib.pyplot as plt

def power_transformation(r, c, gamma):
    r = r.astype(np.float64)
    s = c * r**gamma
    s = rescale(s)
    return s

def rescale(img):
    img -= np.min(img)
    img /= np.max(img)
    img *= 255
    return img

mr_img_path = "./images/mr_images.tif"

mr_img = cv2.imread(mr_img_path, 0)

mr_gammas = [0.6, 0.4, 0.3]

mr_images = []

for gamma in mr_gammas:
    transformed = power_transformation(mr_img, 1, gamma)
    mr_images.append(transformed)

mr_hstacked1 = np.hstack((mr_img, mr_images[0]))
mr_hstacked2 = np.hstack((mr_images[1], mr_images[2]))

mr_vstacked = np.vstack((mr_hstacked1, mr_hstacked2))

plt.imshow(mr_vstacked, cmap="gray")
plt.show()

city_img_path = "./images/city.tif"
city_img = cv2.imread(city_img_path, 0)

city_gammas = [3, 4, 5]
city_images = []

for gamma in city_gammas:
    transformed = power_transformation(city_img, 1, gamma)
    city_images.append(transformed)

city_hstacked1 = np.hstack((city_img, city_images[0]))
city_hstacked2 = np.hstack((city_images[1], city_images[2]))

city_vstacked = np.hstack((city_hstacked1, city_hstacked2))

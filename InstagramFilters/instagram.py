import cv2
import matplotlib.pyplot as plt

im = cv2.imread("house.jpeg")
im2 = cv2.imread("flower.jpeg")
# blurimg = cv2.GaussianBlur(im,(101,101),cv2.BORDER_DEFAULT)
# plt.imshow(blurimg)

edges = cv2.Canny(im2,100,500)

plt.imshow(edges)
plt.show()
import cv2 

im = cv2.imread('cowboy.png')

# cv2.imshow('image', im)
# cv2.waitKey()

outputShape = (400, 800)
resized = cv2.resize(im, outputShape)

# cv2.imshow('resized', resized)
# cv2.waitKey()

cv2.imwrite('cowboy.png', resized)
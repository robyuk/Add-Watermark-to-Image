import cv2

image=cv2.imread('elfs.jpeg')
watermark=cv2.imread('watermark.png')

print(image.shape,watermark.shape)
#print(watermark)

#image.shape is tuple of (y, x, d) #d is colour depth

# Set x and y to the co-ordinates of the watermark in the image
# The watermark will be in the lower right corner of the image
x=image.shape[1] - watermark.shape[1]
y=image.shape[0] - watermark.shape[0]

# watermarkPlace is the portion of the image where the watermark will be.
watermarkPlace=image[y:,x:]
# create a new image that is the blend of the portion and the watermark itself
blend=cv2.addWeighted(watermarkPlace,0.7, watermark,0.3, 0)

# Put the blend in the lower right corner of the image
image[y:,x:]=blend

cv2.imwrite('elfs-watermarked.jpeg',image)
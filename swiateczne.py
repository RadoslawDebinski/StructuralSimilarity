import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import StructuralSimilarity as ss

#Get images and convert
fileName1 = 'org.jpg'
fileName2 = 'edited.jpg'
orgImg = cv.imread(fileName1)
edtImg = cv.imread(fileName2)
orgImgGray = cv.cvtColor(orgImg, cv.COLOR_BGR2GRAY)
edtImgGray = cv.cvtColor(edtImg, cv.COLOR_BGR2GRAY)

#Structural similarity gradient mask
SS = ss.StructuralSimilarity()
ssGradient = SS.ssim(orgImgGray, edtImgGray)
ssGradient = (ssGradient * 255).astype("uint8")

#Treshold by graient mean value
ssGradientMean = np.invert(np.array(ssGradient)).mean()
thr = cv.threshold(ssGradient, ssGradientMean, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1] #127

#Making mask for FloodFill Alghorithm
thrFlood = thr.copy()
height, width = thr.shape[:2]
mask = np.zeros((height + 2, width + 2), np.uint8)
#FloodFill with mask from (0,0) point replacing by 255
cv.floodFill(thrFlood, mask, (0, 0), 255);
#Invert floodfilled image
thrFloodInv = cv.bitwise_not(thrFlood)
#Combining treshold mask with floodfilled and making 3 channel mask
maskFlood = thr | thrFloodInv
maskFlood3Ch = cv.cvtColor(maskFlood, cv.COLOR_GRAY2BGR)
#Targets without background
imgNoBack = edtImg.copy()
imgNoBack[maskFlood3Ch==0] = 0


#Getting python list of countours
cont, hier = cv.findContours(maskFlood,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
#Calculating contours areas
areas = []
for c in cont:
    areas.append(cv.contourArea(c))

#Calculating mean and enclosing cont with large areas // dict(zip(keys,values))
areas = np.array(areas)
areasMean = areas.mean()
areasId = np.array(areas > areasMean)
cont = np.array(list(cont),dtype=tuple)
cont = (cont[areasId])

#Find index of biggest area
bigOne = np.argmax(areas[areasId])

roi = []
for c in cont:
    x,y,w,h = cv.boundingRect(c)
    roi.append(imgNoBack[y:y+h, x:x+w])
    edtImg = cv.rectangle(edtImg,(x,y),(x+w,y+h),(0,0,255),2)

#Creating one image with all ROIs and saving
bigOneShape = (int(roi[bigOne].shape[1]),int(roi[bigOne].shape[0]))
scaled = []
for r in roi:
    scaled.append(cv.resize(r, bigOneShape, interpolation = cv.INTER_AREA))
roiAsOne = cv.hconcat(scaled)
cv.imwrite('allGrinchesInOneNoBackground.jpg', roiAsOne)

cv.imwrite('biggestGrinchNoBackground.jpg', roi[bigOne])
cv.imwrite('editedWithGrinches.jpg', edtImg)

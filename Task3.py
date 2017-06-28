# -*- coding: utf-8 -*-
"""
Jose Fernández Ortiz
"""
import numpy as np
import cv2
import os

path ='c:\\improc'
os.chdir(path)
im = np.ones((700, 700), 'uint8') *255
            
r,c = im.shape[:2]

bases = []
bases.append([0,c/2])
bases.append([r-1,0])
bases.append([r-1,c-1])
point = (np.random.random(2) * im.shape).astype(int)
print point, point.shape, point.dtype
num = bases.shape[0]

num = bases.shape[0]
niterations = 1000000
for i in range(niterations):
    indx = int(np.random.random() * num)
    point[0] = (point[0]+ bases[indx][0])/2
    point[1] = (point[1]+ bases[indx][1])/2
    im[point[0], point[1]] = 0

cv2.imshow('triangle', im)
cv2.waitKey()
cv2.destroyAllWindows()
    
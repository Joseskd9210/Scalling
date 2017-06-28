# -*- coding: utf-8 -*-
"""
Jose Fernández Ortiz
"""

import numpy as np
import cv2
import os

def process_image(im):
    sfx = 0.5
    sfy = 0.5
    im2 = cv2.resize(im, None, fx = sfx, fy = sfy, interpolation = cv2.INTER_LINEAR)
    im3 = np.hstack((im2, im2))
    translation_matrix = np.array([[1,0,im2.shape[1]/2],[0,1, 0]], 'float32')
    im2 = cv2.warpAffine(im2, translation_matrix, (2*im2.shape[1], im2.shape[0]))
    im2 = np.vstack((im2,im3))
    return im2
path ='c:\\improc'
os.chdir(path)
im = cv2.imread('edin_castle.png')
rows, cols = im.shape[:2]
print 'orginnal size: ', im.shape[:2]

im2 = im.copy()


for i in range(5):
    im2 = process_image(im2)
    
    print 'scaled size ', im2.shape[:2]
    
cv2.imshow('image original', im)
cv2.imshow('New', im2)
cv2.waitKey()
cv2.destroyALLWindows();
#!/usr/bin/env python3
__author__ = 'Thibaut Kovaltchouk'
# -*- coding: utf-8 -*-

filename = "lenna.jpg"

import numpy as np
import cv2

def replace_impose(imageBGR, value, impose="H"):
    imgIn = cv2.cvtColor(imageBGR, cv2.COLOR_BGR2HSV)
    # we fixe the value depending of the parameter impose
    if impose.lower() == "h":
        imgIn[:,:,0] = value*np.ones(imgIn.shape[:2], dtype=np.uint8)
    elif impose.lower() == "s":
        imgIn[:,:,1] = value*np.ones(imgIn.shape[:2], dtype=np.uint8)
    elif impose.lower() == "v":
        imgIn[:,:,2] = value*np.ones(imgIn.shape[:2], dtype=np.uint8)
    else:
        print("impose = ", impose)
        print("Should be H, S or V")
    imgOut = cv2.cvtColor(imgIn, cv2.COLOR_HSV2BGR)
    return imgOut

imgIn = cv2.imread(filename)

listH = np.linspace(0, 360, 16)

for h in listH:
    img = np.copy(imgIn)
    New_img = replace_impose(img, int(h/2), impose="H")
    base = filename.split(".")[-2]
    outputImage = base + "_H" + str(int(h)) + ".png"
    cv2.imwrite(outputImage, New_img)
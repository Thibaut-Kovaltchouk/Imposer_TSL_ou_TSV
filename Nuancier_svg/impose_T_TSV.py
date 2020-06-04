#!/usr/bin/env python3
__author__ = 'Thibaut Kovaltchouk'
# -*- coding: utf-8 -*-

filename = "input_test.svg"

from colormath.color_objects import sRGBColor as RGBColor
from colormath.color_objects import HSVColor
from colormath.color_conversions import convert_color
from colormath.color_conversions import convert_color
import numpy as np

def replace_impose(strColorHex, value, impose="H"):
    color = RGBColor.new_from_rgb_hex(strColorHex)
    color = convert_color(color, HSVColor)
    # we fixe the value depending of the parameter impose
    if impose.lower() == "h":
        color.hsv_h = value
    elif impose.lower() == "s":
        color.hsv_s = value
    elif impose.lower() == "v":
        color.hsv_v = value
    else:
        print("impose = ", impose)
        print("Should be H, S or V")
    color = convert_color(color, RGBColor)
    return color.get_rgb_hex()

file = open(filename, mode='r')
svgFile = file.read()
file.close()

prefixes = ["fill:#", "stroke:#", "stop-color:#"]

set_colors = set() 
for prefix in prefixes:
    i = svgFile.find(prefix, 0)
    while i != -1:
        i = i + len(prefix)
        set_colors.add(svgFile[i:i+6])
        i = svgFile.find(prefix, i+6)


listH = np.linspace(0, 360, 16)

for h in listH:
    svgFileOut = svgFile[:]
    for color in set_colors:
        print(color)
        newColor = replace_impose(color, h, impose="H")
        print(newColor[1:])
        svgFileOut = svgFileOut.replace(color, newColor[1:])
    base = filename.split(".")[-2]
    file = open(base + "_H" + str(int(h))+".svg", mode='w')
    file.write(svgFileOut)
    file.close()
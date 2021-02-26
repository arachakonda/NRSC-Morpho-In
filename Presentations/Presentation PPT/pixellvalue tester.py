# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 01:07:39 2017

@author: Ananth
"""

import scipy.ndimage as nimg

image=nimg.imread('binary.png',flatten=False,mode='HSV')

print(image[46,22])
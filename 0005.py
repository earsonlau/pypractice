# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 00:11:13 2017

@author: zzz
"""

from PIL import Image
import os

path = '0005/pics'
resultPath = '0005/result'
if not os.path.isdir(resultPath):
    os.mkdir(resultPath)
for picName in os.listdir(path):
    picPath = os.path.join(path,picName)
    print(picPath)
    with Image.open(picPath) as im:
        w,h = im.size 
        n = w /1366 if (w/1366) >= (h/640) else h /640
        im.thumbnail(w / n, h / n)
        im.save(resultPath+'/finish_' + picName.split('-')[0] + '.jpg','jpeg')
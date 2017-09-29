# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 19:38:22 2017

@author: zzz
"""
import PIL 
from PIL import Image,ImageDraw,ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf',size= 20)
    fillcolor  ="#ff0000"
    width,height = img.size
    draw.text((width-40,0),'99',font = myfont,fill = fillcolor)
    img.save('result.jpg','jpeg')
    
    return 0
if __name__ == '__main__':
    image =Image.open ('zhihutouxiang.png')
    add_num(image)
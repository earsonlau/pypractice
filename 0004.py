# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 23:53:49 2017

@author: zzz
"""

import re
fin = open('0004.txt','r')
str = fin.read()

reObj = re.compile('\b?(\w+)\b?')
words = reObj.findall(str)

wordDict = dict()

for word in words:
    if word.lower() in wordDict:
        wordDict[word.lower()] += 1
    else:
        wordDict[word] = 1
        
for key ,value in wordDict.items():
    print ('%s: %s' % (key,value))
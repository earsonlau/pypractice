# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:33:23 2017

@author: zzz
"""
##可以不把文件放在源文件夹
##复杂版本
'''
import os
import re

def walk_dir(path):
    file_path = []
    for root,dirs,files in os.walk(path):
        for f in files:
            if f.lower().endswith('txt'):
                file_path.append(os.path.join(root,f))
    return file_path

def file_key_word(filepath):
    word_dic = {}
    filename = os.path.basename(filepath)
    with open(filepath) as f:
        text=f.read()
        words_list = re.findall(r'[A-Za-z]+',text.lower())
        for w in words_list:
            if w in word_dic:
                word_dic[w]+=1
            else :
                word_dic[w]=1
        sorted_word_list = sorted(word_dic.items(),key=lambda d:d[1])
        print ("在%s文件中，%s为关键词，共出现了%s次" ,(filename,sorted_word_list[-1][0],sorted_word_list[-1][1]))

if __name__=="__main__":
    for file_path in walk_dir(os.getcwd()):
        file_key_word(file_path)
'''
##简单版本,不区分大小写
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
sorted_word_list = sorted(wordDict.items(),key=lambda d:d[1])
print ("在文件中，%s为关键词，共出现了%s次" %(sorted_word_list[-1][0],sorted_word_list[-1][1]))
##其实上面的程序调用了很多的方法，下面有比较漂亮的写法，区分了大小写
import re

def list1(string):
    words = re.findall(r'[a-zA-z]+\b',string)
    return words

def file_read(filename):
    with open(filename,'r') as fp:
        article = fp.read()
    return article

def most_word_number(word_list):
    str_dict = {}
    for item in word_list:
        if item in str_dict:
            str_dict[item] +=1
            
        else :
            str_dict[item] = 1
    str_dict = {str_dict[key]:key for key in str_dict}
    return (max(str_dict),str_dict[max(str_dict)])

if __name__=='__main__':
    stirng = file_read('0004.txt')
    words = list1(string)
    times,word = most_word_number(words)
    print ('出现最多的单词为' + str(word)+'.出现了'+str(times)+'次')
    

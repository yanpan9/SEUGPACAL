#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
#filename=input("Please input the path of your GPA file:")
#print(filename)
filename="/home/yanpan/Study/python/GPA.html"
with open("/home/yanpan/Study/python/GPA1.html",'w') as f:
    with open(filename,'r') as file:
        for line in file.readlines():
            print('BEGIN=',line.strip())
            if re.search('</span>*&amp;nbsp',line):
                f.write(line)

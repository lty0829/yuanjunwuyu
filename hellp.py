# -*- coding: utf-8 -*-
import codecs

w=''
with codecs.open('as.txt', 'r','gbk') as f:
    w = f.read()
print w
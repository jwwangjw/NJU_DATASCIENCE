#!/usr/bin/python
# -*- coding: UTF-8 -*-
l=eval(input())
ll=eval(input())
re=[]
for i in range (0,len(l)):
    if(ll.count(l[i])!=0):
        re.append(l[i])
re=list(set(re))
re.sort()
print(re)
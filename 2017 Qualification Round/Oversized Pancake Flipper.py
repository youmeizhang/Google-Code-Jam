#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 17:38:54 2019

@author: yumi.zhang
"""

def flipper(s, k):
    s=s.replace('-','1').replace('+','0')
    
    i = s.find("1")
    if i == -1:
        return 0
        
    count = 0
    while i < len(s)-k:
        if s[i] == "1":
            former = s[:i]
            latter = s[i+k:]
            tmp = s[i:i+k].replace("1", "+").replace("0", "-")
            tmp = tmp.replace("+", "0").replace("-", "1")
            s = former + tmp + latter
            count += 1
            
        i = s.find("1")
        if i == -1:
            return count
    
    if i != len(s) - k:
        return "IMPOSSIBLE"
        
    elif i == len(s) - k and s[i:i+k] != "1" * k:
        return "IMPOSSIBLE"

    else:
        return count + 1
      
n=int(input())
for j in range(n):
    s,k=input().split()
    k=int(k)
    
    ans = flipper(s, k)
    print("Case #%d: %s"%(j+1,str(ans)))
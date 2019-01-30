#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:45:28 2019

@author: yumi.zhang
"""

def fillCake(karta):
    row, column = len(karta), len(karta[0])
    row_list = []
    for r in range(row):
        curr = karta[r][0]
        for c in range(column):
            if karta[r][c] != "?":
                curr = karta[r][c]
                for i in range(c):
                    if karta[r][i] == "?":
                        karta[r][i] = curr
                    
            else:
                karta[r][c] = curr
                
        if curr == "?":
            row_list.append(r)
        
        else:
            while(row_list):
                row_l = row_list.pop()
                karta[row_l] = karta[r]
                
    while(row_list):
        row_l = row_list.pop()
        replace_l = row_l
        
        while(karta[replace_l][0] == "?"):
            replace_l -= 1
            
        karta[row_l] = karta[replace_l]
    
    return karta
    
  
for j in range(1, int(input()) + 1):    
    r, c = map(int, input().strip().split())
    
    karta = [list(input()) for _ in range(r)]
    res = fillCake(karta)
    print("Case #%d:"%(j))
    for i in range(len(res)):
        print("".join(res[i]))

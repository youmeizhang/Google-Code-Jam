#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 21:48:43 2019

@author: yumi.zhang
"""

def tidy(number):
    number = [int(a) for a in number]
    for i in range(len(number)-2, -1, -1):
        if number[i] > number[i+1]:
            if number[i] - 1 == 0 and i != 0:
                number[i] = 9
                try:    
                    number[i-1] -= 1
                except:
                    continue
            else:
                number[i] -= 1
            for j in range(i+1, len(number)):
                number[j] = 9
        else:
            continue
        
    return "".join(str(num) for num in number if num)

n=int(input())
for j in range(n):
    n = input()
    ans = tidy(n)
    
    print("Case #%d: %s"%(j+1,ans))

#this is an old version
def tidyNumber(number):
    if len(number) == 1:
        return number
    
    res = ""
    for i in range(len(number) - 1):
        if int(number[i]) > int(number[i+1]):
            if int(number[i]) - 1 != 0:
                if i != 0 and int(number[i]) == int(number[i-1]):
                    while(number[i] == number[i-1] and i > 1):
                        i -= 1
                    if i == 1 and number[i-1] == number[i]:
                        res = str(int(number[i-1]) - 1)
                        res += "9" * (len(number[i:]))
                        return res
                    
                    else:
                        res = number[:i]
                        res += str(int(number[i]) - 1)                    
                        res += "9" * (len(number[i+1:]))
                        return res
                else:
                    res += str(int(number[i]) - 1)
                    res += "9" * (len(number[i+1:]))
                    return res
            else:
                res = "9" * (len(number) - 1)
                return res
                
        else:
            res += number[i]
    


    res += number[-1]
    return res

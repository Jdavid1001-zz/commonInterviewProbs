# -*- coding: utf-8 -*-

def combine(inStr):
    outStr = ""
    doCombine(inStr, outStr, 0)

def doCombine(inStr, outStr, start):
    #global outStr
    l = len(inStr)
    for i in range(start, l):
        outStr = outStr + inStr[i]
        print outStr
        if i < l - 1:
            doCombine(inStr, outStr, i + 1)
        outStr = outStr[:-1]
        
combine("wxyz")


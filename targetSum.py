# -*- coding: utf-8 -*-
"""
Given an array of integers and a target integer sum, return whether there exist a pair of integers in the array which add up to sum.

See if you can come up with an O(n^2) solution first. Then—can you come up with an O(n log n) one?
"""

def targetSumNaive(arrayInts, targetNum):
    for eachNum in xrange(len(arrayInts)):
        for otherNum in xrange(len(arrayInts)):
            if eachNum != otherNum:
                if arrayInts[eachNum] + arrayInts[otherNum] == targetNum:
                    return True
                    

def targetSumSorted(arrayInts, targetNum):
    pass
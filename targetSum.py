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
    return False
                    

def targetSumSorted(arrayInts, targetNum):
    arrayInts = sorted(arrayInts)
    leftIndex = 0
    rightIndex = len(arrayInts) - 1
    while(leftIndex < rightIndex):
        currentSum = arrayInts[leftIndex] + arrayInts[rightIndex]
        if currentSum < targetNum:
            leftIndex += 1
        elif currentSum > targetNum:
            rightIndex -= 1
        else:
            return True
    return False


def hasTargetSum(arrayInts, targetNum):
    return targetSumNaive(arrayInts, targetNum)
    
def randomArray(arraySize):
    import random
    return [random.randint(0, 50) for x in xrange(arraySize)]

def assertTargetSums(arrayInts, targetNum):
    assert targetSumNaive(arrayInts, targetNum) == targetSumSorted(arrayInts, targetNum)

for x in xrange(25):
    assertTargetSums(randomArray(x * 3), x)
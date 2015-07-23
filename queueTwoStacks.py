# -*- coding: utf-8 -*-
"""
Write a queue using two stacks.

Challenge: can you write it in a way that causes, average-case, O(1) stack operations per enqueue and dequeue?
"""
from collections import deque #closest to a stack
class StackImpl:
    """
    Stack implemented by using deque. 
    
    Python's deque class has closest time complexity to a stack for its
    operations    
    """
    def __init__(self):
        self.innerDeque = deque([])
    
    def pop(self):
        return self.innerDeque.pop()
    
    def push(self, intVal):
        self.innerDeque.append(intVal)

class NaiveQueue:
    def __init__(self):
        self.stackA = StackImpl()
        self.stackB = StackImpl()
        
    def push(self, intVal):
        self.stackA.push(intVal)
        
    def emptyStackIntoOtherStack(stack1, stack2):
        while True:
            try:
                stack2.push(stack1.pop())
            except IndexError:
                return stack1, stack2
        
    def pop(self):
        stackA, stackB = self.emptyStackIntoOtherStack(self.stackA, self.stackB)
        returnVal = stackB.pop()
        self.stackA, self.stackB = self.emptyStackIntoOtherStack(stackA, stackB)
        return returnVal
                
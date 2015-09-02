# -*- coding: utf-8 -*-

#warm-up nums

def sleep_in(weekday, vacation):
 return not weekday or vacation  


def monkey_trouble(a_smile, b_smile):
 return not (a_smile ^ b_smile) 
 
def sum_double(a, b):
 sum = (a + b)
 if a == b:
  return 2 * sum
 else:
  return sum
  
#warm-up string
def hello_name(name):
  return "Hello" + " " + name + "!"  
  
def string_times(str, n):
  return str * n

def front_times(str, n):
  frontLen = 3
  front = ""
  if len(str) < frontLen:
    front = str
  else:
    front = str[:frontLen]
  return front * n

def given_front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result = result + front
  return result

def string_bits(str):
  returnStr = ""
  for i in xrange(0, len(str), 2):
    returnStr += str[i]
  return returnStr
  
def make_tags(tag, word):
  leftTag = "<" + tag + ">"
  rightTag = "</" + tag + ">"
  return leftTag + word + rightTag

def reverseOrder(a, b):
  return b + a
def make_abba(a, b):
  front = a + b
  back = reverseOrder(a, b)
  return front + back
    
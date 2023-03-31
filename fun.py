#!/usr/bin/env python3
import random
x=9
print(x, hex(id(x)))
def fun1(x=x):
  print(x, hex(id(x)))
  x=100
  print(x, hex(id(x)))
  return x
def test_list(ll):
  print(ll, hex(id(ll)))
  ll.append('punn')
  print(ll, hex(id(ll)))
def dic_test(d1):  
  print(random.random())
  numstr=str(random.random()).replace('.','')
  key="hello_"+numstr[1:len(numstr):2]
  d1[key]=1
  print(d1, hex(id(d1)))

  
x=1111
print(x, hex(id(x)))
x=fun1()
print(x, hex(id(x)))
list1=[1,2,3,4,'kamal']
print(list1, hex(id(list1)))
test_list(list1)
print(list1, hex(id(list1)))
d={}
print(d, hex(id(d)))
dic_test(d)
print(d, hex(id(d)))


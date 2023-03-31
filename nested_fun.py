#!/usr/bin/env python3
def outer(x):
  def inner(y):
    print(x+y)
  print("inner address=%d" %(id(inner)))
  return inner

kp1=outer(10)
print("inner address outside function=%d" %(id(kp1)))
kp1(20)

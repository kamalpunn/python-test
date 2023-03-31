#!/usr/bin/env python3
def x(a):
  def y(b):
    return b+a
  return y
kp=x(10)    
print(kp(20))
print(kp(30))
print(kp(40))
print(kp(50))

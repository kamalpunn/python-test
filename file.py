#!/usr/bin/env python3
#file1
inf=open('triangle.py')
for i in inf.read().split('\n'):
  print(i)
for i in open('triangle.py'):
  print(i.rstrip())

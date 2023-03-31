#!/usr/bin/env python3
x=10
name="kamala rani"
ls=range(1,100,10)
def print_ls(ls):
  for i in ls:
   print("%010d"%(i),end="****\n")

x=10
mylist=[1,2,3,4,5]
def value_int(y):
  x=y*70
  print(x)
  y=x
def value_test(x):
  for i in x:
     x[i-1]=i*2
  x[1]=111
  print(x)
if __name__ == '__main__':
   value_test(mylist)
   value_int(x)
   print_ls(ls)
   print(mylist)
   print(x)
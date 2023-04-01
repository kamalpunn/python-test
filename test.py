#!/usr/bin/env python3
#test
#test1
import re
inf=open('ip-list.txt')
l=inf.readlines()
id1=1
for line in l:
    print("Hostname-%d belongs to %s" % ( id1, line.rstrip() ))
    id1+=1
ips={}
for line in l:
    line=line.rstrip()
    tmp=line.split('.')[0:3]
    str='.'.join(tmp)
    if str not in ips.keys():
        ips[str]=1
print(list(ips.keys()))
d={}
for line in l:
   line=line.rstrip()
   res=re.match("(\d{1,3}\.\d{1,3}\.\d{1,3})(.*)",line)
   if res.group(1) not in d.keys():
     d[res.group(1)]=1
print(list(d.keys()))

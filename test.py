#!/usr/bin/env python3
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

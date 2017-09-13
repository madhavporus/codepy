# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 12:24:43 2017

Spyder Editor

In thi editor code between the block #%% and #%% is a block and it can be executed by Ctrl+b

@author: madhavareddy
"""

#%%
# Compare the Ribbon Items. get the ribbon items from https://nightly-dot-netdesign-demo.googleplex.com/admin/ribbon/
def ribbon():
    st1 = '/usr/local/google/home/madhavareddy/Desktop/la1.py'
    st2 = '/usr/local/google/home/madhavareddy/Desktop/la2.py'
    st3 = '/usr/local/google/home/madhavareddy/Desktop/la3.py'
    st4 = '/usr/local/google/home/madhavareddy/Desktop/la4.py'
    
    s1 = open(st1, 'r')
    d1 = open(st2, 'w')
    for lines in s1:
        x = lines.find('label:')
        y = lines[x:]
        d1.write(y)
    s1.close()
    d1.close()
    
    s2 = open(st2, 'r')
    d2 = open(st3, 'w')
    for lines in s2:
        k1 = lines.find(':')
        h1 = k1+2
        i = lines[h1:]
        d2.write(i+"\n")
    s2.close()
    d2.close()
   
    s3 = open(st3, 'r')
    d3 = open(st4, 'w')
    for lines in s3:
        h3 = lines.find('\n')
        i3 = lines[:h3]
        #print(i3, end=" ")
        #print(item, end=" ")
        if i3.strip():
            d3.write(i3+'\n')            
        #print(i3)
    s3.close()
    d3.close()
    
    
ribbon()

#%%
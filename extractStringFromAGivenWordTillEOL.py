# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Spyder Editor

In thi editor code between the block #%% and #%% is a block and it can be executed by Ctrl+b

This is a temporary script file.
"""




#%%
def senddata():
    st2 = '/usr/local/google/home/madhavareddy/Desktop/test4.py'    
    st3 = '/usr/local/google/home/madhavareddy/Desktop/test5.txt'
    ss = open(st2, 'r')
    sss = open(st3, 'w')
    for lines in ss:
       fl = lines.find('SN:')
       x = lines[fl:]
       sss.write(x)
    sss.close()
    ss.close()          
       #print(x)
    st4 = '/usr/local/google/home/madhavareddy/Desktop/test6.py'    
    sss = open(st3, 'r')
    ss = open(st4, 'w')
    for lines in sss:
        fll = lines.find(':')
        g = fll + 2
        y = lines[g:]
        ss.write(y)
        print(y)
    sss.close()
    ss.close()
    
    st4 = '/usr/local/google/home/madhavareddy/Desktop/test6.py'  
    st5 = '/usr/local/google/home/madhavareddy/Desktop/test7.py'    
    
    s4 = open(st4, 'r')
    s5 = open(st5, 'w')
    for lines in s4:
        f2l = lines.find('N/A')
        z = lines[:f2l]
        s5.write(z+'\n') # Writing each entry in a new line.
        print(z)
       #return(x)
    s4.close()
    s5.close()

senddata()


#%%

'''
NOTES: HOW TO USE THE ABOVE SCRIPT

Update the test result in the below sheet:
https://docs.google.com/spreadsheets/d/14E9jf2kTjuGN-75cbMlYTgGyrZBfyySgx_PTovzd80Y/edit#gid=1307837342

If you are to verify any record,. First make sure you run the hardware

Run the hardware import job:
    https://netdesign-staging.googleplex.com/import/hardware/CISCOXR/
Status:
    https://screenshot.googleplex.com/BEH7U0H0hGf

--- 
Helper script to extract all SNs from a gRancid unstructured file:

STEPS:

#1:
Go to gRancid page:
https://screenshot.googleplex.com/FCduREYSc4n

#2
Click on the record you want to take records and check in DH, if all records exist:
Ex: ec15.dfw25

#3
Search with the word ‘inventory’. You will see 2 portions with ‘admin show inventory’ and ‘show inventory’

#4:
Select all the content from these 2 portions and copy.
    https://screenshot.googleplex.com/5pEYszfRDPr

#5:
Paste the copied content in a file name ‘test4.py’ and save it on ‘Desktop’
'/usr/local/google/home/madhavareddy/Desktop/test4.py' 
#6:
Create a blank file with name ‘test5.py’ and save it on desktop
'/usr/local/google/home/madhavareddy/Desktop/test5.txt'

#7:
Create another file with name ‘test6.py’ and save it on ‘Desktop’ as below
'/usr/local/google/home/madhavareddy/Desktop/test6.py' 

#8:
Create another file with name ‘test7.py’ and save it on ‘Desktop’ as below
'/usr/local/google/home/madhavareddy/Desktop/test7.py'

Now, run the ABOVE python code and get the output from ‘test7.py’ file

Finally go get the data for the device from DH and compare: 
https://netdesign-staging.googleplex.com/baseinfra/discovered/#juniper
'''


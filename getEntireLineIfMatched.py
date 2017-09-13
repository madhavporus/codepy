# -*- coding: utf-8 -*-
'''
Spyder Editor

In thi editor code between the block #%% and #%% is a block and it can be executed by Ctrl+b
'''

#%%
def senddata():
    st2 = '/usr/local/google/home/madhavareddy/Desktop/test4.py'    
    st3 = '/usr/local/google/home/madhavareddy/Desktop/test5.txt'
    ss = open(st2, 'r')
    sss = open(st3, 'w')
    for lines in ss:
       fl = lines.find('Poorna:')
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
def findStr():
    st2 = '/usr/local/google/home/madhavareddy/Desktop/test4.py'   
    err_occur = []                         # The list where we will store results.
    substr = "Poorna:"                        # Substring to use for search.
    try:                              # Try to:
        with open (st2, 'rt') as in_file:        # open file for reading text.
            for linenum, line in enumerate(in_file):    # Keep track of line numbers
                if line.lower().find(substr) != -1: #If case-insensitive substring search matches, then:
                    err_occur.append((linenum, line.rstrip('\n'))) # strip linebreaks, store line and line number in list as tuple.
                    for linenum, line in err_occur:              # Iterate over the list of tuples, an
                        print("Line ", linenum, ": ", line)  # print results as "Line [linenum]: [line]".
#%%
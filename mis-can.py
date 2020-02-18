# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 20:41:44 2020

@author: Akshat
"""

flag = "true"
dict=[]

def trans(ML,CL,MR,CR):
    global flag
    if (ML < 0 or CL < 0 or MR < 0 or CR < 0):
        return False
    if ((ML and CL > ML) or (MR and CR > MR)):
        return False

    if (flag=="false" and ML == 0 and CL == 0 or (flag=="false" and MR == 0 and CR == 0)):
        return True

    if (flag=="false") :
        sr=[ML,CL,MR,CR,"left"]
    else:
        sr=[MR,CR,ML,CL,"right"]

    st= str(sr)
    for i in dict:
        if (i == st):
            return False

    dict.append(st);
    if flag=="true":
        flag = "false"
    else:
        flag = "true"

    if (trans(MR + 2, CR, ML - 2, CL)==True):
        print("2,0",'\n')
        print(sr, '\n')
        return True

    elif (trans(MR, CR + 2, ML, CL - 2)):
        print("0,2", '\n')
        print(sr, '\n')
        return True

    elif (trans(MR + 1, CR + 1, ML - 1, CL - 1)):
        print("1,1", '\n')
        print(sr, '\n')
        return True

    elif (trans(MR + 1, CR, ML - 1, CL)):
        print("1,0", '\n')
        print(sr, '\n')
        return True

    elif (trans(MR, CR+1, ML, CL-1)):
        print("0,1", '\n')
        print(sr, '\n')
        return True

    if flag=="true":
        flag = "false"
    else:
        flag = "true"
    dict.pop()
    return False

ML = 3
CL = 3
MR = 0
CR = 0
FY= [ML,CL,MR,CR,"left"]
if (trans(ML, CL, 0, 0)== False):
    print(" NO Solution Found!")
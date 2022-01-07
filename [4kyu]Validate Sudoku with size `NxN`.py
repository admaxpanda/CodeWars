'''
Given a Sudoku data structure with size NxN, N > 0 and √N == integer, 
write a method to validate if it has been filled out correctly.
'''

import math
from typing import Type
class Sudoku(object):
    def __init__(self, data):
        self.data=data
        
                
    def is_valid(self):
        data=self.data
        n=len(data)
        if n==0:
            return False
        if len(data[-1])!=n:
            return False
        
        if n==1:
            if type(data[0][0])==type(1) and data[0][0] ==1:
                return True
            else:
                return False
            

        sn=int(math.sqrt(n))
        
        #行列
        for i in range(n):
            tmp=set()
            tmp1=set()
            for k in range(n):
                if data[i][k] in tmp or data[i][k]>n or data[i][k]<1:
                    return False
                else:
                    tmp.add(data[i][k])
                if data[k][i] in tmp1 or data[k][i]>n or data[k][i]<1:
                    return False
                else:
                    tmp1.add(data[k][i])
            if(len(tmp)!=n or len(tmp1)!=n):
                return False
        #方格
        #外层区块->内层方格
        for i in range(sn):
            for k in range(sn):
                tmp=set()
                for ii in range(sn):
                    for kk in range(sn):
                        if data[i*sn+ii][k*sn+kk] in tmp or data[i*sn+ii][k*sn+kk]>n or data[i*sn+ii][k*sn+kk]<1:
                            return False
                        else:
                            tmp.add(data[i*sn+ii][k*sn+kk])
                if(len(tmp)!=n):
                    return False
        return True

if(__name__=='__main__'):
    a=Sudoku(data=[
    [True]
    ])
    print(a.is_valid())
    #print(type(True),type(1))

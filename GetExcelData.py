#file: GetExcelData.py
import global_vars
from os import read
from os import path
#import tkinter as tk
#from tkinter import filedialog as fd
import numpy as np
import pandas as pd
import re


def colJoin(xHeader): return ';'.join(xHeader[xHeader.notnull()].astype(str))

def filterInputFile(InputFileFullPath):
    #irow = 0
    f = open(global_vars.OutputFile, "a")
    if path.isfile(InputFileFullPath):
        df = pd.read_csv(InputFileFullPath, names=global_vars.ConfigHeader)
        print(global_vars.ConfigHeader)
        print (df.shape[0])
        for val in pd.read_csv(InputFileFullPath, names=global_vars.ConfigHeader): #, nrows=1):
            #print('len of DataFrame: ' + len(df.size))
            if val == "Labels" or val == "Component/s":
                df.groupby(level=0, axis=1).apply(lambda val: val.apply(colJoin, axis=1))
            val = re.sub("\Σ", "Sum of", val)
            #if irow == 1: 
            #    print('iloc[0] = %s \nindex[-1] = %s' %(pd.read_csv(InputFileFullPath).iloc[0], pd.read_csv(InputFileFullPath).index[-1]))
            #irow = irow+1
            f.write('Column %d val: %s' %('MyColumn', val))
    else: print('%s file does not exits in path: %s' %(global_vars.OutputFile, InputFileFullPath))
    f.write('\n')
    f.close
    return



    
mHead = pd.DataFrame.head
mNumOfRows = pd.DataFrame.set_index
mTail = pd.DataFrame.tail

    
    
    
    


'''    

xls_header=[]
xls_header[0, "RTT"]
xls_header.append("KSK")
xls_header.append("773")
print(xls_header[0], " - ", xls_header[1], " - ",xls_header[2])
'''


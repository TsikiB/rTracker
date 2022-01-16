import global_vars
from log import *
import os
import config
import tkinter as tk
from tkinter import filedialog as fd

import pandas as pd



EE = writeToFile('Kyku.txt', 'My first Textxxx')

#--- Test func
global_vars.DataFilePath = 'C:/Users/tsikib1/Downloads/rTracker - ALL Content in given date For Test.csv' #Tsiki: line2remove
config.getConfigHeaders()


InputFileFullPath  = global_vars.DataFilePath #Tsiki: line2remove
df = pd.read_csv(InputFileFullPath, names=global_vars.ConfigHeader)
df.at[1,'Status'] = 'Kuku'
print(df[2:4, 'State'])
print ('Input Rows: %d' %(df.shape[0]))
print('Input Columns: %d' %(df.shape[1]))
#print(df.iloc[2:6])

index_ = list(range(1, df.shape[0]+1))
#print(index_)
df.index = index_

df.loc[2:4]





#--- End of Test Func
iname='Joe'
iage = 42

#print ('%s is %d years old' % ('Joe', 42))
print ('%s is %d years old' % (iname, iage)) 


T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
print(T[0])
print(T[2][1])

myArr = [['Tsiki']]
myArr.extend([['R', 'Y']])
myArr.append ([['R1']])
myArr.append ([['Y1']])
print (myArr)
print (myArr[1])


ROOT_DIR = os.path.dirname(os.path.abspath("tempy.py"))
print (ROOT_DIR)

root = tk.Tk()
root.withdraw()
raw_data_file = fd.askopenfilename(defaultextension='.csv', 
                               filetypes=[("csv", '*.csv'),("Excel","*.xlsx"),("all files","*.*")],
                               title = "Select Data Source")
print (raw_data_file)

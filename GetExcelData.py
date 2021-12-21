from os import read
import configparser
import tkinter as tk
from tkinter import filedialog as fd



root = tk.Tk()
root.withdraw()
raw_data_file = fd.askopenfile(defaultextension='.csv', 
                               filetypes=[("csv", '*.csv'),("Excel","*.xlsx"),("all files","*.*")],
                               title = "Select Data Source")
print (raw_data_file)
xls_header=[]
xls_header[0, "RTT"]
xls_header.append("KSK")
xls_header.append("773")
print(xls_header[0], " - ", xls_header[1], " - ",xls_header[2])



from os import read
import tkinter as tk
from tkinter import filedialog as fd

root = tk.Tk()
root.withdraw()
raw_data_file = fd.askopenfilename(defaultextension='.csv', 
                               filetypes=[("csv", '*.csv'),("Excel","*.xlsx"),("all files","*.*")],
                               title = "Select Data Source")
print (raw_data_file)

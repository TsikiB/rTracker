# rTracker: the Release Tracker App
#file: main.py
import global_vars
import config 
import common
import log
import GetExcelData
import tkinter as tk
from tkinter import filedialog as fd


#--- Set Configuration ---
config.getLogLevel()
if not config.setLogLevel():
    log.log_finish_info()
    quit()
config.getConfigTeams()
config.getConfigTeamMembers()

log.log_start_info()
root = tk.Tk()
root.withdraw()
raw_data_file = fd.askopenfile(defaultextension='.csv', 
                                filetypes=[("csv", '*.csv'),("Excel","*.xlsx"),("all files","*.*")],
                                title = "Select Data Source")
global_vars.DataFilePath = raw_data_file.name
log.LogInfo('DataFilePath: ' + global_vars.DataFilePath)
config.getConfigHeaders()
#print (global_vars.ConfigHeader)
GetExcelData.filterInputFile(global_vars.DataFilePath)


 

log.log_finish_info()

log.setLogLevel()
print('ProjectDir: ' + str(config.ProjectDir))
print('LogFile: ' + config.LogFile)
print ('logLevel : ' + config.logLevel)







log.log_finish_info()

ttmp = common.open_borwser('https://getnada.com')


#Start the routine
UrlInFocus = 'http://www.verifone.com'
common.open_borwser('https://jira.verifone.com/issues/?filter=69651')
#LogInfo('open browser = ' + str(open_borwser('http://www.verifone.com')))
log.LogInfo(UrlInFocus)
log.LogError('Some error text will go in here')

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"--Output--:{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:
    
        user_input_number = int(input_val)
        if user_input_number > 0:
            calculated_value =  days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a positive number")
        else:
            print("you entered a negative value, Can't convert this")
            
    except ValueError:
        print("you input is not a valid value. Follow the rules plaese") 

user_input = ""
while user_input != "exit":
    user_input = input("Enter a value (or 'exit'):\n")
    if user_input == "exit":
        break
    else:
        #user_list = user_input.split(", ")
        #print(f'List:{user_list}\n  Set:{set(user_list)}') 
        for input_val in set(user_input.split(",")):
            input_val = input_val.strip()
            validate_and_execute()

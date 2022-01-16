#file: log.py
from genericpath import isfile
from tkinter.constants import FALSE, TRUE
import global_vars
from datetime import datetime
from os import path as path
import os
from pathlib import Path as PathCheck
import logging
import inspect 
import traceback


def writeToFile(FileName, Text, FilePath='.'):
    if (FilePath == '') or (FilePath == '.'): 
        FilePath = global_vars.ProjectDir
    fileFullPath = PathCheck(str(FilePath) + '\\' + str(FileName))
    f = open(fileFullPath, "a")
    f.write(str(Text)+ '\n')
    f.close
    if not path.isfile(fileFullPath):
        print('%s file does not exits in path: %s' %(FileName, fileFullPath))
        return FALSE
    else: return TRUE
            


def logLine():
    print("%s Ln:%s" % (__file__, inspect.getframeinfo(inspect.currentframe()).lineno))
    print(traceback.print_exception)


def setLogFile():
    try:
        if not os.path.exists(global_vars.LogFile):
            os.mknod(global_vars.LogFile) 
        return True              
    except IOError:
        print(IOError)
    except os.error:
        print(traceback.print_exception)
        print(os.error)
        print("%s Ln:%s" % (__file__, inspect.getframeinfo(inspect.currentframe()).lineno))
        print('Error: ' + IOError)
        return False

def log_start_info():
    try:
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y_%H:%M:%S")
        if os.stat(global_vars.LogFile).st_size > 0:
            file2write = open(global_vars.LogFile, "a")  # append mode  
            file2write.write('\n')
            file2write.close()
        logging.info('>>> rTracker started at: ' + str(date_time))
        return True
    except os.error:
        LogError(os.error)
    
def log_finish_info():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y_%H:%M:%S")
    logging.info('>>> rTracker finished at: ' + str(date_time) + ' <<<')

def LogTerminated(txt_message):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y_%H:%M:%S")
    logging.info(str(date_time) + ': >> TERMINATED << ' + str(txt_message))
    
def LogInfo(txt_message):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y_%H:%M:%S")
    logging.info(str(date_time) + ': ' + str(txt_message))
    
def LogError(txt_message):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y_%H:%M:%S")
    logging.error(str(date_time) + ': ' + str(txt_message))
    

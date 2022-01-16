#file: config.py
import global_vars
import logging
import configparser
import string
import array
import sys
import pathlib
import inspect
import traceback

#--- System Files ---
global_vars.LogFile='rTracker.log'
global_vars.ConfigFile = 'rTrackerConfig.INI'
global_vars.OutputFile = 'Import.txt'

global_vars.ProjectDir=pathlib.Path(global_vars.ConfigFile).parent.resolve()
global_vars.ConfigFullPath = str(str(global_vars.ProjectDir) + '\\' + global_vars.ConfigFile)
#--------------------

#Set configuration parser and arrays
conf = configparser.ConfigParser(allow_no_value=True)
conf.optionxform=str  #Preserve Case from Config File
conf.read(global_vars.ConfigFullPath)

#--- Log level ---
def getLogLevel():
    #global logLevel; logLevel = 'INFO' 
    for val in conf.items('Log'):
        global_vars.logLevel = str.upper(val[1])
        break #only the first valus is taken       
    return global_vars.logLevel

def setLogLevel():
    if global_vars.logLevel == 'DEBUG':
        logging.basicConfig(filename=global_vars.LogFile, encoding='utf-8', level=logging.DEBUG)
        frame = inspect.currentframe()
        stack_trace = traceback.format_stack(frame)
        logging.debug(stack_trace[:-1])
    elif global_vars.logLevel == 'LOG':
        logging.basicConfig(filename=global_vars.LogFile, encoding='utf-8', level=logging.INFO)
        logging.critical(string)
    elif global_vars.logLevel == 'WARNING':
        logging.basicConfig(filename=global_vars.LogFile, encoding='utf-8', level=logging.WARNING)
    else:
        print("Error: Process is terminated. Log level %s is not supported" %global_vars.logLevel)
        logging.basicConfig(filename=global_vars.LogFile, encoding='utf-8', level=logging.ERROR)
        logging.error('Log level %s is not supported' %global_vars.logLevel)
        return False     
    return True          

def getConfigHeaders():
    #global ConfigHeader; ConfigHeader=[]
    pos=0 #ignores index(1) in config may return ',' or '\n' value
    for val in conf.items('Headers'):
        global_vars.ConfigHeader.append(val[pos])
    #print('ConfigHeader: %s' %global_vars.ConfigHeader)

def getConfigTeams(): 
    #global ConfigTeams; ConfigTeams=[]
    for val in conf.items('Teams'):
        global_vars.ConfigTeams.append(val[0])
        global_vars.ConfigTeams.append(val[1])
    #print ('ConfigTeams: %s' %ConfigTeams)
    
def getConfigTeamMembers():
    #global ConfigTeamMemebers; ConfigTeamMemebers = [['Tsiki']] #Position-0
    global_vars.ConfigTeamMemebers = [['Tsiki']] #Position-0
    for i in global_vars.ConfigTeams[0::2]:
        ConfigValues=[]
        for val in conf.items('Team'+i):
            if len(ConfigValues) > 0:
                ConfigValues = ConfigValues + ',' + val[0]
            else: ConfigValues = val[0]
        global_vars.ConfigTeamMemebers.extend([[ConfigValues]])
    #print(ConfigTeamMemebers)
import pathlib
import logging
import configparser

#--- System files ---
LogFile='rTracker.log'
ConfigFile = 'rTrackerConfig.INI'
#--------------------

#Setup the root setup and configuration files
global ProjectDir
ProjectDir=pathlib.Path(ConfigFile).parent.resolve()
global ConfigFullPath
ConfigFullPath = str(str(ProjectDir) + '\\' + ConfigFile)
logging.basicConfig(filename=LogFile, encoding='utf-8', level=logging.DEBUG)


#Upload configurable data
config = configparser.ConfigParser(allow_no_value=True)
config.optionxform=str  #Preserve Case from Config File
config.read(ConfigFullPath)
ConfigHeader=[]
ConfigTeams=[]

def getConfigHeader():
    pos=0 #ignores index(1) in config may return ',' or '\n' value
    ee=0
    for val in config.items('Headers'):
        ConfigHeader.append(val[pos])
        print (ConfigHeader[ee])
        ee = ee+1

def getConfigTeams():
    pos=0 #ignores index(1) in config may return ',' or '\n' value
    for val in config.items('Teams'):
        ConfigTeams.append(val[pos])
import logging
from datetime import datetime



def __init__ (self):
    now = datetime.now() 
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H:%M:%S")
    date_time = now.strftime("%d/%m/%Y, '_' , %H:%M:%S")
    print('>>> rTracker started at ' + datetime(date_time))
    #logging.info('>>> rTracker started at ' + {date_time})
   
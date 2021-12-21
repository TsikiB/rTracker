#Handle the core functions
from datetime import datetime
from typing import KeysView
import tkinter as tk
from tkinter import filedialog as fd
import webbrowser
import logging



#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

def log_start_info():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y_%H:%M:%S")
    logging.info('>>> rTracker started at: ' + str(date_time))


def open_borwser(url):
    try:
        targeturl = 'http://www.cnn.com'
        defaulturl = 'http://google.com'
        webbrowser.get()
        current_page = webbrowser.open(url,1)
        return current_page
    except webbrowser.Error:
        print('Error: ' + webbrowser.Error)
        return False


def out_of_scope():
    webbrowser.get('http://www.yahoo.com')
    assert 'Yahoo' in webbrowser.title

    elem = webbrowser.find_element_by_name('p')  # Find the search box
    elem.send_keys('seleniumhq' + KeysView.RETURN)

    webbrowser.quit()
    
def file_dialog():
    fd.asksaveasfile()
    



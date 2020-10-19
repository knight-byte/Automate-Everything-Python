#!/usr/bin/python

from selenium import webdriver
import sys
import time
import os
from selenium.webdriver.chrome.options import Options

# file_name=sys.argv[0]
img = """ ___                            
|_ _|_ __ ___   __ _  __ _  ___ 
 | || '_ ` _ \ / _` |/ _` |/ _ \\
 | || | | | | | (_| | (_| |  __/
|___|_| |_| |_|\__,_|\__, |\___|
                     |___/      
\t\t ____                      _     
\t\t/ ___|  ___  __ _ _ __ ___| |__  
\t\t\___ \ / _ \/ _` | '__/ __| '_ \ 
\t\t ___) |  __/ (_| | | | (__| | | |
\t\t|____/ \___|\__,_|_|  \___|_| |_|
\t\t\t\t-by KNIGHT-BYTE

"""
print(img)
file = input(
    "-*-*-*-*-*-\nDrag and Drop \nOR\nPaste the full path of the Image\n-*-*-*-*-*-*-\n==>  ")
file_name = os.path.abspath(file)

# path for chromedriver
option = webdriver.ChromeOptions()
option.add_argument('headless')
PATH = os.path.abspath('chromedriver')
driver = webdriver.Chrome(PATH, options=option)
# gettint the URL path
driver.get('https://www.google.co.in/imghp?hl=en&tab=ri&authuser=0&ogbl')

# selecting the Camicon
cam = driver.find_element_by_class_name('LM8x9c')
cam.click()
# selecting the uploadImage option
uploadImage = driver.find_element_by_link_text('Upload an image')
uploadImage.click()

try:
    choose_file = driver.find_element_by_name('encoded_image')
    choose_file.send_keys(file_name)
    url = driver.current_url
    for i in range(101):
        time.sleep(0.05)
        sys.stdout.write("\rloading:%s%s%d%%" %
                         ('='*(i//10), '-'*(10-(i//10)), i))
        sys.stdout.flush()
    browser = webdriver.Chrome(PATH)
    browser.get(url)
except:
    print('File Not Found')
    driver.quit()

print('\nDone Search')

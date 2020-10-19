#!/usr/bin/python
'''
Created by    : Abunachar
Language used : Python3
Editor Used   : Vim
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys
import time

head = """\t\t__   ___     _ _                          
\t\t\ \ / / |   (_) |__  _ __ __ _ _ __ _   _ 
\t\t \ V /| |   | | '_ \| '__/ _` | '__| | | |
\t\t  | | | |___| | |_) | | | (_| | |  | |_| |
\t\t  |_| |_____|_|_.__/|_|  \__,_|_|   \__, |
\t\t                                    |___/ 
\t\t                          -by KNIGHT-BYTE            
"""
print(head)

# book name
bookSearch = input("Enter the Book name : ")
print("Looking for book...")

# path for chromeDriver
option = webdriver.ChromeOptions()
option.add_argument('headless')
PATH = os.path.abspath('chromedriver')
driver = webdriver.Chrome(PATH, options=option)

# getting the URL path
driver.get('https://b-ok.asia/')

#Search in library
search_bar = driver.find_element_by_id('searchFieldx')
search_bar.send_keys(bookSearch)

searchButton = driver.find_element_by_class_name("button")
searchButton.click()

# Total books found
TB = driver.find_elements_by_id('subprojectsSearch')[0]
tot = TB.text[:12]
totalBooks = int(tot.split('(')[1].split(')')[0][:3])
print("\n", totalBooks, 'result found!\n')


# function for getting the Chrome download rate hai and progress report
def get_download_progress():
    progress = driver.execute_script('''
    
    var tag = document.querySelector('downloads-manager').shadowRoot;
    var intag = tag.querySelector('downloads-item').shadowRoot;
    var progress_tag = intag.getElementById('progress');
    var progress = null;
    if(progress_tag) {
        progress = progress_tag.value;
    }
    var rate_tag = intag.getElementById('description');
    var rate = null;
    if(rate_tag) {
        rate = rate_tag.textContent;
    }
    return [progress,rate];   
    ''')
    return [progress[0], progress[1]]


# Download Function
def DownloadFunction():
    try:
        time.sleep(3)

        # greeting the Chrome download URL
        driver.get('chrome://downloads/')

        # default progress percentage
        progress = 0

        # looping till progress is 100%
        while progress <= 100:

            progress = get_download_progress()[0]
            rate = str(get_download_progress()[1])
            time.sleep(0.08)

            sys.stdout.write("\rDownloading: [%s%s]%d%%%s" %
                             ('='*(progress//5), '-'*(20-(progress//5)), progress, rate[1:len(rate)-2].split(',')[0]))
            sys.stdout.flush()

            # if any error occur in downloading then
            if rate == None or len(rate) == 12:
                print("Error while downloading the book")
                break
        print("Download Comleted check the default download location")
    except:
        print("Unable to download or You have already Downloaded 5 book in 24hr")


# Number of Options to Show to the User
x = (5 if totalBooks >= 10 else totalBooks)
items = driver.find_elements_by_class_name('resItemTable')

# Looping through all the Books available
for item in range(totalBooks):
    if item >= x:

        # options to perform
        choose = input('''Select Option to perform
---------------------------
d: Download 
n: Next page
q: Quit 
--> ''')
        if choose.lower() == 'd':
            try:
                inp = input("select the No. of the book to download : ")
                items[int(inp)].find_elements_by_tag_name('a')[1].click()
            except:
                print('Invalid selection : (')
                driver.quit()
                break

            driver.find_element_by_class_name('dlButton').click()
            DownloadFunction()
            break
        elif choose.lower() == 'n':
            x += 5
        elif choose.lower() == 'q':
            driver.quit()
            print("BYE :)")
            break
        else:
            print('Invalid Input :( ')
            continue

    title = items[item].find_elements_by_tag_name('a')[1]
    author = items[item].find_element_by_class_name("authors")
    print('[ '+str(item+1)+' ] '+title.text+"\n- by " + author.text+"\n")

print(''' _                      __  
| |__  _   _  ___    _  \ \ 
| '_ \| | | |/ _ \  (_)  | |
| |_) | |_| |  __/   _   | |
|_.__/ \__, |\___|  (_)  | |
       |___/            /_/ 

''')

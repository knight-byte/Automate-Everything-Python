#!/usr/bin/python
'''
Created by    : Abunachar
Language used : Python3
Editor Used   : Vim
'''

import pip
from os import system, name
from time import sleep


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def install(packages):
    print("Checking Requirements...")
    for package in packages:
        if hasattr(pip, 'main'):
            pip.main(['install', package])
        else:
            pip._internal.main(['install', package])

    sleep(2)
    clear()

req_list = ['beautifulsoup4', 'tqdm', 'bs4', 'lxml', 'requests']
install(req_list)

from tqdm import tqdm
from bs4 import BeautifulSoup
import requests

def download_book(book_url):
    try:
        inp = int(input("select the No. of the book to download : "))
        book_req = requests.get(f'https://b-ok.asia/{book_url[inp-1]}').text
        book_soup = BeautifulSoup(book_req, 'lxml')
        b_url = book_soup.find(class_='dlButton')['href']
        name = book_soup.h1.text.strip()
        extension = book_soup.find(class_='dlButton').text.strip()
        extension = extension.split('(')
        extension = extension[1].split(',')[0].strip()
        # print(b_url, extension)

        response = requests.get(f'https://b-ok.asia/{b_url}', stream=True)
        total_size_in_bytes = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte
        progress_bar = tqdm(total=total_size_in_bytes,
                            unit='iB', unit_scale=True)
        with open(f"{name}.{extension}", 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
        progress_bar.close()
        if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
            print("ERROR, something went wrong")

    except Exception as e:
        print(f"{e}ERROR, something went wrong")

    finally:
        print(''' _                      __
| |__  _   _  ___    _  \ \
| '_ \| | | |/ _ \  (_)  | |
| |_) | |_| |  __/   _   | |
|_.__/ \__, |\___|  (_)  | |
       |___/            /_/

''')
    exit()


def main():

    head = """\t\t__   ___     _ _
    \t\t\ \ / / |   (_) |__  _ __ __ _ _ __ _   _
    \t\t \ V /| |   | | '_ \| '__/ _` | '__| | | |
    \t\t  | | | |___| | |_) | | | (_| | |  | |_| |
    \t\t  |_| |_____|_|_.__/|_|  \__,_|_|   \__, |
    \t\t                                    |___/  v2.0
    \t\t                          -by KNIGHT-BYTE
    """
    print(head)
    # book name
    bookSearch = input("Enter the Book name : ")
    print("Looking for book...")

    source = requests.get(f'https://b-ok.asia/s/{bookSearch}').text
    soup = BeautifulSoup(source, 'lxml')
    books_url = []
    for i, single_book in enumerate(soup.find_all(class_='resItemTable')):
        book_name = single_book.h3.a.text
        author_name = ", ".join([n.text for n in single_book.find(
            class_='authors').find_all('a')])
        url_links = single_book.h3.a['href']
        books_url.append(url_links)
        print(f"[{i+1}] {book_name}\n\t- By {author_name}\n")
        while (i+1) % 7 == 0:
            choose = input('''Select Option to perform
    ---------------------------
    d: Download
    n: Next page
    q: Quit
    --> ''')
            if choose.lower() == 'd':
                download_book(books_url)
                break
            elif choose.lower() == 'n':
                break
            elif choose.lower() == 'q':
                print('Bye :)')
                exit()

    exit()


if __name__ == "__main__":
    main()

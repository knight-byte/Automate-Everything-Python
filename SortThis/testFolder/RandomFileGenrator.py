import os

from random import randint
extension = ['png', 'jpg', 'jpeg', 'bmp', 'tiff',
             'psd', 'ai', 'raw', 'svg', 'gif', 'icon', 'mp4', 'flv', 'mkv',
             'mov', 'wmv', 'flv', 'avi', 'webm', 'm4a', 'mp3', 'flac', 'wav',
             'wma', 'aac', 'ppt', 'doc', 'pptx', 'docx', 'pdf', 'txt', 'xls',
             'xlsx', 'py', 'ipynb', 'java', 'jar', 'class', 'css',
             'html', 'xhtml', 'scss', 'c', 'cpp', 'cxx', 'js',
             'xml', 'json', 'cvs', 'exe', 'bat', 'sh', 'zip', 'rar', 'bz2', '7z', 'gz', 'tar']

path = os.getcwd()
no_of_file=int('Enter the no of File ro generate : ')
for i in range(no_of_file):
    x = randint(0, len(extension)-1)
    with open(os.path.join(path, str(i)+'.'+extension[x]), 'w') as fp:
        pass

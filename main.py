import os
import re
from readfile import readFile

with os.scandir('./tests') as entries:
    for entry in entries:
        with open(entry, 'r',encoding='utf8') as file:
            automovel = readFile(file)
            print(automovel['motor'])
           



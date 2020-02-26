import os
import re
from readfile import readFile
from automovel import Automovel

lojaCarros = []
with os.scandir('./tests') as entries:
    for entry in entries:
        with open(entry, 'r',encoding='utf8') as file:
            automovel = readFile(file)
            result = Automovel(automovel)
            lojaCarros.append(result)
print(lojaCarros[0].nome)
           



import os
import re
from readfile import readFile
from automovel import Automovel

import pandas as pd
import matplotlib.pyplot as plt

lojaCarros = []
with os.scandir('./tests') as entries:
    for entry in entries:
        with open(entry, 'r',encoding='utf8') as file:
            automovel = readFile(file)
            result = Automovel(automovel)
            lojaCarros.append(result)


df = pd.DataFrame({
    'nome':[lojaCarros[0].nome,lojaCarros[1].nome,lojaCarros[2].nome,lojaCarros[3].nome,lojaCarros[4].nome,lojaCarros[5].nome,lojaCarros[6].nome,lojaCarros[7].nome,lojaCarros[8].nome,lojaCarros[9].nome,lojaCarros[10].nome,lojaCarros[11].nome,lojaCarros[12].nome, lojaCarros[13].nome,lojaCarros[14].nome],
    'ano':[lojaCarros[0].ano,lojaCarros[1].ano,lojaCarros[2].ano,lojaCarros[3].ano,lojaCarros[4].ano,lojaCarros[5].ano,lojaCarros[6].ano,lojaCarros[7].ano,lojaCarros[8].ano,lojaCarros[9].ano,lojaCarros[10].ano,lojaCarros[11].ano,lojaCarros[12].ano, lojaCarros[13].ano,lojaCarros[14].ano],
    'cor':[lojaCarros[0].cor,lojaCarros[1].cor,lojaCarros[2].cor,lojaCarros[3].cor,lojaCarros[4].cor,lojaCarros[5].cor,lojaCarros[6].cor,lojaCarros[7].cor,lojaCarros[8].cor,lojaCarros[9].cor,lojaCarros[10].cor,lojaCarros[11].cor,lojaCarros[12].cor, lojaCarros[13].cor,lojaCarros[14].cor],
    'motor':[lojaCarros[0].motor,lojaCarros[1].motor,lojaCarros[2].motor,lojaCarros[3].motor,lojaCarros[4].motor,lojaCarros[5].motor,lojaCarros[6].motor,lojaCarros[7].motor,lojaCarros[8].motor,lojaCarros[9].motor,lojaCarros[10].motor,lojaCarros[11].motor,lojaCarros[12].motor, lojaCarros[13].motor,lojaCarros[14].motor],
    'km':[lojaCarros[0].km,lojaCarros[1].km,lojaCarros[2].km,lojaCarros[3].km,lojaCarros[4].km,lojaCarros[5].km,lojaCarros[6].km,lojaCarros[7].km,lojaCarros[8].km,lojaCarros[9].km,lojaCarros[10].km,lojaCarros[11].km,lojaCarros[12].km, lojaCarros[13].km,lojaCarros[14].km],
})




df.plot(kind='scatter',x='ano',y='nome',color='red')
plt.show()

df.groupby('cor')['nome'].nunique().plot(kind='bar')
plt.show()

df.groupby(['cor','motor']).size().unstack().plot(kind='bar',stacked=True)
plt.show()


df = pd.DataFrame({
    'km':[lojaCarros[0].km,lojaCarros[1].km,lojaCarros[2].km,lojaCarros[3].km,lojaCarros[4].km,lojaCarros[5].km,lojaCarros[6].km,lojaCarros[7].km,lojaCarros[8].km,lojaCarros[9].km,lojaCarros[10].km,lojaCarros[11].km,lojaCarros[12].km, lojaCarros[13].km,lojaCarros[14].km],
})
df=df.astype(int)

df[['km']].plot(kind='hist',rwidth=0.8)
plt.show()
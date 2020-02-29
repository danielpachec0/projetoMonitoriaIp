import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Carro import Carro


def read1(nome):
    arq = open(nome, "r")
    l = arq.readlines()
    modelo = l[0]
    ano = l[3]
    km = l[5]
    cor = l[7]
    # print(l[8])
    if l[8][:6] == "PORTAS":
        val = l[10]
        # print(val)
        aux = l[11].split()
        comb = aux[3]
        motor = aux[9]
        camb = aux[11]
    else:
        val = l[8]
        # print(val)
        aux = l[9].split()
        comb = aux[3]
        motor = aux[9]
        camb = aux[11]
    arq.close()
    if nome == "data/test2.txt":
        aux = ano
        ano = km
        km = aux
    modelo = modelo.strip('\n')
    marca = modelo.split()[0]
    marca = marca.lower()
    cor = cor.strip('\n')
    ano = ano.strip('\n')
    motor = motor.strip('\n')
    motor = float(motor)
    comb = comb.strip('\n')
    val = val.strip('\n')
    val = val.strip("R$ ")
    val = val[:-3]
    val = val.replace(".", "")
    val = int(val)
    km = km.strip('\n')
    km = int(km)
    camb = camb.strip('\n')
    carro = Carro(modelo, marca, ano, km, val, motor, camb, comb, cor)
    return carro


def read2(nome):
    arq = open(nome, "r")
    l = arq.readlines()
    for i in range(len(l)):
        if l[i][:6] == 'Modelo':
            modelo = l[i + 1]
        elif l[i][:5] == 'Marca':
            marca = l[i + 1]
        elif l[i][:3] == 'Ano':
            ano = l[i + 1]
        elif l[i][:13] == 'Quilometragem':
            km = l[i + 1]
        elif l[i][:3] == 'Cor':
            cor = l[i + 1]
        elif l[i][:6] == 'Câmbio':
            camb = l[i + 1]
        elif l[i][:11] == 'Combustível':
            comb = l[i + 1]
        elif l[i][:8] == 'Potência':
            motor = l[i + 1]
    arq.close()
    modelo = modelo.strip('\n')
    modelo = modelo.replace("GM - CHEVROLET", "Chevrolet")
    marca = marca.strip('\n')
    marca = marca.replace("GM - CHEVROLET", "Chevrolet")
    marca = marca.lower()
    cor = cor.strip('\n')
    ano = ano.strip('\n')
    motor = motor.strip('\n')
    motor = float(motor)
    comb = comb.strip('\n')
    km = km.strip('\n')
    km = int(km)
    camb = camb.strip('\n')
    carro = Carro(modelo, marca, ano, km, "nan", motor, camb, comb, cor)
    return carro


arquivos1 = ["test1.txt", "test2.txt", "test3.txt", "test4.txt", "test5.txt", "test13.txt", "test14.txt", "test15.txt"]
arquivos2 = ["test6.txt", "test7.txt", "test8.txt", "test9.txt", "test10.txt", "test11.txt", "test12.txt"]

carros = []

for i in arquivos1:
    aux = "data/" + i
    carros.append(read1(aux))

for i in arquivos2:
    aux = "data/" + i
    carros.append(read2(aux))

df = pd.DataFrame({"Marca": [],
                   "Modelo": [],
                   "Ano": [],
                   "Kilometragem": [],
                   "Valor": [],
                   "Potencia do motor": [],
                   "Transmissão": [],
                   "Combustivel": [],
                   "Cor": []})

for i in carros:
    df = df.append(i.creat_serie(), ignore_index=True)

# --------------------------------------------------------------------------

qnt_cor = df["Cor"].value_counts().values
nome_cor = df["Cor"].value_counts().index
plt.pie(qnt_cor, labels=list(nome_cor))
plt.show()

# --------------------------------------------------------------------------

x = list(df["Modelo"])
aux2 = 0
for i in range(len(x)):
    aux = x[i].split()[1]
    if aux in x:
        aux = aux + str(aux2)
        aux2 = aux2+1
    x[i] = aux
y = df["Potencia do motor"]
plt.xticks(rotation=90)
plt.bar(x, y)
plt.show()

# --------------------------------------------------------------------------

x = list(df["Modelo"][df["Valor"] != "nan"])
aux2 = 0
for i in range(len(x)):
    aux = x[i].split()[1]
    if aux in x:
        aux = aux + str(aux2)
        aux2 = aux2+1
    x[i] = aux
y = df["Valor"][df["Valor"] != "nan"]
plt.xticks(rotation=90, )
plt.scatter(x, y)
plt.show()

# --------------------------------------------------------------------------

df.hist(column="Kilometragem")
plt.show()

# --------------------------------------------------------------------------

x = df["Marca"].value_counts().index
y = df["Marca"].value_counts().values
plt.xticks(rotation=90, )
plt.bar(x, y)
plt.show()


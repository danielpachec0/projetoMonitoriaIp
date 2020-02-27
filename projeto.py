import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Carro import Carro

arquivos1 = ["test1.txt", "test2.txt", "test3.txt", "test4.txt", "test5.txt", "test13.txt", "test14.txt", "test15.txt"]
arquivos2 = ["test6.txt", "test7.txt", "test8.txt", "test9.txt", "test10.txt", "test11.txt", "test12.txt"]

def read1(nome):
    arq = open(nome, "r")
    l = arq.readlines()
    modelo = l[0]
    ano = l[3]
    km = l[5]
    cor = l[7]
    #print(l[8])
    if l[8][:6] == "PORTAS":
        val = l[10]
        #print(val)
        aux = l[11].split()
        comb = aux[3]
        motor = aux[9]
        tran = aux[11]
    else:
        val = l[8]
        #print(val)
        aux = l[9].split()
        comb = aux[3]
        motor = aux[9]
        tran = aux[11]
    arq.close()
    carro = Carro(modelo, modelo[0], ano, km, val, motor, tran, comb, cor)
    return carro

def read2(nome):
    arq = open(nome, "r")
    l = arq.readlines()
    for i in range(len(l)):
        if l[i][:6] == 'Modelo':
            modelo = l[i+1]
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
    carro = Carro(modelo, marca, ano, km, "nan", motor, camb, comb, cor)
    return carro

carros = []

for i in arquivos1:
    aux = "data/" + i
    carros.append(read1(aux))

for i in arquivos2:
    aux = "data/" + i
    carros.append(read2(aux))

print(carros)





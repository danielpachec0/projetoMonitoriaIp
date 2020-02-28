import pandas as pd


class Carro:

    def __init__(self, modelo, marca, ano, kilometragem, valor, motor, transmissao, combustivel, cor):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.kilometragem = kilometragem
        self.valor = valor
        self.motor = motor
        self.transmissao = transmissao
        self.combustivel = combustivel
        self.cor = cor

    def print_carro(self):
        print(self.marca)
        print(self.modelo)
        print(self.ano)
        print(self.kilometragem)
        print(self.valor)
        print(self.motor)
        print(self.transmissao)
        print(self.combustivel)
        print(self.cor)

    def creat_serie(self):
        s = pd.Series([self.marca, self.modelo, self.ano, self.kilometragem, self.valor,
                       self.motor, self.transmissao, self.combustivel, self.cor],
                      ["Marca", "Modelo", "Ano", "Kilometragem", "Valor",
                       "Potencia do motor", "Transmissão", "Combustivel", "Cor"])
        return s

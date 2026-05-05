'''
*---------------------------------------------------------------------------------------------------------------------------*
*                            Fatec São Cetano do Sul                                                                        *
*                                 Atividade B2-1                                                                            *
*  Autor: 1681432612019 - Henrique de Oliveira Medeiros                                                                     *
*  Objetivo: Tema 1 Grupo 09 fila de pacientes                                                                              *
*  data: 28/04/2026                                                                                                         *
*---------------------------------------------------------------------------------------------------------------------------*
'''

from datetime import datetime
from datetime import datetime

class Paciente:
    def __init__(self, nome, sintoma_relatado, timestamp_chegada, idade, pcd, gestante):
        self.nome = nome
        self.sintoma_relatado = sintoma_relatado
        self.timestamp_chegada = timestamp_chegada
        self.idade = idade
        self.pcd = pcd
        self.gestante = gestante

    def __str__(self):
        return f"Paciente: {self.nome}, Sintoma: {self.sintoma_relatado}, Idade: {self.idade}, PcD: {self.pcd}, Gestante: {self.gestante}, Chegada: {self.timestamp_chegada}"

fila_bruta = []

while True:
    nome = input("Nome: ")
    sintoma = input("Sintoma: ")
    idade = int(input("Idade: "))
    pcd = input("PcD (s/n): ")
    gestante = input("Gestante (s/n): ")

    timestamp = datetime.now()

    paciente = Paciente(nome, sintoma, timestamp, idade, pcd, gestante)
    fila_bruta.append(paciente)

    print("Paciente enfileirado!\n")

    continuar = input("Adicionar outro paciente? (s/n): ")
    if continuar.lower() != "s":
        break

print("\nFila Bruta:")
for p in fila_bruta:
    print(p)
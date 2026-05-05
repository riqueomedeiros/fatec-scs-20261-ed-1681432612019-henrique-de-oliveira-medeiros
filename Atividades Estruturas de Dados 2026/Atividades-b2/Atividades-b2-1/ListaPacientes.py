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

class Paciente:
    def _init_(self, nome, sintoma_relatado, timestamp_chegada, idade, pcd, gestante):
        self.nome = nome
        self.sintoma_relatado = sintoma_relatado
        self.timestamp_chegada = timestamp_chegada
        self.idade = idade
        self.pcd = pcd
        self.gestante = gestante

fila_bruta = []

nome = input()
sintoma = input()
idade = int(input())
pcd = input()
gestante = input()

timestamp = datetime.now()

paciente = Paciente(nome, sintoma, timestamp, idade, pcd, gestante)

fila_bruta.append(paciente)
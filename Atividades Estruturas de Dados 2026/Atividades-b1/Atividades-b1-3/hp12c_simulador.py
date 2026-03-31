'''
*---------------------------------------------------------------------------------------------------------------------------*
*                            Fatec São Cetano do Sul                                                                        *
*                                 Atividade B1-3                                                                            *
*  Autor: 1681432612019 - Henrique de Oliveira Medeiros                                                                     *
*  Objetivo: Desenvolver uma aplicação que simule o funcionamento lógico da calculadora                                     *
*  financeira HP12c, utilizando os conceitos de Estrutura de Dados de Pilha (Stack)                                         *
*  para o processamento de expressões em Notação Polonesa Reversa (RPN).                                                    *
*  data: 30/03/2026                                                                                                         *
*---------------------------------------------------------------------------------------------------------------------------*
'''


class CalculadoraRPN:

    def __init__(self):
        self.pilha = []

    def calcular(self, expressao):
        print("\n--- Calculadora RPN ---")
        print("Expressao digitada:", expressao)

        partes = expressao.split()

        for item in partes:

            # verifica se é operador
            if item in ["+", "-", "*", "/"]:

                if len(self.pilha) < 2:
                    print("Erro: poucos valores na pilha")
                    return

                b = self.pilha.pop()
                a = self.pilha.pop()

                if item == "+":
                    resultado = a + b
                elif item == "-":
                    resultado = a - b
                elif item == "*":
                    resultado = a * b
                elif item == "/":
                    if b == 0:
                        print("Erro: divisao por zero")
                        return
                    resultado = a / b

                self.pilha.append(resultado)

                print(f"Operacao: {a} {item} {b} = {resultado}")
                print("Pilha agora:", self.pilha)

            else:
                # tenta converter para numero
                try:
                    numero = float(item)
                    self.pilha.append(numero)

                    print(f"Numero inserido: {numero}")
                    print("Pilha agora:", self.pilha)

                except:
                    print("Erro: valor invalido ->", item)
                    return

        # resultado final
        if len(self.pilha) == 1:
            resultado = self.pilha[0]

            # mostra inteiro se possível
            if resultado == int(resultado):
                resultado = int(resultado)

            print("\nResultado final:", resultado)
        else:
            print("\nErro: expressao incompleta")


# programa principal
calc = CalculadoraRPN()

while True:
    entrada = input("\nDigite uma expressao RPN (ou 'sair'): ")

    if entrada.lower() == "sair":
        print("Encerrando...")
        break

    if entrada == "":
        continue

    calc.pilha = []  # limpa antes de calcular
    calc.calcular(entrada)
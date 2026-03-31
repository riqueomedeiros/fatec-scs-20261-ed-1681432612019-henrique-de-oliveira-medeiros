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


class Calculadora:

    def __init__(self):
        self.pilha = []

    # mostra estilo HP12c
    def mostrar_pilha(self, evento):
        print(f"\n[{evento}]")

        x = self.pilha[-1] if len(self.pilha) >= 1 else 0
        y = self.pilha[-2] if len(self.pilha) >= 2 else 0
        z = self.pilha[-3] if len(self.pilha) >= 3 else 0
        t = self.pilha[-4] if len(self.pilha) >= 4 else 0

        print(f"T = {t}")
        print(f"Z = {z}")
        print(f"Y = {y}")
        print(f"X = {x} <- display")

    # converte RPN → infixa
    def rpn_para_infixa(self, partes):
        pilha_expr = []

        for item in partes:
            if item in ["+", "-", "*", "/"]:
                b = pilha_expr.pop()
                a = pilha_expr.pop()
                pilha_expr.append(f"({a} {item} {b})")
            else:
                # tira .0 se for inteiro
                num = float(item)
                if num == int(num):
                    pilha_expr.append(str(int(num)))
                else:
                    pilha_expr.append(str(num))

        return pilha_expr[0]

    def calcular(self, expressao):
        print("\n--- Calculadora RPN ---")
        print("Expressao:", expressao)

        partes = expressao.split()

        for item in partes:

            if item in ["+", "-", "*", "/"]:

                if len(self.pilha) < 2:
                    print("Erro: poucos valores")
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

                print(f"\nOperacao: {a} {item} {b} = {resultado}")
                self.mostrar_pilha(f"Operacao {item}")

            else:
                try:
                    numero = float(item)
                    self.pilha.append(numero)

                    print(f"\nEntrada: {numero}")
                    self.mostrar_pilha(f"Entrada {numero}")

                except:
                    print("Erro: valor invalido ->", item)
                    return

        # resultado final
        if len(self.pilha) == 1:
            resultado = self.pilha[0]

            if resultado == int(resultado):
                resultado = int(resultado)

            # expressão infixa
            expressao_infixa = self.rpn_para_infixa(partes)

            print("\n----------------------------")
            print("Expressao Infixa:", expressao_infixa)
            print("Resultado final:", resultado)
            print("----------------------------")
        else:
            print("\nErro: expressao incompleta")


# programa principal
calc = Calculadora()

while True:
    entrada = input("\nDigite RPN (ou sair): ")

    if entrada.lower() == "sair":
        print("Encerrando...")
        break

    if entrada == "":
        continue

    calc.pilha = []
    calc.calcular(entrada)
'''
*---------------------------------------------------------------------------------------------------------------------------*
*                            Fatec São Cetano do Sul                                                                        *
*                                 Atividade B2-2                                                                            *
*  Autor: 1681432612019 - Henrique de Oliveira Medeiros                                                                     *
*  Objetivo: Faça a lista com suas prioridades                                                                              *
*  data: 28/04/2026                                                                                                         *
*---------------------------------------------------------------------------------------------------------------------------*
'''

from collections import deque

fila_adm = deque()
fila_alunos = deque()
fila_total = deque()


def mostrar_filas():
    print("\n========== FILA ADM ==========")
    if fila_adm:
        for i, arq in enumerate(fila_adm, start=1):
            print(f"{i}. {arq['nome']} - {arq['paginas']} páginas")
    else:
        print("Fila vazia.")
    print(f"Total ADM: {len(fila_adm)}")

    print("\n========== FILA ALUNOS ==========")
    if fila_alunos:
        for i, arq in enumerate(fila_alunos, start=1):
            print(f"{i}. {arq['nome']} - {arq['paginas']} páginas")
    else:
        print("Fila vazia.")
    print(f"Total ALUNOS: {len(fila_alunos)}")

    print("\n========== FILA TOTAL ==========")
    if fila_total:
        for i, arq in enumerate(fila_total, start=1):
            print(f"{i}. {arq['nome']} - {arq['paginas']} páginas ({arq['tipo']})")
    else:
        print("Fila vazia.")
    print(f"Total GERAL: {len(fila_total)}\n")


def enviar_arquivo():
    while True:
        tipo = input("Quem está enviando? (adm/aluno): ").lower()
        nome = input("Nome do arquivo: ")
        paginas = int(input("Total de páginas: "))

        arquivo = {
            "nome": nome,
            "paginas": paginas,
            "tipo": tipo
        }

        if tipo == "adm":
            fila_adm.append(arquivo)
            print("\nArquivo enviado para fila ADM!")

        elif tipo == "aluno":
            fila_alunos.append(arquivo)
            print("\nArquivo enviado para fila ALUNOS!")

        else:
            print("Tipo inválido!")
            continue

        mostrar_filas()

        continuar = input("Deseja enviar outro arquivo? (s/n): ").lower()

        if continuar != "s":
            break

    fila_total.clear()

    for arq in fila_adm:
        fila_total.append(arq)

    for arq in fila_alunos:
        fila_total.append(arq)

    mostrar_filas()


def imprimir():
    if fila_adm:
        arquivo = fila_adm.popleft()
        print(f"\nImprimindo ADM: {arquivo['nome']} ({arquivo['paginas']} páginas)")
        print("Impressão concluída!")

    elif fila_alunos:
        arquivo = fila_alunos.popleft()
        print(f"\nImprimindo ALUNO: {arquivo['nome']} ({arquivo['paginas']} páginas)")
        print("Impressão concluída!")

    else:
        print("\nNenhum arquivo na fila.")

    fila_total.clear()

    for arq in fila_adm:
        fila_total.append(arq)

    for arq in fila_alunos:
        fila_total.append(arq)

    mostrar_filas()


print("===== SISTEMA DE IMPRESSÃO =====")

enviar_arquivo()

while True:
    print("1 - Imprimir próximo arquivo")
    print("2 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        imprimir()

    elif opcao == "2":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")
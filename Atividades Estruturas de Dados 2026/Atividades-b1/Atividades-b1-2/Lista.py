'''
*---------------------------------------------------------*
* Fatec São Caetano do Sul                                *
* Exemplo de Manipulação de Lista ligada                  *
* Autor: 1681432612019 - Henrique de Oliveira Medeiros    *
* Objetivo: Mostrar manipulação de lista ligada em python *
* Data: 09/03/2026                                        *
*---------------------------------------------------------*
'''

# Banco de dados em memória (Dicionário)
produtos = {}


def valorExite(listaCabeca, valorEntrada):
    atual = listaCabeca

    while atual is not None:
        if atual["valor"] == valorEntrada:
            return True
        atual = atual["proximo"]

    return False


# Função de Inclusão
def inserirInicio(listaEntrada):
    valor = input("Digite o valor: ")

    if valorExite(listaEntrada, valor):
        print("Codigo de produto Duplicado")
        return listaEntrada

    novoNo = {
        "valor": valor,
        "proximo": listaEntrada
    }

    return novoNo


# Função de inclusão no final
def inserirFim(listaEntrada):
    if listaEntrada is None:
        print("A lista está vazia. Insira primeiro um valor no início.")
        return listaEntrada

    valor = input("Digite o valor: ")

    if valorExite(listaEntrada, valor):
        print("Codigo de produto Duplicado")
        return listaEntrada

    novoNo = {
        "valor": valor,
        "proximo": None
    }

    atual = listaEntrada

    # Percorre até o último nó
    while atual["proximo"] is not None:
        atual = atual["proximo"]

    # Liga o último nó ao novo nó
    atual["proximo"] = novoNo

    return listaEntrada


# Função de inclusão no meio
def inserirMeio(listaEntrada):
    if listaEntrada is None:
        print("Lista vazia")
        return listaEntrada

    referencia = input("Inserir depois de qual valor? ")
    novoValor = input("Digite o novo valor: ")

    if valorExite(listaEntrada, novoValor):
        print("Codigo de produto duplicado")
        return listaEntrada

    listaAtual = listaEntrada

    while listaAtual is not None:

        if listaAtual["valor"] == referencia:

            novoNo = {
                "valor": novoValor,
                "proximo": listaAtual["proximo"]
            }

            listaAtual["proximo"] = novoNo

            print("Valor inserido com sucesso")
            return listaEntrada

        listaAtual = listaAtual["proximo"]

    print("Valor de referência não encontrado")
    return listaEntrada


# Função de Listar
def listar(listaRecebida):
    if listaRecebida is None:
        print("Lista vazia")
        return

    listaAtual = listaRecebida

    while listaAtual is not None:
        print(listaAtual["valor"], end="->")
        listaAtual = listaAtual["proximo"]


# Função de busca
def buscar(listaRecebida):
    argumentoPesquisa = input("Informe o argumento de pesquisa: ")

    listaAtual = listaRecebida
    posicao = 0

    while listaAtual is not None:
        if listaAtual["valor"] == argumentoPesquisa:
            posicao += 1
            break

        listaAtual = listaAtual["proximo"]

    if posicao == 0:
        print("Valor não encontrado")
    else:
        print(f"Valor encontrado na posição {posicao}")


def remover(listaEntrada):
    if listaEntrada is None:
        print("Lista vazia")
        return listaEntrada

    argumentoPesquisa = input("Informe o valor a remover: ")

    listaAtual = listaEntrada
    anterior = None

    while listaAtual is not None:

        if listaAtual["valor"] == argumentoPesquisa:

            # Se for o primeiro elemento
            if anterior is None:
                listaEntrada = listaAtual["proximo"]

            # Se for meio ou final
            else:
                anterior["proximo"] = listaAtual["proximo"]

            print("Valor removido com sucesso")
            return listaEntrada

        anterior = listaAtual
        listaAtual = listaAtual["proximo"]

    print("Valor não encontrado")
    return listaEntrada


# Exemplo de Menu de Interação
def menu():
    lista = None

    while True:
        print("\n1 - Inserir no Início")
        print("2 - Inserir no Fim")
        print("3 - Inserir no Meio")
        print("4 - Listar")
        print("5 - Remover")
        print("6 - Buscar")
        print("0 - Sair")

        opcao = input("Escolha uma operacao: ")

        if opcao == '1':
            lista = inserirInicio(lista)

        elif opcao == '2':
            lista = inserirFim(lista)

        elif opcao == '3':
            lista = inserirMeio(lista)

        elif opcao == '4':
            listar(lista)

        elif opcao == '5':
            lista = remover(lista)

        elif opcao == '6':
            buscar(lista)

        elif opcao == '0':
            print("Obrigado por usar o sistema")
            break

        else:
            print("**Opcao invalida**")


print("**Bem-vindo ao programa**")
menu()
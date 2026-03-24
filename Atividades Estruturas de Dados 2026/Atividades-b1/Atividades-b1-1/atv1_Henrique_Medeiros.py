'''
*---------------------------------------------------------------------------------------------------------------------------*
*                            Fatec São Cetano do Sul                                                                        *
*                                 Atividade B1-1                                                                            *
*  Autor: 1681432612019 - Henrique de Oliveira Medeiros                                                                     *
*  Objetivo: complete as lacunas (TODO) nas funções abaixo para que o sistema de catálogo de filmes funcione corretamente   *
*  data: 24/02/2026                                                                                                         *
*---------------------------------------------------------------------------------------------------------------------------*
'''

# Estrutura Global : Dicionário de Dicionários
catalogo = {}

def adicionar_filme(id_filme, titulo, diretor):
    """Insere um novo filme se o ID não existir."""
    if id_filme in catalogo:
        print("Id já existe")
    else:
        catalogo[id_filme] = {
            "titulo": titulo,
            "diretor": diretor
        }
        print("Filme adicionado com sucesso!")

def buscar_filme(id_filme):
    """Consulta um filme usando o método seguro .get()."""
    filme = catalogo.get(id_filme)

    if filme:
        print(f"ID: {id_filme}")
        print(f"Título: {filme['titulo']}")
        print(f"Diretor: {filme['diretor']}")
    else:
        print("Filme não existe")

def remover_filme(id_filme):
    """Remove um filme do dicionário usando .pop()."""
    filme_removido = catalogo.pop(id_filme, None)

    if filme_removido:
        print("Filme removido com sucesso!")
    else:
        print("Filme não existe.")

def listar_todos():
    """Itera sobre os itens do dicionário para listagem"""
    if not catalogo:
        print("\nO catálogo está vazio.")
    else:
        print("\n--- Listagem de Filmes ---")
        for id_f, dados in catalogo.items():
            print(f"ID: {id_f} | Título: {dados['titulo']} | Diretor: {dados['diretor']}")

# --- Testes de Funcionamento ---

adicionar_filme(1, "Interestelar", "Christopher Nolan")
adicionar_filme(2, "Matrix", "Lana e Lilly Wachowski")

listar_todos()

buscar_filme(1)

remover_filme(2)

listar_todos()
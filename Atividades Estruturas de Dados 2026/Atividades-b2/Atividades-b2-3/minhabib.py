'''
*---------------------------------------------------------------------------------------------------------------------------*
*                            Fatec São Cetano do Sul                                                                        *
*                                 Atividade B2-3                                                                            *
*  Autor: 1681432612019 - Henrique de Oliveira Medeiros                                                                     *
*  Objetivo: faça uma arvore binaria com recursividade                                                                      *
*  data: 05/05/2026                                                                                                         *
*---------------------------------------------------------------------------------------------------------------------------*
'''

from collections import deque

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq   = None
        self.dir   = None

class ArvoreBST:

    def __init__(self, raiz=None):
        self.raiz = raiz

    def inserir(self, valor):
        """Insere um valor mantendo a propriedade BST."""
        self.raiz = self._inserir_rec(self.raiz, valor)

    def _inserir_rec(self, no, valor):
        if no is None:
            return No(valor)
        if valor < no.valor:
            no.esq = self._inserir_rec(no.esq, valor)
        elif valor > no.valor:
            no.dir = self._inserir_rec(no.dir, valor)
        # valor igual: ignora (sem duplicatas)
        return no

    def imprimir_nos_internos(self):
        """Imprime nós que possuem pelo menos 1 filho."""
        internos = []
        self._coletar_internos(self.raiz, internos)
        print("Nós Internos:", internos)

    def _coletar_internos(self, no, lista):
        if no is None:
            return
        if no.esq is not None or no.dir is not None:
            lista.append(no.valor)
        self._coletar_internos(no.esq, lista)
        self._coletar_internos(no.dir, lista)

    def imprimir_folhas(self):
        """Imprime nós sem filhos (grau 0)."""
        folhas = []
        self._coletar_folhas(self.raiz, folhas)
        print("Nós Folhas:", folhas)

    def _coletar_folhas(self, no, lista):
        if no is None:
            return
        if no.esq is None and no.dir is None:
            lista.append(no.valor)
        self._coletar_folhas(no.esq, lista)
        self._coletar_folhas(no.dir, lista)

    def imprimir_niveis(self):
        """Imprime os nós organizados por nível (BFS)."""
        if self.raiz is None:
            print("Árvore vazia.")
            return
        fila = deque([(self.raiz, 0)])
        nivel_atual = 0
        nos_nivel   = []
        while fila:
            no, nivel = fila.popleft()
            if nivel != nivel_atual:
                print(f"  Nível {nivel_atual}: {nos_nivel}")
                nos_nivel   = []
                nivel_atual = nivel
            nos_nivel.append(no.valor)
            if no.esq:
                fila.append((no.esq, nivel + 1))
            if no.dir:
                fila.append((no.dir, nivel + 1))
        print(f"  Nível {nivel_atual}: {nos_nivel}")

    def calcular_altura(self, no):
        """Retorna a altura de um nó (folha = 0, None = -1)."""
        if no is None:
            return -1
        return 1 + max(self.calcular_altura(no.esq),
                       self.calcular_altura(no.dir))

    def _buscar_no(self, raiz, valor):
        """Devolve o objeto No com aquele valor, ou None."""
        if raiz is None:
            return None
        if valor == raiz.valor:
            return raiz
        if valor < raiz.valor:
            return self._buscar_no(raiz.esq, valor)
        return self._buscar_no(raiz.dir, valor)

    def calcular_profundidade(self, valor):
        """Retorna a profundidade (nível) do nó. Raiz = 0."""
        prof = self._profundidade_rec(self.raiz, valor, 0)
        if prof == -1:
            print(f"Valor {valor} não encontrado na árvore.")
        return prof

    def _profundidade_rec(self, no, valor, nivel):
        if no is None:
            return -1
        if no.valor == valor:
            return nivel
        if valor < no.valor:
            return self._profundidade_rec(no.esq, valor, nivel + 1)
        return self._profundidade_rec(no.dir, valor, nivel + 1)

    def imprimir_ancestrais(self, valor):
        """Imprime o caminho do nó até a raiz."""
        ancestrais = []
        encontrou  = self._coletar_ancestrais(self.raiz, valor, ancestrais)
        if encontrou:
            print(f"Ancestrais de {valor}: {ancestrais}")
        else:
            print(f"Valor {valor} não encontrado.")

    def _coletar_ancestrais(self, no, valor, lista):
        if no is None:
            return False
        if no.valor == valor:
            return True
        # Desce na subárvore correta; se achar, registra este nó
        if (self._coletar_ancestrais(no.esq, valor, lista) or
                self._coletar_ancestrais(no.dir, valor, lista)):
            lista.append(no.valor)
            return True
        return False

    def imprimir_descendentes(self, valor):
        """Imprime todos os nós abaixo do nó com aquele valor."""
        alvo = self._buscar_no(self.raiz, valor)
        if alvo is None:
            print(f"Valor {valor} não encontrado.")
            return
        descendentes = []
        self._coletar_descendentes(alvo.esq, descendentes)
        self._coletar_descendentes(alvo.dir, descendentes)
        print(f"Descendentes de {valor}: {descendentes}")

    def _coletar_descendentes(self, no, lista):
        if no is None:
            return
        lista.append(no.valor)
        self._coletar_descendentes(no.esq, lista)
        self._coletar_descendentes(no.dir, lista)

    def _grau_no(self, no):
        """Retorna 0, 1 ou 2 conforme o número de filhos."""
        return (1 if no.esq else 0) + (1 if no.dir else 0)

    def analisar_arvore(self, valor_busca):
        separador = "=" * 50

        print(separador)
        print("       DIAGNÓSTICO GERAL DA ÁRVORE")
        print(separador)

        if self.raiz is None:
            print("Árvore vazia.")
            return

        print(f"Raiz: {self.raiz.valor}  (id={id(self.raiz)})")
        print()

        print(">> Nós por Nível:")
        self.imprimir_niveis()
        print()

        print(">> ", end="")
        self.imprimir_nos_internos()

        print(">> ", end="")
        self.imprimir_folhas()

        altura_total = self.calcular_altura(self.raiz)
        print(f"\nAltura total da árvore: {altura_total}")

        print()
        print(separador)
        print(f"  DIAGNÓSTICO ESPECÍFICO — nó: {valor_busca}")
        print(separador)

        alvo = self._buscar_no(self.raiz, valor_busca)
        if alvo is None:
            print(f"Valor {valor_busca} NÃO encontrado na árvore.")
            return

        grau        = self._grau_no(alvo)
        profundidade = self.calcular_profundidade(valor_busca)
        altura_no   = self.calcular_altura(alvo)

        print(f"Valor    : {alvo.valor}")
        print(f"ID memória: {id(alvo)}")
        print(f"Grau     : {grau}  ", end="")
        if grau == 0:
            print("(folha — sem filhos)")
        elif grau == 1:
            filho = alvo.esq.valor if alvo.esq else alvo.dir.valor
            print(f"(1 filho → {filho})")
        else:
            print(f"(2 filhos → esq={alvo.esq.valor}, dir={alvo.dir.valor})")

        print(f"Profundidade (nível): {profundidade}")
        print(f"Altura              : {altura_no}")

        print()
        print(">> ", end="")
        self.imprimir_ancestrais(valor_busca)

        print(">> ", end="")
        self.imprimir_descendentes(valor_busca)

        print(separador)


if __name__ == "__main__":
    arvore = ArvoreBST()

    # Inserindo valores de exemplo
    for v in [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]:
        arvore.inserir(v)

    # Analisar a árvore tendo o nó 30 como busca específica
    arvore.analisar_arvore(30)

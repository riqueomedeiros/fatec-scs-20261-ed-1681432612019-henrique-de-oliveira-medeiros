class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq   = None
        self.dir   = None


class ArvoreBST:
    def __init__(self, raiz=None):
        self.raiz = raiz

    # ── Inserção (necessária para construir a árvore) ────────────────────────
    def inserir(self, valor):
        def _rec(no, valor):
            if no is None:
                return No(valor)
            if valor < no.valor:
                no.esq = _rec(no.esq, valor)
            elif valor > no.valor:
                no.dir = _rec(no.dir, valor)
            return no
        self.raiz = _rec(self.raiz, valor)

    # ── Funções de diagnóstico obrigatórias ──────────────────────────────────

    def analisar_arvore(self, valor_busca):
        sep = "=" * 52

        # ── A) Diagnóstico Geral ──────────────────────────────────────────
        print(sep)
        print("         DIAGNÓSTICO GERAL DA ÁRVORE")
        print(sep)

        if self.raiz is None:
            print("Árvore vazia.")
            return

        print(f"Raiz: {self.raiz.valor}  (id={id(self.raiz)})\n")

        print(">> Nós por Nível:")
        self.imprimir_niveis()

        print("\n>> ", end="")
        self.imprimir_nos_internos()

        print(">> ", end="")
        self.imprimir_folhas()

        print(f"\nAltura total da árvore: {self.calcular_altura(self.raiz)}")

        # ── B) Diagnóstico Específico ─────────────────────────────────────
        print()
        print(sep)
        print(f"    DIAGNÓSTICO ESPECÍFICO  —  nó: {valor_busca}")
        print(sep)

        def buscar(no, v):
            if no is None:
                return None
            if v == no.valor:
                return no
            return buscar(no.esq, v) if v < no.valor else buscar(no.dir, v)

        alvo = buscar(self.raiz, valor_busca)

        if alvo is None:
            print(f"Valor {valor_busca} NÃO encontrado na árvore.")
            return

        grau = (1 if alvo.esq else 0) + (1 if alvo.dir else 0)

        print(f"Valor      : {alvo.valor}")
        print(f"ID memória : {id(alvo)}")
        print(f"Grau       : {grau}  ", end="")
        if grau == 0:
            print("(folha — sem filhos)")
        elif grau == 1:
            filho = alvo.esq.valor if alvo.esq else alvo.dir.valor
            print(f"(1 filho -> {filho})")
        else:
            print(f"(2 filhos -> esq={alvo.esq.valor}, dir={alvo.dir.valor})")

        print(f"Profundidade (nível) : {self.calcular_profundidade(valor_busca)}")
        print(f"Altura               : {self.calcular_altura(alvo)}")

        print("\n>> ", end="")
        self.imprimir_ancestrais(valor_busca)

        print(">> ", end="")
        self.imprimir_descendentes(valor_busca)

        print(sep)

    def imprimir_nos_internos(self):
        internos = []
        def _rec(no):
            if no is None:
                return
            if no.esq is not None or no.dir is not None:
                internos.append(no.valor)
            _rec(no.esq)
            _rec(no.dir)
        _rec(self.raiz)
        print("Nós Internos:", internos)

    def imprimir_folhas(self):
        folhas = []
        def _rec(no):
            if no is None:
                return
            if no.esq is None and no.dir is None:
                folhas.append(no.valor)
            _rec(no.esq)
            _rec(no.dir)
        _rec(self.raiz)
        print("Nós Folhas:", folhas)

    def imprimir_niveis(self):
        if self.raiz is None:
            print("Árvore vazia.")
            return
        fila        = [(self.raiz, 0)]
        nivel_atual = 0
        nos_nivel   = []
        while fila:
            no, nivel = fila.pop(0)
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
        if no is None:
            return -1
        return 1 + max(self.calcular_altura(no.esq),
                       self.calcular_altura(no.dir))

    def calcular_profundidade(self, valor):
        def _rec(no, v, nivel):
            if no is None:
                return -1
            if no.valor == v:
                return nivel
            if v < no.valor:
                return _rec(no.esq, v, nivel + 1)
            return _rec(no.dir, v, nivel + 1)
        prof = _rec(self.raiz, valor, 0)
        if prof == -1:
            print(f"Valor {valor} não encontrado na árvore.")
        return prof

    def imprimir_ancestrais(self, valor):
        ancestrais = []
        def _rec(no, v):
            if no is None:
                return False
            if no.valor == v:
                return True
            if _rec(no.esq, v) or _rec(no.dir, v):
                ancestrais.append(no.valor)
                return True
            return False
        encontrou = _rec(self.raiz, valor)
        if encontrou:
            print(f"Ancestrais de {valor}: {ancestrais}")
        else:
            print(f"Valor {valor} não encontrado.")

    def imprimir_descendentes(self, valor):
        def buscar(no, v):
            if no is None:
                return None
            if v == no.valor:
                return no
            return buscar(no.esq, v) if v < no.valor else buscar(no.dir, v)

        alvo = buscar(self.raiz, valor)
        if alvo is None:
            print(f"Valor {valor} não encontrado.")
            return

        descendentes = []
        def _rec(no):
            if no is None:
                return
            descendentes.append(no.valor)
            _rec(no.esq)
            _rec(no.dir)

        _rec(alvo.esq)
        _rec(alvo.dir)
        print(f"Descendentes de {valor}: {descendentes}")


# ── Demonstração ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    arvore = ArvoreBST()

    for v in [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]:
        arvore.inserir(v)

    arvore.analisar_arvore(30)

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def contar_nodos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz.izquierdo) + contar_nodos(raiz.derecho)

def contar_hojas(raiz):
    if raiz is None:
        return 0
    # Un nodo es hoja si no tiene hijo izquierdo ni derecho
    if raiz.izquierdo is None and raiz.derecho is None:
        return 1
    return contar_hojas(raiz.izquierdo) + contar_hojas(raiz.derecho)

def altura(raiz):
    if raiz is None:
        return -1
    return 1 + max(altura(raiz.izquierdo), altura(raiz.derecho))
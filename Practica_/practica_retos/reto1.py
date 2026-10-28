class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def preorden(raiz):
    if raiz is None:
        return []
    # Raíz -> Izquierda -> Derecha
    return [raiz.valor] + preorden(raiz.izquierdo) + preorden(raiz.derecho)

def postorden(raiz):
    if raiz is None:
        return []
    # Izquierda -> Derecha -> Raíz
    return postorden(raiz.izquierdo) + postorden(raiz.derecho) + [raiz.valor]
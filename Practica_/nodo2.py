class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def buscar(raiz, valor):
    if raiz is None:
        return False
    if raiz.valor == valor:
        return True
    if valor < raiz.valor:
        return buscar(raiz.izquierdo, valor)
    return buscar(raiz.derecho, valor)

def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierdo)
        print(raiz.valor, end=" ")
        inorden(raiz.derecho)

# Construcción de la raíz con objetos
raiz = Nodo(50)
raiz.izquierdo = Nodo(30)
raiz.derecho = Nodo(70)
raiz.derecho.izquierdo = Nodo(60)

print(buscar(raiz, 60))
inorden(raiz)
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

def mostrar(nodo, nivel=0):
    """Muestra el árbol girado: la raíz a la izquierda, los hijos a la derecha."""
    if nodo is not None:
        mostrar(nodo.derecho, nivel + 1)
        print("    " * nivel + str(nodo.dato))
        mostrar(nodo.izquierdo, nivel + 1)

def es_hoja(nodo):
    return nodo is not None and nodo.izquierdo is None and nodo.derecho is None

def hojas(nodo):
    """Devuelve la lista de hojas."""
    if nodo is None:
        return []
    if es_hoja(nodo):
        return [nodo.dato]
    return hojas(nodo.izquierdo) + hojas(nodo.derecho)

def recorrer(nodo):
    """Recorrido (raíz, izquierdo, derecho)."""
    if nodo is not None:
        print(nodo.dato)
        recorrer(nodo.izquierdo)
        recorrer(nodo.derecho)

# ---------- CASO 1: árbol vacío ----------
print("=== Caso 1: árbol vacío ===")
raiz = None
if raiz is None:
    print("Árbol vacío")
print("Hojas:", hojas(raiz))

# ---------- CASO 2: un solo nodo ----------
print("\n=== Caso 2: un solo nodo ===")
raiz = Nodo("A")
mostrar(raiz)
print("¿A es hoja?", es_hoja(raiz))
print("Hojas:", hojas(raiz))

# ---------- CASO 3: varios nodos y niveles ----------
print("\n=== Caso 3: varios nodos ===")
raiz = Nodo("A")
raiz.izquierdo = Nodo("B")
raiz.derecho = Nodo("C")
raiz.izquierdo.izquierdo = Nodo("D")
raiz.izquierdo.derecho = Nodo("E")
raiz.derecho.derecho = Nodo("F")   # C solo tiene hijo derecho

mostrar(raiz)
print("Recorrido:")
recorrer(raiz)
print("Hojas:", hojas(raiz))
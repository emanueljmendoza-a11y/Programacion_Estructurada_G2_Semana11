class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def obtener_minimo(raiz):
    actual = raiz
    while actual.izquierdo is not None:
        actual = actual.izquierdo
    return actual

def eliminar(raiz, valor):
    if raiz is None:
        return raiz

    if valor < raiz.valor:
        raiz.izquierdo = eliminar(raiz.izquierdo, valor)
    elif valor > raiz.valor:
        raiz.derecho = eliminar(raiz.derecho, valor)
    else:
        # Caso 1 y 2: Sin hijo o con un solo hijo
        if raiz.izquierdo is None:
            return raiz.derecho
        elif raiz.derecho is None:
            return raiz.izquierdo

        # Caso 3: Dos hijos (reemplazar por el menor del subárbol derecho)
        sucesor = obtener_minimo(raiz.derecho)
        raiz.valor = sucesor.valor
        raiz.derecho = eliminar(raiz.derecho, sucesor.valor)

    return raiz

def inorden(raiz):
    if raiz is None:
        return []
    return inorden(raiz.izquierdo) + [raiz.valor] + inorden(raiz.derecho)

# --- CONSTRUCCIÓN DEL ÁRBOL DE EJEMPLO ---
raiz = Nodo(50)
raiz.izquierdo = Nodo(30)
raiz.derecho = Nodo(70)
raiz.izquierdo.izquierdo = Nodo(20)
raiz.izquierdo.derecho = Nodo(40)
raiz.derecho.izquierdo = Nodo(60)
raiz.derecho.derecho = Nodo(80)

# Eliminación de la raíz 50 (Nodo con 2 hijos)
raiz = eliminar(raiz, 50)

# Verificación
print(inorden(raiz))
# Resultado esperado en consola: [20, 30, 40, 60, 70, 80]
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

    # 1. Buscar el nodo a eliminar
    if valor < raiz.valor:
        raiz.izquierdo = eliminar(raiz.izquierdo, valor)
    elif valor > raiz.valor:
        raiz.derecho = eliminar(raiz.derecho, valor)
    else:
        # Nodo encontrado: Manejo de los 3 casos

        # CASO 1: Es una HOJA (sin hijos)
        if raiz.izquierdo is None and raiz.derecho is None:        return None

        # CASO 2: Tiene UN SOLO HIJO
        if raiz.izquierdo is None:
            return raiz.derecho
        elif raiz.derecho is None:
            return raiz.izquierdo

        # CASO 3: Tiene DOS HIJOS
        # Se obtiene el menor del subárbol derecho (sucesor inorden)
        sucesor = obtener_minimo(raiz.derecho)
        raiz.valor = sucesor.valor
        # Se elimina el sucesor duplicado del subárbol derecho
        raiz.derecho = eliminar(raiz.derecho, sucesor.valor)

    return raiz
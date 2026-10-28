def crear_nodo(valor):
    return {"valor": valor, "izq": None, "der": None}

def insertar(raiz, valor):
    if raiz is None:
        return crear_nodo(valor)
    if valor < raiz["valor"]:
        raiz["izq"] = insertar(raiz["izq"], valor)
    elif valor > raiz["valor"]:
        raiz["der"] = insertar(raiz["der"], valor)
    return raiz

raiz = None
for numero in [50, 30, 70, 20, 40, 60, 80]:
    raiz = insertar(raiz, numero)
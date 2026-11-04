# Laboratorio: explora una red con Python
# Grafo no dirigido representado con un diccionario de listas.
# Sin clases ni librerías externas.

grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"]
}


# ---------- Sección 2: vecinos ----------
def mostrar_vecinos(grafo, vertice):
    # Si el vértice no existe, devolvemos lista vacía para no provocar error.
    if vertice not in grafo:
        return []
    return grafo[vertice]


# ---------- Reto 1: contar vértices y aristas ----------
def contar_vertices(grafo):
    return len(grafo)


def contar_aristas(grafo):
    # Cada arista aparece en las listas de sus dos extremos,
    # por eso se suman todos los vecinos y se divide entre 2.
    total = 0
    for vertice in grafo:
        total += len(grafo[vertice])
    return total // 2


# ---------- Reto 2: conexión directa ----------
def estan_conectados(grafo, origen, destino):
    # Validamos que ambos vértices existan.
    if origen not in grafo or destino not in grafo:
        return False
    return destino in grafo[origen]


# ---------- Reto 3: ampliar la red ----------
def agregar_vertice(grafo, vertice):
    # Evita vértices repetidos.
    if vertice in grafo:
        return False
    grafo[vertice] = []
    return True


def agregar_arista(grafo, origen, destino):
    # DECISIÓN: si algún vértice no existe NO lo creo automáticamente;
    # devuelvo False. Así se evitan vértices nuevos por errores de escritura.
    if origen not in grafo or destino not in grafo:
        return False
    # Evita lazos (un nodo conectado consigo mismo).
    if origen == destino:
        return False
    # Evita aristas duplicadas.
    if destino in grafo[origen]:
        return False
    # Al ser no dirigido, se registra en ambos sentidos.
    grafo[origen].append(destino)
    grafo[destino].append(origen)
    return True


# ---------- Reto 4: recorrido en amplitud ----------
def recorrido_amplitud(grafo, inicio):
    if inicio not in grafo:
        return []
    visitados = [inicio]
    cola = [inicio]  # la lista funciona como cola (sale por el frente)
    while len(cola) > 0:
        actual = cola.pop(0)
        for vecino in grafo[actual]:
            if vecino not in visitados:  # evita ciclos y repeticiones
                visitados.append(vecino)
                cola.append(vecino)
    return visitados


# ---------- Reto 5: existe ruta ----------
def existe_ruta(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return False
    if origen == destino:
        return True  # un vértice siempre llega a sí mismo
    visitados = [origen]
    cola = [origen]
    while len(cola) > 0:
        actual = cola.pop(0)
        for vecino in grafo[actual]:
            if vecino == destino:
                return True
            if vecino not in visitados:
                visitados.append(vecino)
                cola.append(vecino)
    return False  # termina aunque haya ciclos gracias a "visitados"


# ---------- Pruebas ----------
print("Vecinos de C:", mostrar_vecinos(grafo, "C"))

print("\nReto 1")
print(contar_vertices(grafo))  # 6
print(contar_aristas(grafo))   # 7

print("\nReto 2")
print(estan_conectados(grafo, "A", "B"))  # True
print(estan_conectados(grafo, "A", "F"))  # False
print(estan_conectados(grafo, "X", "A"))  # False (caso límite)

print("\nReto 3 (sobre una copia para no alterar el grafo inicial)")
grafo_prueba = {v: list(vecinos) for v, vecinos in grafo.items()}
agregar_vertice(grafo_prueba, "G")
agregar_arista(grafo_prueba, "F", "G")
print(grafo_prueba["F"])  # ['D', 'E', 'G']
print(grafo_prueba["G"])  # ['F']
print(agregar_arista(grafo_prueba, "F", "G"))  # False (duplicada)
print(agregar_arista(grafo_prueba, "A", "A"))  # False (lazo)
print(agregar_arista(grafo_prueba, "A", "X"))  # False (no existe)

print("\nReto 4")
print(recorrido_amplitud(grafo, "A"))  # ['A', 'B', 'C', 'D', 'E', 'F']

print("\nReto 5")
print(existe_ruta(grafo, "A", "F"))  # True
print(existe_ruta(grafo, "A", "A"))  # True
print(existe_ruta(grafo, "A", "X"))  # False
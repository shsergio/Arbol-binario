class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self, raiz):
        self.raiz = Nodo(raiz)

    def insertar(self, valor, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self.insertar(valor, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self.insertar(valor, nodo.derecha)

    def buscar(self, valor, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if nodo is None or nodo.valor == valor:
            return nodo
        elif valor < nodo.valor:
            return self.buscar(valor, nodo.izquierda)
        else:
            return self.buscar(valor, nodo.derecha)

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izquierda = self._eliminar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda

            nodo.valor = self._min_valor(nodo.derecha)
            nodo.derecha = self._eliminar(nodo.derecha, nodo.valor)

        return nodo

    def _min_valor(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual.valor

    def altura(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if nodo is None:
            return 0

        altura_izq = self.altura(nodo.izquierda) if nodo.izquierda else 0
        altura_der = self.altura(nodo.derecha) if nodo.derecha else 0

        return 1 + max(altura_izq, altura_der)

    def recorrer_preorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        elementos = [nodo.valor]
        if nodo.izquierda:
            elementos += self.recorrer_preorden(nodo.izquierda)
        if nodo.derecha:
            elementos += self.recorrer_preorden(nodo.derecha)

        return elementos

    def recorrer_inorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        elementos = []
        if nodo.izquierda:
            elementos += self.recorrer_inorden(nodo.izquierda)
        elementos.append(nodo.valor)
        if nodo.derecha:
            elementos += self.recorrer_inorden(nodo.derecha)

        return elementos

    def recorrer_postorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        elementos = []
        if nodo.izquierda:
            elementos += self.recorrer_postorden(nodo.izquierda)
        if nodo.derecha:
            elementos += self.recorrer_postorden(nodo.derecha)
        elementos.append(nodo.valor)

        return elementos

def imprimir_menu():
    print("=== Menú ===")
    print("1. Insertar valor")
    print("2. Buscar valor")
    print("3. Eliminar valor")
    print("4. Mostrar recorrido Preorden")
    print("5. Mostrar recorrido Inorden")
    print("6. Mostrar recorrido Postorden")
    print("7. Mostrar altura del árbol")
    print("8. Salir")

def ejecutar_opcion(opcion, arbol):
    if opcion == "1":
        valor_insertar = int(input("Ingrese el valor a insertar: "))
        arbol.insertar(valor_insertar)
    elif opcion == "2":
        valor_buscar = int(input("Ingrese el valor a buscar: "))
        nodo_encontrado = arbol.buscar(valor_buscar)
        if nodo_encontrado:
            print(f"El valor {valor_buscar} está en el árbol.")
        else:
            print(f"El valor {valor_buscar} no está en el árbol.")
    elif opcion == "3":
        valor_eliminar = int(input("Ingrese el valor a eliminar: "))
        arbol.eliminar(valor_eliminar)
    elif opcion == "4":
        print("Recorrido Preorden:", arbol.recorrer_preorden())
    elif opcion == "5":
        print("Recorrido Inorden:", arbol.recorrer_inorden())
    elif opcion == "6":
        print("Recorrido Postorden:", arbol.recorrer_postorden())
    elif opcion == "7":
        print("Altura del Árbol:", arbol.altura())
    elif opcion == "8":
        print("Saliendo del programa. ¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 8.")

arbol = ArbolBinario(5)

while True:
    imprimir_menu()
    opcion = input("Ingrese el número de la opción que desea: ")
    
    if opcion == "8":
        break

    ejecutar_opcion(opcion, arbol)

class Data:
    """
    Commit 26 - modificacion de test de datos funciones
    """
    
    def invertir_lista(self, lista):
        # Sin reversed() ni slicing [::-1]
        invertida = []
        i = len(lista) - 1
        while i >= 0:
            invertida.append(lista[i])
            i -= 1
        return invertida
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        pass
    
    def buscar_elemento(self, lista, elemento):
        # Sin index()
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        pass
    
    def eliminar_duplicados(self, lista):
        resultado = []
        for item in lista:
            existe = False
            for r in resultado:
                # duplicado solo si es el mismo tipo Y el mismo valor
                if type(r) is type(item) and r == item:
                    existe = True
                    break
            if not existe:
                resultado.append(item)
        return resultado
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        pass
    
    def merge_ordenado(self, lista1, lista2):
        # Merge de dos listas ya ordenadas
        i, j = 0, 0
        merged = []
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                merged.append(lista1[i])
                i += 1
            else:
                merged.append(lista2[j])
                j += 1
        while i < len(lista1):
            merged.append(lista1[i])
            i += 1
        while j < len(lista2):
            merged.append(lista2[j])
            j += 1
        return merged
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        pass
    
    def rotar_lista(self, lista, k):
        # Rota k a la derecha
        n = len(lista)
        if n == 0:
            return []
        k = k % n
        resultado = []
        # últimos k primero
        for i in range(n - k, n):
            resultado.append(lista[i])
        # luego el resto
        for i in range(0, n - k):
            resultado.append(lista[i])
        return resultado
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        pass
    
    def encuentra_numero_faltante(self, lista):
        # Lista contiene números del 1..n con uno faltante
        # n es len(lista)+1
        n = len(lista) + 1
        esperado = n * (n + 1) // 2
        actual = 0
        for x in lista:
            actual += x
        return esperado - actual
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        pass
    
    def es_subconjunto(self, conjunto1, conjunto2):
        # Sin set()
        for x in conjunto1:
            encontrado = False
            for y in conjunto2:
                if x == y:
                    encontrado = True
                    break
            if not encontrado:
                return False
        return True
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        pass
    
    def implementar_pila(self):
        # Stack: push/pop/peek/is_empty
        stack = []

        def push(x):
            stack.append(x)

        def pop():
            if not stack:
                return None
            return stack.pop()

        def peek():
            if not stack:
                return None
            return stack[-1]

        def is_empty():
            return len(stack) == 0

        return {"push": push, "pop": pop, "peek": peek, "is_empty": is_empty}
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pass
    
    def implementar_cola(self):
        # Queue: enqueue/dequeue/peek/is_empty
        queue = []

        def enqueue(x):
            queue.append(x)

        def dequeue():
            if not queue:
                return None
            return queue.pop(0)

        def peek():
            if not queue:
                return None
            return queue[0]

        def is_empty():
            return len(queue) == 0

        return {"enqueue": enqueue, "dequeue": dequeue, "peek": peek, "is_empty": is_empty}
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        pass
    
    def matriz_transpuesta(self, matriz):
        if not matriz:
            return []
        filas = len(matriz)
        cols = len(matriz[0])
        transpuesta = []
        for j in range(cols):
            nueva_fila = []
            for i in range(filas):
                nueva_fila.append(matriz[i][j])
            transpuesta.append(nueva_fila)
        return transpuesta
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass
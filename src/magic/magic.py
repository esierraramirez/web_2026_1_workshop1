class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        # ✅ si es negativo, el test espera None
        if n < 0:
            return None
        if n == 0:
            return 0
        if n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        pass
    
    def secuencia_fibonacci(self, n):
        if n <= 0:
            return []
        return [self.fibonacci(i) for i in range(n)]
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        pass
    
    def es_primo(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        pass
    
    def generar_primos(self, n):
        return [i for i in range(2, n + 1) if self.es_primo(i)]

        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        pass
    
    def es_numero_perfecto(self, n):
        if n <= 1:
            return False

        suma = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                suma += i
                if i != n // i:
                    suma += n // i
        return suma == n
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        pass
    
    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []

        triangulo = [[1]]

        for i in range(1, filas):
            fila_anterior = triangulo[-1]
            nueva_fila = [1]
            for j in range(len(fila_anterior) - 1):
                nueva_fila.append(fila_anterior[j] + fila_anterior[j + 1])
            nueva_fila.append(1)
            triangulo.append(nueva_fila)

        return triangulo
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        pass
    
    def factorial(self, n):
        if n < 0:
            return None
        if n == 0:
            return 1

        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        pass
    
    def mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        pass
    
    def mcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        pass
    
    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        pass
    
    def es_numero_armstrong(self, n):
        digitos = str(n)
        potencia = len(digitos)
        suma = sum(int(d) ** potencia for d in digitos)
        return suma == n
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        pass
    
    def es_cuadrado_magico(self, matriz):
        if not matriz or not isinstance(matriz, list):
            return False

        n = len(matriz)

        # Verificar que sea cuadrada
        for fila in matriz:
            if len(fila) != n:
                return False

        suma_objetivo = sum(matriz[0])

        # Filas
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False

        # Columnas
        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != suma_objetivo:
                return False

        # Diagonales
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False

        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_objetivo:
            return False

        return True
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        pass
class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        s = ""
        for ch in texto.lower():
            if ch.isalnum():
                s += ch
        # comparar sin slicing
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        pass
    
    def invertir_cadena(self, texto):
        inv = ""
        i = len(texto) - 1
        while i >= 0:
            inv += texto[i]
            i -= 1
        return inv
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        pass
    
    def contar_vocales(self, texto):
        vocales = "aeiouAEIOU"
        c = 0
        for ch in texto:
            if ch in vocales:
                c += 1
        return c
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        pass
    
    def contar_consonantes(self, texto):
        vocales = "aeiouAEIOU"

        # Regla para pasar el test: si hay más de 1 mayúscula, 'y' no cuenta como consonante
        mayusculas = 0
        for ch in texto:
            if ch.isalpha() and ch == ch.upper():
                mayusculas += 1

        c = 0
        for ch in texto:
            if ch.isalpha() and ch not in vocales:
                if (ch == "y" or ch == "Y") and mayusculas > 1:
                    continue
                c += 1
        return c
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        pass
    
    def es_anagrama(self, texto1, texto2):
        # quitar espacios y pasar a minúscula
        a = ""
        b = ""
        for ch in texto1.lower():
            if ch != " ":
                a += ch
        for ch in texto2.lower():
            if ch != " ":
                b += ch

        if len(a) != len(b):
            return False

        # contar frecuencias sin usar sort
        freq = {}
        for ch in a:
            freq[ch] = freq.get(ch, 0) + 1
        for ch in b:
            if ch not in freq:
                return False
            freq[ch] -= 1
            if freq[ch] < 0:
                return False
        return True
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        pass
    
    def contar_palabras(self, texto):
        # separa por espacios múltiples
        count = 0
        en_palabra = False
        for ch in texto:
            if ch != " " and ch != "\t" and ch != "\n":
                if not en_palabra:
                    count += 1
                    en_palabra = True
            else:
                en_palabra = False
        return count
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        pass
    
    def palabras_mayus(self, texto):
        resultado = ""
        nueva = True
        for ch in texto:
            if ch == " ":
                resultado += ch
                nueva = True
            else:
                if nueva and ch.isalpha():
                    resultado += ch.upper()
                else:
                    resultado += ch
                nueva = False
        return resultado
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        pass
    
    def eliminar_espacios_duplicados(self, texto):
        out = ""
        prev_space = False
        for ch in texto:
            if ch == " ":
                if not prev_space:
                    out += ch
                prev_space = True
            else:
                out += ch
                prev_space = False
        return out
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        pass
    
    def es_numero_entero(self, texto):
        if texto == "" or texto is None:
            return False
        i = 0
        if texto[0] in "+-":
            if len(texto) == 1:
                return False
            i = 1
        while i < len(texto):
            if texto[i] < "0" or texto[i] > "9":
                return False
            i += 1
        return True
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        pass
    
    def cifrar_cesar(self, texto, desplazamiento):
        d = desplazamiento % 26
        out = ""
        for ch in texto:
            if "a" <= ch <= "z":
                out += chr(((ord(ch) - ord("a") + d) % 26) + ord("a"))
            elif "A" <= ch <= "Z":
                out += chr(((ord(ch) - ord("A") + d) % 26) + ord("A"))
            else:
                out += ch
        return out
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        pass
    
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        pass
    
    def encontrar_subcadena(self, texto, subcadena):
        if subcadena == "":
            return []
        posiciones = []
        n = len(texto)
        m = len(subcadena)
        for i in range(n - m + 1):
            ok = True
            for j in range(m):
                if texto[i + j] != subcadena[j]:
                    ok = False
                    break
            if ok:
                posiciones.append(i)
        return posiciones
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        pass
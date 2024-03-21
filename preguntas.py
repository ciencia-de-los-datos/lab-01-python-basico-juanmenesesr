"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
nombre_archivo = 'data.csv'

# Abrir el archivo CSV en modo lectura
with open(nombre_archivo, 'r') as file:
    # Leer todas las líneas del archivo
    lineas = file.readlines()



def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma_segunda_columna = sum(int(linea.strip().split('\t')[1]) for linea in open(nombre_archivo))
   
    return suma_segunda_columna


def pregunta_02():


    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    # Crear un diccionario para almacenar la cantidad de registros por letra
    conteo_letras = {}


    # Iterar sobre cada línea y contar la cantidad de registros por letra
    for linea in lineas:
        # Obtener la primera letra de la primera columna
        letra = linea.strip().split()[0][0]  # Se supone que las letras están separadas por espacios y no por comas

            # Incrementar el conteo para la letra actual
        conteo_letras[letra] = conteo_letras.get(letra, 0) + 1

    # Convertir el diccionario en una lista de tuplas y ordenar alfabéticamente por la letra
    lista_conteo = sorted(conteo_letras.items())

    return lista_conteo


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
        # Crear un diccionario para almacenar la suma de la columna 2 por letra
    suma_por_letra = {}


        # Iterar sobre cada línea y sumar la columna 2 por letra
    for linea in lineas:
            # Dividir la línea por tabulaciones para obtener los datos
        datos = linea.strip().split('\t')
            
            # Obtener la letra de la primera columna
        letra = datos[0][0]

            # Obtener el valor de la segunda columna y convertirlo a entero
        valor_columna2 = int(datos[1])

            # Sumar el valor al acumulador correspondiente a la letra
        suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor_columna2

    # Convertir el diccionario en una lista de tuplas y ordenar alfabéticamente por la letra
    lista_suma = sorted(suma_por_letra.items())

    return lista_suma


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    # Crear un diccionario para almacenar la cantidad de registros por mes
    conteo_meses = {}


        # Iterar sobre cada línea y contar la cantidad de registros por mes
    for linea in lineas:
            # Dividir la línea por tabulaciones para obtener los datos
        datos = linea.strip().split('\t')
            
            # Obtener la fecha en formato YYYY-MM-DD desde la tercera columna
        fecha = datos[2]
            
            # Extraer el mes de la fecha (se asume que la fecha está en el formato YYYY-MM-DD)
        mes = fecha.split('-')[1]

            # Incrementar el conteo para el mes actual
        conteo_meses[mes] = conteo_meses.get(mes, 0) + 1

    # Convertir el diccionario en una lista de tuplas y ordenar alfabéticamente por el mes
    lista_conteo = sorted(conteo_meses.items())

    return lista_conteo


def pregunta_05():
    """
    Retorna una lista de tuplas con el valor máximo y mínimo de la columna 2 por cada
    letra de la columna 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    # Abrir el archivo CSV y leer los datos
    with open('data.csv') as file:
        # Crear un diccionario para almacenar los valores máximo y mínimo por letra
        maximos_minimos = {}

        # Leer cada línea del archivo CSV
        for linea in file:
            # Dividir la línea en columnas separadas por tabulaciones
            columna = linea.strip().split('\t')
            letra = columna[0]
            valor = int(columna[1])

            # Si la letra ya está en el diccionario, actualizamos los valores máximo y mínimo
            if letra in maximos_minimos:
                maximos_minimos[letra] = (max(maximos_minimos[letra][0], valor), min(maximos_minimos[letra][1], valor))
            # Si no está, creamos una nueva entrada en el diccionario
            else:
                maximos_minimos[letra] = (valor, valor)

    # Convertir el diccionario en una lista de tuplas
    resultado = [(letra, maximo, minimo) for letra, (maximo, minimo) in maximos_minimos.items()]
    resultado = sorted(resultado, key=lambda x: x[0])

    return resultado

# Ejemplo de uso


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    
    # Diccionario para almacenar los valores asociados a cada clave
    valores = {}

    # Abrir el archivo CSV y leer los datos
    with open('data.csv') as file:
        # Leer cada línea del archivo CSV
        for linea in file:
            # Dividir la línea en columnas separadas por tabulaciones
            columna = linea.strip().split('\t')
            diccionario = columna[4]

            # Dividir el diccionario en claves y valores
            elementos = diccionario.split(',')
            for elemento in elementos:
                clave, valor = elemento.split(':')
                valor = int(valor)

                # Si la clave ya está en el diccionario, actualizamos los valores máximo y mínimo
                if clave in valores:
                    valores[clave] = (min(valores[clave][0], valor), max(valores[clave][1], valor))
                # Si no está, creamos una nueva entrada en el diccionario
                else:
                    valores[clave] = (valor, valor)

    # Convertir el diccionario en una lista de tuplas
    resultado = [(clave, minimo, maximo) for clave, (minimo, maximo) in valores.items()]

    # Ordenar la lista de resultados por la clave
    resultado = sorted(resultado, key=lambda x: x[0])

    return resultado


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
        # Diccionario para almacenar las letras asociadas a cada valor de la columna 2
    asociaciones = {}

    # Abrir el archivo CSV y leer los datos
    with open('data.csv') as file:
        # Leer cada línea del archivo CSV
        for linea in file:
            # Dividir la línea en columnas separadas por tabulaciones
            columna = linea.strip().split('\t')
            valor_columna_2 = int(columna[1])
            letra_columna_1 = columna[0]

            # Si el valor de la columna 2 ya está en el diccionario, agregamos la letra a la lista correspondiente
            if valor_columna_2 in asociaciones:
                asociaciones[valor_columna_2].append(letra_columna_1)
            # Si no está, creamos una nueva entrada en el diccionario con una lista que contiene la letra
            else:
                asociaciones[valor_columna_2] = [letra_columna_1]

    # Convertir el diccionario en una lista de tuplas
    resultado = [(valor, letras) for valor, letras in asociaciones.items()]
    resultado = sorted(resultado, key=lambda x: x[0])


    return resultado


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    # Diccionario para almacenar las letras asociadas a cada valor de la columna 2
    asociaciones = {}

    # Abrir el archivo CSV y leer los datos
    with open('data.csv') as file:
        # Leer cada línea del archivo CSV
        for linea in file:
            # Dividir la línea en columnas separadas por tabulaciones
            columna = linea.strip().split('\t')
            valor_columna_2 = int(columna[1])
            letra_columna_1 = columna[0]

            # Si el valor de la columna 2 ya está en el diccionario, agregamos la letra a la lista correspondiente
            if valor_columna_2 in asociaciones:
                asociaciones[valor_columna_2].append(letra_columna_1)
            # Si no está, creamos una nueva entrada en el diccionario con una lista que contiene la letra
            else:
                asociaciones[valor_columna_2] = [letra_columna_1]

    # Ordenar y eliminar duplicados en las listas de letras asociadas
    for valor in asociaciones:
        asociaciones[valor] = sorted(set(asociaciones[valor]))

    # Convertir el diccionario en una lista de tuplas
    resultado = [(valor, letras) for valor, letras in asociaciones.items()]
    resultado = sorted(resultado, key=lambda x: x[0])

    return resultado



def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    # Diccionario para almacenar el conteo de cada clave
    conteo_claves = {}

    # Abrir el archivo CSV y leer los datos
    with open('data.csv') as file:
        # Leer cada línea del archivo CSV
        for linea in file:
            # Dividir la línea en columnas separadas por tabulaciones
            columnas = linea.strip().split('\t')
            claves = columnas[4].split(',')  # Separar las claves de la columna 5

            # Iterar sobre las claves y actualizar el conteo en el diccionario
            for clave in claves:
                nombre_clave, valor_clave = clave.split(':')
                if nombre_clave in conteo_claves:
                    conteo_claves[nombre_clave] += 1
                else:
                    conteo_claves[nombre_clave] = 1

    # Convertir el diccionario en una lista de tuplas y ordenarla alfabéticamente por la clave
    conteo_claves_ordenado = sorted(conteo_claves.items())

    return conteo_claves_ordenado


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    # Lista para almacenar las tuplas resultado
    resultados = []

    # Abrir el archivo CSV y leer los datos
    with open('data.csv') as file:
        # Leer cada línea del archivo CSV
        for linea in file:
            # Dividir la línea en columnas separadas por tabulaciones
            columnas = linea.strip().split('\t')
            letra = columnas[0]
            cantidad_columna_4 = len(columnas[3].split(','))  # Calcular la cantidad de elementos de la columna 4
            cantidad_columna_5 = len(columnas[4].split(','))  # Calcular la cantidad de elementos de la columna 5
            resultados.append((letra, cantidad_columna_4, cantidad_columna_5))

    return resultados


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    # Diccionario para almacenar las sumas de la columna 2 para cada letra de la columna 4
    sumas_por_letra = {}

    # Abrir el archivo CSV y leer los datos
    with open('data.csv') as file:
        # Leer cada línea del archivo CSV
        for linea in file:
            # Dividir la línea en columnas separadas por tabulaciones
            columnas = linea.strip().split('\t')
            letra_columna_4 = columnas[3].split(',')
            valor_columna_2 = int(columnas[1])

            # Calcular la suma para cada letra de la columna 4
            for letra in letra_columna_4:
                sumas_por_letra[letra] = sumas_por_letra.get(letra, 0) + valor_columna_2

    # Ordenar el diccionario por las claves (letras) alfabéticamente
    sumas_ordenadas = {letra: sumas_por_letra[letra] for letra in sorted(sumas_por_letra)}

    return sumas_ordenadas


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
       # Diccionario para almacenar la suma de los valores de la columna 5 por letra de la columna 1
    sumas_por_letra = {}

    # Abrir el archivo CSV y leer los datos
    with open('data.csv') as file:
        # Leer cada línea del archivo CSV
        for linea in file:
            # Dividir la línea en columnas separadas por tabulaciones
            columnas = linea.strip().split('\t')
            letra_columna_1 = columnas[0]
            valores_columna_5 = columnas[4].split(',')

            # Calcular la suma de los valores de la columna 5
            suma_valores_columna_5 = sum(int(valor.split(':')[1]) for valor in valores_columna_5)

            # Actualizar el diccionario con la suma correspondiente
            sumas_por_letra[letra_columna_1] = sumas_por_letra.get(letra_columna_1, 0) + suma_valores_columna_5

    # Ordenar el diccionario por las claves (letras) alfabéticamente
    sumas_ordenadas = {letra: sumas_por_letra[letra] for letra in sorted(sumas_por_letra)}

    return sumas_ordenadas



# Librería Numpy - arreglos y matrices
print("Librería Numpy - arreglos y matrices")

# *Importación de la librería Numpy
import numpy as nmp

# Funcionalidades de python con matrices
print("\nFuncionalidades de Python con matrices \n")

# Formas de escribir matrtices en python
print("\n- Formas de mostrar matrices en Python, sin uso de Numpy \n")

# Forma 1
print("Forma 1: Creación de la matriz con listas de listas")
# Creación de la matriz a y b con listas de listas
a = [[2,6,1,7],[5,3,8,9],[0,4,2,5]]
print("Matriz 'a': ",a)
b = [[2,3,4,5],[6,5,3,3],[2,4,7,8]]
print("Matriz 'b': ",b)

# Veremos que ocurre al hacer a + b
print("\nCon este arreglo, qué pasa al hacer 'a' + 'b'?\n")
c = a+b
print("El resultado de sumar 'a' + 'b' es: ",c)

# Obervación
print("\nCon este arreglo, el resultado de hacer 'a' + 'b' es una concatenación de tales listas.\n")

# Ahora veremos como acceder a las posiciones de las matrices
print("\n- Posiciones en las matrices: \n")

# Accederemos a algunas posiciones de las matrices anteriores, a[i][j], i corresponde a las filas, que serían las listas internas de la lista mayor, mientras que j corresponde a los elementos específicos de esas listas, que vendrían siendo las columnas
print("\nFila 3 de la matriz 'a': ", a[2])
print("Elemento de la posición 0,2 de la matriz 'a': ",a[0][2])
print("\nFila 1 de la matriz 'b': ", b[1])
print("Elementos de la segunda fila entre la columna 3 y 4 de la matriz 'b': ",b[1][2:])


# Ahora para hacer operaciones entre matrices, se ve la necesidad de definir funciones que permitan realizar diferentes cálculos
print("\n- Operaciones con matrices definidas por funciones")

# Sumar matrices
print("\nSuma de matrices\n")
def suma_matriz(m, n):
    '''Permite sumar dos matrices'''
    if len(n) != len(m):
        print("Las matrices deben contener la misma cantidad de filas para que puedan ser operadas")
    lis = []
    for i in range(0, len(m)):
        lis.append([])
        for j in range(0, len(m[0])):
            lis[i].append(m[i][j] + n[i][j])
    return lis

print("El resultado de sumar la matriz 'a' y la matriz 'b' es: ", suma_matriz(a,b))

# Restar matrices
print("\nResta de matrices\n")
def resta_matriz(m, n):
    '''Permite restar dos matrices'''
    if len(n) != len(m):
        print("Las matrices deben contener la misma cantidad de filas para que puedan ser operadas")
    lis = []
    for i in range(0, len(m)):
        lis.append([])
        for j in range(0, len(m[0])):
            lis[i].append(m[i][j] - n[i][j])
    return lis

print("El resultado de restar la matriz 'a' y la matriz 'b' es: ", resta_matriz(a,b))

# Multiplicar la matriz por un número
print("\nMultiplicación de la matriz por un escalar\n")
def multiplicar_number(number, c):
    '''Permite multiplicar una matriz por un número'''
    lis = []
    for i in range(0, len(c)):
        lis.append([])
        for j in range(0, len(c[0])):
            lis[i].append(c[i][j] * number)
    return lis

print("El resultado de multiplicar la matriz 'a' por el número 3 es: ", multiplicar_number(3,b))

print()
print("--------"*7)

# Ahora, veremos algo similar, pero utlizando la librería Numpy, con la cuál todos estos cálculos se facilitarán
print("\n- Uso de Numpy")

# Para esto debemos importar la librería. Es una buena práctica, importarla desde el inicio del documento, así que lo haremos*

# Ya importada la librería, podemos hacer uso de todas sus funciones y facilidades

# En Numpy, indicamos un arreglo utilizando la palabra clave array(): sirve para almacenar estas grandes secuencias de números. Admite valores de tipo float, se pueden recorrer sus posiciones. Es necesario tener en cuenta, que todos los elementos del array sean del mismo tipo; su tamañano es fijo, no es dinámico como las listas 

print()
# Sabiendo esto, crearemos algunos array y operaremos con ellos
array1 = nmp.array([4,-6,2,-1,6,9])
array2 = nmp.array([2,9,0,8,5,-7])

# Con incluir solamente un float, todos los elementos del array, se convierten en float
array3 = nmp.array([1.4,8,0,3,5,4])
print("Array 1:",array1)
print("Array 2:",array2)
print("Array 3 con elementos float:",array3)

# Arreglo de ceros en float
print("\nArray de ceros en float: ")
array_cero = nmp.zeros(4, dtype=float)
print(array_cero)

# Arreglo de ceros, con dimensión 3x2
print("\nArray de ceros enteros con dimensión 3x2 : ")
array_cerodim = nmp.zeros((3,2),dtype=int)
print(array_cerodim)

# Array de ones
print("\nArray de unos: ")
array_unos = nmp.ones(9)
print(array_unos)

# Array donde se pone el mismo número en todas las posiciones del array, de dimensiones 5x4
print("\nArray con full(): ")
array_full = nmp.full((6,4),20)
print(array_full)

# arange() similar a la función range, con la diferencia de que los números ingresados pueden ser de tipo float
print("\nArray con arange(): ")
array_arange = nmp.arange(2,7.4)
print(array_arange)

# linspace(a, b, n) crea un arreglo de n valores equiespaciados entre a y b
print("\nArray con linspace(): ")
array_linspace = nmp.linspace(2,10,6)
print(array_linspace)

# Ahora veremos como acceder a las posiciones de las matrices
print("\n- Posiciones en arreglos: \n")

# Acceder al elemento de la posición 3 del array2
print("Elemento 4 del array 2: ",array2[3])

# Acceder a los elementos desde el 3 hasta el 6 del array1
print("\nElementos desde el 3 hasta 6 del array 1: ",array1[2:])

# Acceder al último elemento array3
print("\nÚltimo elemento del array 3 : ",array3[-1])

# Operaciones entre arreglos 
print("\n- Operaciones entre arreglos: \n")

# Suma entre array1 y array2
print("Suma entre array 1 y array 2")
suma1y2 = array1 + array2
print("El resultado es: ", suma1y2) 

# Suma entre array1 y array3
print("\nSuma entre array 1 y array 3")
suma1y3 = array1+array3
print("El resultado es: ", suma1y3) 

# Resta entre array3 y array2
print("\nResta entre array 3 y array 2")
resta3y2 = array3 - array2
print("El resultado es: ", resta3y2) 

# Resta entre array2 y array2
print("\nResta entre array 2 y array 2")
resta2y2 = array2 - array2
print("El resultado es: ", resta2y2) 

# Multiplicación por un escalar
print("\nMultiplicación de array 2 por 5:")
mult5array2 = array2 * 5
print("El resultado es: ", mult5array2) 

# Elevar un arreglo a una potencia
print("\nElevar array 1 a la potencia 3:")
poten3array1 = array1 ** 3
print("El resultado es: ", poten3array1) 

# Multiplicación de arreglos
print("\nMultiplicación de array 3 por array 1:")
multarray3x1 = array3 * array1
print("El resultado es: ", multarray3x1 ) 

# Comparación de arreglos: Las operaciones relacionales también se aplican elemento a elemento, y retornan un arreglo de valores booleanos
print("\nComparar array 2 con array 1:")
comparray2y1 = array2 > array1
print("Son los elementos del array 2 mayores que el array 1?: ", comparray2y1 ) 

# Para reducir el arreglo de booleanos a un único valor, se puede usa any y all. any retorna True si al menos uno de los elementos es verdadero, mientras que all retorna True sólo si todos lo son 

# Con any
print("\nComparar array 1 con array 3 con any:")
comparray3y1 = any(array1 < array3)
print("Algún elemento del array 1 es menor que el elemento del array 3?: ", comparray3y1 ) 

# con all
print("\nComparar array 1 con array 3 con all:")
comparray3y1all = all(array1 < array3)
print("Todos los elementos del array 1 menores que el array 3?: ", comparray3y1all) 

# con !=
print("\nComparar array 1 con array 3 :")
comparray3y1dif = array1 != array3
print("El array 1 es diferente array 3?: ", comparray3y1dif) 

print()
# Matrices con numpy
print("\nMatrices de numpy:")
A = nmp.matrix([[3,6,7],[2,4,1],[8,3,4]])
B = nmp.matrix([[5,2,1],[5,7,8],[3,9,1]])
print("\nMatriz A: \n", A)

print("\nMatriz B: \n", B)

# Suma de matrices
print("\nSuma de matrices:")
sumamatr = A+B
print("\nEl resultado de la suma de la matriz A y B es: \n", sumamatr)

# Resta de matrices
print("\nResta de matrices:")
restamatr = B-A
print("\nEl resultado de la resta de la matriz B y A es: \n", restamatr)

# Multiplicación de matrices
print("\nMultiplicación de matrices:")
multmatr = A*B
print("\nEl resultado de la multiplicación de la matriz A y B es: \n", multmatr)

# Multiplicación de un escalar por matriz B
print("\nMultiplicar la matriz B por 7:")
multi7amatr = B*7
print("\nEl resultado de multiplicar la matriz B por 7: \n", multi7amatr)

# Elevar matriz a una potencia
print("\nElevar la matriz A a la 4:")
potenmatr = A**4
print("\nEl resultado de elevar la matriz A a la potencia 4 es: \n", potenmatr)

# Webgrafía: http://progra.usm.cl/apunte/materia/arreglos.html
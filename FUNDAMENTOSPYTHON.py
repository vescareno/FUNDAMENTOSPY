def nuevoTema(tema): 
    print("\n-----------", tema, "--------\n")

if __name__ == "__main__":

    nuevoTema("Operadores aritméticos")
    print("Operador suma, 5+3: ", 5+3)
    print("Operador resta 10-2:", 10-2)
    print("Operador multriplicación 3*3:", 3*3)
    print("Operador división 20/3:", 20/3)
    print("Operadar división entera 20//3:", 20//3)
    print("Operador módulo 20%3:", 20%3)
    print("Operador cambio de signo -3:", -3)
    print("Operador exponente 5**5", 5**5)

    '''Gato para mensaje de una línea
    Tres comillas simples para varias'''
    nuevoTema("Operadores Lógicos")
    print("True and True:", True and True) #Operador logíco and
    #Imprimir la tabla de operador and
    print("False and True:", False and True)
    print("False and False:", False and False)
    print("True and True:", True and True)
    print("True and False:", True and False)
    print("False and True:", False and True)
    print("False and False:", False and False)
    print("True or False:", True or False)
    print("False or True:", False or True)
    print("False or False:", False or False)
    print("True or True:", True or True)
    print("True or False:", True or False)
    print("False or True:", False or True)
    print("False or False:", False or False)
    print("not False:", not False)
    print("not True:", not True)
    nuevoTema("Operadores de comparación")
    print("Es igual que:", 1==1)
    print("Es distinto de:", 1!=1)
    print("Es menor que:", 1<1)
    print("Es menor o igual que:", 1<=1)
    print("Es mayor que:", 1>1)
    print("Es mayor o igual que:", 1>=1)
    print("1==1:", 1==1)
    print("1!=1:", 1!=1)
    print("1<1:", 1<1)
    print("1<=1:", 1<=1)
    print("1>1:", 1>1)
    print("1>=1:", 1>=1)


    nuevoTema("Variables")
    variable1 = 10
    _variable2 = 6.2547
    Variable3 = "pepe"
    nombreVariable = 8
    nombre_variable = 34.2
    print(variable1, _variable2, Variable3, nombreVariable, nombre_variable)


    a, b, c = 5, 10.8, "Hola"
    print(a)
    print(b)
    print(c)

    nuevoTema("Enteros")
    w = 105
    x = 324732492384793
    y = -58
    z = 0b00110011
    h = 0xFF

    print(w, type (w))
    print(x, type (x))
    print(y, type (y))
    print(z, type (z))
    print(h, type (h))

    nuevoTema("Flotantes")
    x = 1234.56
    print(x, type (x))
    y = -9874.56
    print(y, type(y))

    nuevoTema("Números complejos")
    x = -46j
    y = 12 + 45j
    z = 2j
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))

    nuevoTema("Booleanos")
    lis = []
    print(lis, "is", bool(lis))

    nuevoTema("Listas")
    a = [10, 20.5, "Python List"]
    print(a)
    print(a[1])
    a[1] = "Hola"
    print(a)

    nuevoTema("Tuplas")
    t = (25, "Tupla", 1 + 1j)
    print(t)
    print(t[1])

    nuevoTema("Cadenas")
    cadena1 = "Esto es una cadena"
    cadena2 = 'Esto también es una cadena'
    print(cadena1, type(cadena1))
    print(cadena2, type(cadena2))
    print(cadena1[5])

    cadenaMultilinea = '''Esto es una cadena
    de varias líneas    con tabulares y
    saltos
    de
    línea'''
    print(cadenaMultilinea, type(cadenaMultilinea))

    cadena3 = "Hola" * 5
    print(cadena3)

    nuevoTema("Conjuntos")
    conjunto = {10, 20, 30, 40, 10, 50}
    print(conjunto)

    nuevoTema("Diccionarios")
    diccionario = {"Nombre": "Conrado",
                "Edad": 38,
                "Tel": 12345678}
    print(diccionario)
    print(diccionario["Nombre"])

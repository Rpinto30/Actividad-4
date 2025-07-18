print("-"*20+"Bienvenido"+"-"*20)

regist_students = {}

while True:
    print("-"*10+"Opciones"+"-"*10)
    print("  1) Agregar Estudiante\n  2) Mostrar Lista de Estudiantes\n  3) Calcular promedio general\n  4) Salir")
    option = int(input(">Selecciona una opcion: "))
    if option == 1:
        print("\n"+"-"*20+"Agrega a un estudiante"+"-"*20)
        name = input("Ingresa el nombre del nuevo estudiante:")
        points = int(input("Ingresa la nota del nuevo estudiante: "))
        #FUNCION SETDEFAULT PARA AGREGAR UN UNICO NOMBRE
            #Sacado de: https://www.w3schools.com/python/ref_dictionary_setdefault.asp
        regist_students.setdefault(name, points)
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    else:
        print("Entrada no valida")
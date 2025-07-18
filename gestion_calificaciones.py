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

        print(f"\nEl estudiante {name} ha sido agregado con {points} puntos\n")
    elif option == 2:
        if len(regist_students) > 0:
            print("\n" + "-" * 20 + "Mostrar lista de estudiantes" + "-" * 20)
            print(f"{'Nombre del estudiante':<50}{'Nota'}")
            for i in regist_students: print(f"{i:<50}{regist_students[i]}")
        else: print("No se han encontrado estudiantes")
    elif option == 3:
        if len(regist_students) > 0:
            sum = 0
            for i in regist_students: sum += regist_students[i]
            print(f"\nEl promedio general de los estudiantes es: {round(sum/len(regist_students), 2)}\n")
        else: print("No se han encontrado estudiantes")
    elif option == 4: break
    else: print("Entrada no valida")

print("\nHasta pronto!\n")
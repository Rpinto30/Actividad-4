PRICE, PRICE_STUDENT = 50, 35
days = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabadado', 'domingo']

print("-"*10+"Bienvenido"+"-"*10)
age = int(input("Ingrese su edad: "))
print("-"*30)
print("  1) Lunes\n  2) Martes\n  3) Miercoles\n  4) Jueves\n  5) Viernes\n  6) Sabadado\n  7) Domingo")
day = int(input("Ingrese el día de la semana: "))
print("-"*30)
print("  1) Si\n  2) No")
student = int(input("Es usted un estudiante?: "))
print('\n')

if age < 0: print("Lo sentimos, la edad que ingresó no es valida")
elif  0 > day > 7: print("Lo sentimos, el día que ingreso no es valido")
elif 1 > student > 2: print("Lo sentimos, entrada invalida en la pregunta anterior")
else:
    if age >= 13:
        total = PRICE
        if student == 1: total = PRICE_STUDENT
        print(f"Precio total por la entrada: Q{total}")
        if day == 3: print("Felicidades! Miercoles de 2x1")

    else:
        print("Denegación: Usted no puede accder a peliculas +15")



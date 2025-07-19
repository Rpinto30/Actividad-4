deps = ['Alta Verapaz','Baja Verapaz', 'Chimaltenango','Chiquimula','Guatemala', 'El Progreso','Escuintla','Huehuetenango','Izabal','Jalapa','Jutiapa','Peten',  'Quetzaltenango','Quiche','Retalhuleu','Sacatepequez','San Marcos','Santa Rosa','Solola','Suchitepequez','Totonicapan','Zacapa']

name = input("> Ingrese su nombre completo: ")
dpi = input("> Ingrese su dpi: ")

#DEPARTAMENTOS
print("-"*30)
print(f"{'   1)Alta Verapaz':<20}{'   2)Baja Verapaz':<20}{'   3)Chimaltenango':<20}{'   4)Chiquimula'}")
print(f"{'   5)Guatemala':<20}{'   6)El Progreso':<20}{'   7)Escuintla':<20}{'   8)Huehuetenango'}")
print(f"{'   9)Izabal':<20}{'   10)Jalapa':<20}{'   11)Jutiapa':<20}{'   12)Peten'}")
print(f"{'   13)Quetzaltenango':<20}{'   14)Quiche':<20}{'   15)Retalhuleu':<20}{'   16)Sacatepequez'}")
print(f"{'   17)San Marcos':<20}{'   18)Santa Rosa':<20}{'   19)Solola':<20}{'   20)Suchitepequez'}")
print(f"{'   21)Totonicapan':<20}{'   22)Zacapa'}")
dep_index = int(input("> Ingrese el departamento donde recide: "))


if 1 <=dep_index <= 22:
    dep = deps[dep_index - 1]
    year = int(input("> Ingrese su año de nacimiento: "))
    if len(name) < 5: print(f"\nLo sentimos, nombre {name} menor de 5 letras")
    elif len(dpi) != 13: print(f"\nLo sentimos, dpi {dpi} no posee 13 digitos")
    else:
        if dep_index == 1 or dep_index == 12:
            if year >= 17: print(f"\nBienvenido {name}, su centro de votación está en {dep}")
        else:
            if year >= 18: print(f"\nBienvenido {name}, su centro de votación está en {dep}")
else:
    print("Lo siento, entrada invalida en la elección de departamentos")

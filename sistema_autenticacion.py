from os import access

users = {'jorge': 'password', 'miguel': '12345678', 'federico': 'abcdefgh'}

accs = False
attempts = 3

while attempts > 0:
    name = input("\nIngrese el nombre del usuario: ")
    password = input("Ingrese la contraseña del usuario: ")

    for usr in users:
        if usr == name.lower() and users[usr] == password:
            accs = True
            break
    else:
        print("\nCredenciales no validad, intente nuevamente")
        attempts -= 1
        continue
    break

if accs:
    print("\n"+"-"*10+"Bienvenido"+"-"*10)
    print("  1) Ver Perfil\n  2) Cambiar contraseña\n  3)Cerrar sesión")
else: print("Acceso denegado")
directions = ['norte', 'este', 'sur', 'oeste']

print("-"*10+"Calculadora de rumbos"+"-"*10)
print("  1) Norte\n  2) Este\n  3) Sur\n  4) Oeste")

dir_1 = int(input("Ingrese la dirección 1: "))
dir_2 = int(input("Ingrese la dirección 2: "))

print(f"\nPara ir de {directions[dir_1-1]} a {directions[dir_2-1]}:")

if abs(dir_1 - dir_2) > 3:
    print("Lo siento, no seleccionó una entrada valida")
elif dir_1 == dir_2:
    print(f"Debe seguir recto al {directions[dir_1-1]}")
elif abs(dir_1-dir_2) == 2:
    #SI UNO IMAGINA UN CIRCULO DONDE ESTEN OPUESTAS ESAS DIRECCIONES, AL ESTAR CONTRARIAS LA RESTA SIEMPRE ES DE 2
    print(f"Debe ir recto hacia la {directions[dir_2-1]}.")
elif abs(dir_1-dir_2) == 1 or abs(dir_1-dir_2) == 3:
    if dir_1 == 1 or dir_1 == 3: print(f"Debe ir hacia el {directions[dir_1-1][:3] + directions[dir_2-1]}.")
    else: print(f"Debe ir hacia el {directions[dir_2-1][:3] + directions[dir_1-1]}.")



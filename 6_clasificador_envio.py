weight = int(input("Ingrese peso del paquete en Kg: "))
dist = int(input("Ingrese la distancia del envio en Km: "))

print("-"*10)
print("  1) Sí\n  2) No")
urg = int(input("Es de urgencia?: "))

print("-"*10)
print("  1) Pequeño\n  2) Mediano\n  3) Grande")
size = int(input("Ingrese el tamaño del paquete: "))

#Asumiendo costo base como peso + distancia
print("-"*10+"Coste del envio"+"-"*10)

total = weight + dist
print(f"\n  Total inicial: Q{total:.2f}")

if urg==1:
    total += 50
    print(f"  Urgente +50: Q{total:.2f}")
if size == 3:
    total += 30
    print(f"  Grande +30: Q{total:.2f}")
if urg == 2 and weight < 5:
    total -= 20
    print(f"  Descuento no urgente y menor de 5Kg -20: Q{total:.2f}")
print(f"\n  Total: Q{total:.2f}")
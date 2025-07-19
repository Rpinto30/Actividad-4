print("-"*10+"Bienvenido"+"-"*10)

subtotal = 0
while True:
    prod = float(input("> Ingresa precios de productos (-1 para terminar): "))
    if prod == -1: break
    else: subtotal += prod

print("\nDesea dejar propina?")
op_prop = int(input("  1) Sí\n  2) No\nEliga una opción: "))

if op_prop == 1: percent_prop = int(input("Ingresa el porcentaje de propina que deseas dejar: "))

print("\nTiene tarjeta de cliente frecuente?")
op_card = int(input("  1) Sí\n  2) No\nEliga una opción: "))


print("-"*10+"Total detallado"+"-"*10)
print(f"    Subtotal: {subtotal:.2f}")
total = subtotal + subtotal * 0.12
print(f"    IVA (12%): {total:.2f}")
if op_prop == 1:
    total += total*percent_prop/100
    print(f"    Propina agregada ({percent_prop}%): {total:.2f}")
if op_card == 1:
    total -= total * 0.1
    print(f"    Descuento (10%): {total:.2f}")

print(f"\n Total: {total:.2f}")

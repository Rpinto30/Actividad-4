print("-"*20+"Calculadora de impuestos a pagar"+"-"*20)
ingr = int(input("Ingresa el ingreso anual: "))
dep = int(input("Ingresa número de dependientes: "))

if ingr >= 0 and dep >= 0:
    if ingr < 40000 and dep > 2: print("\nUsted no paga impuestos")
    else:
        percent = 0
        if 0 <= ingr <= 30000: percent = 0.05
        elif 30001 <= ingr <= 60000: percent = 0.1
        elif 60001 <= ingr <= 100000: percent = 0.15
        else: percent = 0.2
        final_tax = percent * (ingr - 1000 * dep)

        print(f"\nUsted debe de pagar Q{final_tax} en impuestos\n")
else: print("\nEntrada invalida")
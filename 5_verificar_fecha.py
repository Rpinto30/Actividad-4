days_list = ['Domingo','Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']

#EXPORTADOS DEL EJERCICIO NO.10
def is_leap(year_leap): return (year_leap % 4 == 0 and year_leap % 100 != 0) or (year_leap % 400 == 0)
def month_true(month_day, year_day):
    if month_day == 2:  #FEBRERO CONTANDO SI ES BICIESTO
        if is_leap(year_day): return 29
        else: return 28
    elif month_day in [4, 6, 9, 11]: return 30 #MESES CON 30 DÍAS
    elif month_day in [1, 3, 5, 7, 8, 10, 12]: return 31 #MESES CON 31 DÍAS
    else: return 0 #entrada no valida

print("-"*20+"Formula de Zeller"+"-"*20)
day = int(input("Ingrese día: "))
month = int(input("Ingrese mes: "))
year = int(input("Ingrese año: "))

if year > 0 and 1 <= month <= 12 and 1 <= day <= month_true(month, year):
    a = int((14-month)/12)
    y = year-a
    m = int(month+12*a-2)
    d = int((day+y+y/4-y/100+y/400+(31*m)/12))%7


    print(f"\nLa fecha {day}/{month}/{year} fue un {days_list[d]}")
else: print("\nLo siento, la fecha ingresada no existe")
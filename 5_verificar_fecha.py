print("-"*20+"Formula de Zeller"+"-"*20)
day = int(input("Ingrese día: "))
month = int(input("Ingrese mes: "))
year = int(input("Ingrese año: "))

days_list = ['Domingo','Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']

a = int((14-month)/12)
y = year-a
m = int(month+12*a-2)
d = int((day+y+y/4-y/100+y/400+(31*m)/12))%7


print(f"\nLa fecha {day}/{month}/{year} fue un {days_list[d]}")
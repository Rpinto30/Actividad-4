#dates = [] #[20,7,2025]

dates = [[21,7,2024],[30,8,2025]]
#dates = [[19,7,2025],[30,6,2025]]

#Detección de días segun el mes
def is_leap(year_leap): return (year_leap % 4 == 0 and year_leap % 100 != 0) or (year_leap % 400 == 0)
def month_true(month_day, year_day):
    if month_day == 2:  #FEBRERO CONTANDO SI ES BICIESTO
        if is_leap(year_day): return 29
        else: return 28
    elif month_day in [4, 6, 9, 11]: return 30 #MESES CON 30 DÍAS
    elif month_day in [1, 3, 5, 7, 8, 10, 12]: return 31 #MESES CON 31 DÍAS
    else: return 0 #entrada no valida

def days_on_month(date): return month_true(date[1], date[2]) - date[0]

#Solo imprimen mensajes
def mayor_date(date_1, date_2): print(f"La fecha {date_1[0]}/{date_1[1]}/{date_1[2]} es mayor a la fecha {date_2[0]}/{date_2[1]}/{date_2[2]}")
def equals_date(date_1, date_2, equal): print(f"La fecha {date_1[0]}/{date_1[1]}/{date_1[2]} esta en el mismo {equal} que {date_2[0]}/{date_2[1]}/{date_2[2]}")
'''
for i in range(1,3):
    print("-"*10+f"Fecha {i}"+"-"*10)
    day = int(input(f"Es el DÍA de la fecha {i}: "))
    month = int(input(f"Es el MES de la fecha {i}: "))
    year = int(input(f"Es el AÑO de la fecha {i}: "))

    if year > 0 and 1 <= month <= 12 and 1 <= day <= month_true(month, year): dates.append([day, month, year])
    else:
        print(f"\nLo siento, la fecha {i} es invalida")
        break
'''
if len(dates) > 0:
    print("")
    days_between = 0
    if dates[0][2] > dates[1][2]: #FECHA 1 MAYOR QUE FECHA 2
        mayor_date(dates[0], dates[1])
        if dates[0][1] == dates[1][1]: equals_date(dates[0], dates[1], "mes")
    elif dates[1][2] > dates[0][2]: #FECHA 2 MAYOR QUE FECHA 1
        mayor_date(dates[1], dates[0])
        if dates[0][1] == dates[1][1]: equals_date(dates[0], dates[1], "mes")
    else:#AÑOS IGUALES
        equals_date(dates[0], dates[1], "año")
        if dates[0][1] > dates[1][1]: #FECHA 1 MAYOR QUE FECHA 2
            mayor_date(dates[0], dates[1])
            #days_between = abs(month_true(dates[1][1], dates[1][2])-dates[1][0]+1) + dates[0][0]
        elif dates[0][1] < dates[1][1]: #FECHA 2 MAYOR QUE FECHA 1
            mayor_date(dates[1], dates[0])
            #days_between = abs(month_true(dates[0][1], dates[0][2]) -dates[0][0]+1) + dates[1][0]
        else: #MESES IGUALES
            if dates[0][0] == dates[1][0]: print("Ambas fechas son iguales")
            else:
                days_between += abs(dates[0][0] - dates[1][0])
                equals_date(dates[0], dates[1], "mes y año")

    print(days_on_month([20,7,2025]))
    print(f"\nLos días que han pasado entre ambas fechas son: {days_between}")
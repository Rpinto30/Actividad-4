students = {}

for i in range(5):
    print('\n'+"-"*20+f"Estudiante {i+1}"+"-"*20)
    list_notes = []
    name = input(f"Ingrese el nombre del estudiante {i+1}: ")
    for j in range(3):
        note = int(input(f"  Ingrese la nota {j+1} del estudiante {name}: "))
        list_notes.append(note)
    list_notes.append(round(sum(list_notes)/3, 2))
    students[name] = list_notes
for i in students:
    if all(students[i][-1] < 70 for e in students[i]):
        for k in range(len(students[i])):
            if students[i][k] + 5 <= 100: students[i][k] += 5
            else: students[i][k] = 100
        prom = round(sum(students[i]) / 3, 2)

    students[i].append(round(sum(students[i])/3, 2))
    #APLICACION DE CURVA


print('\n'+f"{'Nombre':<10}{'Promedio'}")
for i in students:print(f"{i:<10}{students[i][3]}")
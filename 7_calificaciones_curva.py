students = {}

for i in range(2):
    print('\n'+"-"*20+f"Estudiante {i+1}"+"-"*20)
    list_notes = []
    name = input(f"Ingrese el nombre del estudiante {i+1}: ")
    for j in range(3):
        note = int(input(f"  Ingrese la nota {j+1} del estudiante {name}: "))
        list_notes.append(note)
    prom = round(sum(list_notes)/3, 2)
    if prom < 70:
        for k in range(len(list_notes)):
            if list_notes[k] + 5 <= 100: list_notes[k] += 5
            else: list_notes[k] = 100
        prom = round(sum(list_notes) / 3, 2)

    list_notes.append(round(sum(list_notes)/3, 2))
    #APLICACION DE CURVA
    students[name] = list_notes

print('\n'+f"{'Nombre':<10}{'Promedio'}")
for i in students:print(f"{i:<10}{students[i][3]}")
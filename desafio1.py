# Lista de calificaciones de los estudiantes
calificaciones = [5, 8, 9, 4, 7, 6, 10, 3, 8, 2, 7, 5,10]

# Inicializamos los contadores de aprobados y desaprobados
aprobados = 0
desaprobados = 0

# Recorremos cada calificación en la lista
for calificacion in calificaciones:
    # Verificamos si la calificación es aprobatoria
    if calificacion >= 7:
        aprobados += 1
    else:
        desaprobados += 1

# Imprimimos los resultados
print(f"Cantidad de estudiantes aprobados: {aprobados}")
print(f"Cantidad de estudiantes desaprobados: {desaprobados}")

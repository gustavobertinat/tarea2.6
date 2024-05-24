# Solicitamos todas las calificaciones en una sola entrada, separadas por comas
calificaciones_str = input("Ingrese todas las calificaciones (entre 1 y 12) separadas por comas: ")

# Convertimos la cadena de calificaciones a una lista de enteros
calificaciones = [int(c) for c in calificaciones_str.split(',') if c.strip().isdigit()]

# Filtramos las calificaciones que están fuera del rango permitido (1 a 12)
calificaciones_validas = [c for c in calificaciones if 1 <= c <= 12]

# Verificamos si hay calificaciones válidas
if calificaciones_validas:
    # Calculamos la suma de las calificaciones válidas
    suma_calificaciones = sum(calificaciones_validas)
    # Contamos las calificaciones válidas
    contador_asignaturas = len(calificaciones_validas)
    # Calculamos el promedio
    promedio = suma_calificaciones / contador_asignaturas
    # Imprimimos el promedio con dos decimales
    print(f"El promedio de las calificaciones es: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones válidas.")

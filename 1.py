# Definir un diccionario de eventos
eventos = {
    "2024-4-13": ["Reunión de trabajo", "Almuerzo con amigos"],
    "2024-4-18": ["Visita al médico", "Clase de natacion miguel"],
    "2024-6-15": ["cumpleaños", "almuerzo con salo"],
    "2024-11-30": ["cumpleaños de mamá", "hacer tarea de matematicas"],
    "2024-12-1": ["aniversario mamá", "cita de la abuela"],
    "2025-2-27": ["aniversario papa", "salir con la abuela"],
}

# Obtener la fecha del  usuario
fecha = input("Ingresa la fecha en formato YYYY-MM-DD: ")

# verificar si hay  eventos programados para esa fecha
if fecha in eventos:
    print(f"Eventos programados para el {fecha}:")
    for evento in eventos[fecha]:
        print(f"- {evento}")
    else:
        print(f"Eventos programados")
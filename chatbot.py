empleados = {
    "45305689": {"nombre": "Juan", "dias": 15},
    "38456378": {"nombre": "Ana", "dias": 0},
    "44557398": {"nombre": "Pedro", "dias": 8}
}

print("=== SOLICITUD DE VACACIONES ===")

dni = input("Ingrese DNI: ")

if dni in empleados:
    if empleados[dni]["dias"] > 0:
        print("Solicitud aprobada")
        print("Dias disponibles:", empleados[dni]["dias"])
    else:
        print("Solicitud rechazada")
        print("No posee dias disponibles")
else:
    print("DNI inexistente")
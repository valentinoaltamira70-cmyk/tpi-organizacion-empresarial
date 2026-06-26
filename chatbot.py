empleados = {
    "45305689": {"nombre": "Juan", "dias": 15},
    "38456378": {"nombre": "Ana", "dias": 0},
    "44557398": {"nombre": "Pedro", "dias": 8}
}

print("=" * 40)
print("     SISTEMA DE SOLICITUD DE VACACIONES")
print("=" * 40)

dni = input("Ingrese el DNI del empleado: ").strip()


if not dni.isdigit() or len(dni) != 8:
    print("\n DNI inválido. Debe contener 8 números.")

elif dni in empleados:
    empleado = empleados[dni]

    print("\n--- DATOS DEL EMPLEADO ---")
    print(f"Nombre: {empleado['nombre']}")
    print(f"Días disponibles: {empleado['dias']}")

    print("\n--- RESULTADO DE LA SOLICITUD ---")

    if empleado["dias"] > 0:
        print(" Solicitud APROBADA.")
        print("El empleado posee días de vacaciones disponibles.")
    else:
        print(" Solicitud RECHAZADA.")
        print("El empleado no posee días de vacaciones disponibles.")

else:
    print("\n El DNI ingresado no existe en la base de datos.")

print("\nGracias por utilizar el sistema.")

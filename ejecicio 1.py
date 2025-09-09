# Nombre completo: [daner]
# Ejercicio 1 - Tabla de multiplicar hasta un número dado

def ejercicio1():
    """
    Programa que genera tablas de multiplicar desde 1 hasta un número dado
    e identifica cuál fue la tabla más larga.
    """
    # Pedir número entero positivo al usuario
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            if numero > 0:
                break
            else:
                print("Por favor, ingrese un número positivo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # Variable para controlar la tabla más larga
    tabla_mas_larga = 0
    longitud_maxima = 0
    
    # Generar tablas de multiplicar desde 1 hasta el número ingresado
    for i in range(1, numero + 1):
        print(f"\n--- Tabla del {i} ---")
        
        # Contar la longitud de esta tabla (multiplicamos hasta 10 por convención)
        longitud_actual = 10
        
        # Generar la tabla de multiplicar del número i
        for j in range(1, 11):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")
        
        # Verificar si esta es la tabla más larga
        # Nota: En este caso todas las tablas tienen la misma longitud (10)
        # Pero consideraremos "más larga" a la que tenga resultados más grandes
        if i > tabla_mas_larga:
            tabla_mas_larga = i
            longitud_maxima = longitud_actual
    
    # Mostrar resultado final
    print(f"\n--- RESUMEN ---")
    print(f"Se generaron {numero} tablas de multiplicar.")
    print(f"La tabla 'más larga' (con valores más altos) fue la del número: {tabla_mas_larga}")

# Ejecutar el ejercicio
if __name__ == "__main__":
    ejercicio1()

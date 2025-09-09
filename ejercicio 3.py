# Nombre completo: [danner]
# Ejercicio 3 - Función con *args y **kwargs para analizar números

def analizar_numeros(*args, **kwargs):
    """
    Función que analiza una lista de números y muestra pares/impares según las opciones.
    
    Args:
        *args: Números enteros a analizar
        **kwargs: Opciones de configuración
            - mostrar_pares (bool): Si mostrar números pares
            - mostrar_impares (bool): Si mostrar números impares
    """
    # Obtener opciones de configuración (valores por defecto)
    mostrar_pares = kwargs.get('mostrar_pares', False)
    mostrar_impares = kwargs.get('mostrar_impares', False)
    
    # Si no se especifica ninguna opción, mostrar ambos
    if not mostrar_pares and not mostrar_impares:
        mostrar_pares = True
        mostrar_impares = True
    
    # Separar números pares e impares
    numeros_pares = []
    numeros_impares = []
    
    for numero in args:
        if isinstance(numero, int):  # Verificar que sea entero
            if numero % 2 == 0:
                numeros_pares.append(numero)
            else:
                numeros_impares.append(numero)
        else:
            print(f"Advertencia: {numero} no es un número entero, se ignora.")
    
    # Mostrar resultados según las opciones
    if mostrar_pares and numeros_pares:
        print(f"Números pares: {', '.join(map(str, numeros_pares))} (Total: {len(numeros_pares)})")
    elif mostrar_pares and not numeros_pares:
        print("Números pares: Ninguno (Total: 0)")
    
    if mostrar_impares and numeros_impares:
        print(f"Números impares: {', '.join(map(str, numeros_impares))} (Total: {len(numeros_impares)})")
    elif mostrar_impares and not numeros_impares:
        print("Números impares: Ninguno (Total: 0)")

def ejercicio3():
    """
    Programa principal para probar la función analizar_numeros
    """
    print("=== ANÁLISIS DE NÚMEROS ===")
    
    # Ejemplo 1: Mostrar solo pares
    print("\n1. Ejemplo mostrando solo números pares:")
    analizar_numeros(1, 2, 3, 4, 5, 6, mostrar_pares=True)
    
    # Ejemplo 2: Mostrar solo impares
    print("\n2. Ejemplo mostrando solo números impares:")
    analizar_numeros(1, 2, 3, 4, 5, 6, mostrar_impares=True)
    
    # Ejemplo 3: Mostrar ambos
    print("\n3. Ejemplo mostrando pares e impares:")
    analizar_numeros(1, 2, 3, 4, 5, 6, mostrar_pares=True, mostrar_impares=True)
    
    # Ejemplo 4: Sin opciones (muestra ambos por defecto)
    print("\n4. Ejemplo sin opciones especificadas:")
    analizar_numeros(10, 15, 20, 25, 30)
    
    # Ejemplo 5: Con números más grandes
    print("\n5. Ejemplo con rango más amplio:")
    analizar_numeros(100, 101, 102, 103, 104, 105, mostrar_pares=True)
    
    # Ejemplo interactivo
    print("\n=== MODO INTERACTIVO ===")
    numeros_usuario = []
    
    print("Ingrese números enteros (escriba 'fin' para terminar):")
    while True:
        entrada = input("Número: ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = int(entrada)
            numeros_usuario.append(numero)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    
    if numeros_usuario:
        print("\nSeleccione qué desea mostrar:")
        print("1. Solo pares")
        print("2. Solo impares") 
        print("3. Ambos")
        
        while True:
            try:
                opcion = int(input("Opción (1-3): "))
                if opcion in [1, 2, 3]:
                    break
                else:
                    print("Seleccione una opción válida (1-3)")
            except ValueError:
                print("Ingrese un número válido")
        
        print(f"\nResultado para los números: {numeros_usuario}")
        
        if opcion == 1:
            analizar_numeros(*numeros_usuario, mostrar_pares=True)
        elif opcion == 2:
            analizar_numeros(*numeros_usuario, mostrar_impares=True)
        else:
            analizar_numeros(*numeros_usuario, mostrar_pares=True, mostrar_impares=True)
    else:
        print("No se ingresaron números.")

# Ejecutar el ejercicio
if __name__ == "__main__":
    ejercicio3()

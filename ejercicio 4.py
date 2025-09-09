# Nombre completo: [daner]
# Ejercicio 4 - Simulador de cajero automático con manejo de excepciones

def cajero_automatico():
    """
    Simula un cajero automático con validaciones usando try-except
    """
    print("=== CAJERO AUTOMÁTICO ===")
    
    # 1. Pedir saldo inicial
    while True:
        try:
            saldo_inicial = int(input("Ingrese su saldo inicial: $"))
            if saldo_inicial >= 0:
                break
            else:
                print("El saldo inicial no puede ser negativo.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido para el saldo.")
    
    saldo_actual = saldo_inicial
    print(f"Saldo inicial registrado: ${saldo_actual:,}")
    
    # Bucle principal para realizar retiros
    while True:
        print(f"\nSaldo actual: ${saldo_actual:,}")
        print("¿Desea realizar un retiro? (s/n)")
        
        continuar = input("Respuesta: ").lower()
        if continuar != 's':
            print("Gracias por usar nuestro cajero automático.")
            break
        
        # 2. Pedir monto a retirar
        print(f"\nSaldo disponible: ${saldo_actual:,}")
        monto_retiro = input("Ingrese el monto a retirar: $")
        
        try:
            # 3. Validaciones con try-except
            
            # Convertir a float para manejar decimales
            monto = float(monto_retiro)
            
            # Validar si el monto es negativo
            if monto < 0:
                print("Error: No se permiten valores negativos.")
                continue
            
            # Validar si el monto es cero
            if monto == 0:
                print("Error: El monto a retirar debe ser mayor que cero.")
                continue
            
            # Validar si hay fondos suficientes
            if monto > saldo_actual:
                print("Error: Fondos insuficientes.")
                print(f"Saldo disponible: ${saldo_actual:,}")
                print(f"Monto solicitado: ${monto:,}")
                continue
            
            # Si todas las validaciones pasan, realizar el retiro
            saldo_actual -= monto
            print(f"\n✓ Retiro exitoso!")
            print(f"Monto retirado: ${monto:,}")
            print(f"Saldo restante: ${saldo_actual:,}")
            
            # Mostrar alerta si el saldo es bajo
            if saldo_actual < (saldo_inicial * 0.1):  # Menos del 10% del saldo inicial
                print("⚠️  Advertencia: Su saldo está bajo.")
        
        except ValueError:
            # Error si no se puede convertir a número
            print("Error: Debe ingresar un número válido.")
            continue
        except Exception as e:
            # Capturar cualquier otro error inesperado
            print(f"Error inesperado: {str(e)}")
            continue

def ejercicio4():
    """
    Función principal que ejecuta el simulador de cajero
    """
    try:
        cajero_automatico()
    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario.")
    except Exception as e:
        print(f"Error del sistema: {str(e)}")

# Función adicional para pruebas específicas
def pruebas_cajero():
    """
    Función para realizar pruebas específicas del cajero
    """
    print("=== MODO DE PRUEBAS ===")
    
    casos_prueba = [
        {"saldo": 10000, "retiro": "5000", "esperado": "éxito"},
        {"saldo": 10000, "retiro": "15000", "esperado": "fondos insuficientes"},
        {"saldo": 10000, "retiro": "-500", "esperado": "valor negativo"},
        {"saldo": 10000, "retiro": "abc", "esperado": "número inválido"},
        {"saldo": 10000, "retiro": "0", "esperado": "valor cero"}
    ]
    
    for i, caso in enumerate(casos_prueba, 1):
        print(f"\n--- Prueba {i} ---")
        print(f"Saldo: ${caso['saldo']:,}")
        print(f"Retiro: {caso['retiro']}")
        print(f"Resultado esperado: {caso['esperado']}")
        
        # Simular la lógica de validación
        try:
            monto = float(caso['retiro'])
            if monto < 0:
                print("Resultado: Error - No se permiten valores negativos.")
            elif monto == 0:
                print("Resultado: Error - El monto debe ser mayor que cero.")
            elif monto > caso['saldo']:
                print("Resultado: Error - Fondos insuficientes.")
            else:
                nuevo_saldo = caso['saldo'] - monto
                print(f"Resultado: Retiro exitoso. Saldo restante: ${nuevo_saldo:,}")
        except ValueError:
            print("Resultado: Error - Debe ingresar un número válido.")

# Ejecutar el ejercicio
if __name__ == "__main__":
    print("Seleccione el modo:")
    print("1. Cajero automático normal")
    print("2. Modo de pruebas")
    
    try:
        modo = int(input("Opción (1-2): "))
        if modo == 1:
            ejercicio4()
        elif modo == 2:
            pruebas_cajero()
        else:
            print("Opción inválida. Ejecutando modo normal...")
            ejercicio4()
    except ValueError:
        print("Ejecutando modo normal...")
        ejercicio4()

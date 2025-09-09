# Nombre completo: [daner]
# Ejercicio 2 - Función para calcular impuesto

def calcular_impuesto(valor, impuesto=19):
    """
    Función que calcula el valor final de un producto con impuesto incluido.
    
    Args:
        valor (float): Precio base del producto
        impuesto (float): Porcentaje de impuesto (por defecto 19%)
    
    Returns:
        float: Valor final con impuesto incluido
    """
    # Calcular el valor del impuesto
    valor_impuesto = valor * (impuesto / 100)
    # Retornar el valor total (base + impuesto)
    valor_final = valor + valor_impuesto
    return valor_final

def ejercicio2():
    """
    Programa principal que solicita valores de productos y calcula el total con impuesto.
    """
    print("=== CALCULADORA DE IMPUESTOS ===")
    productos = []
    total_sin_impuesto = 0
    total_con_impuesto = 0
    
    # Solicitar al menos 3 productos
    for i in range(3):
        while True:
            try:
                print(f"\n--- Producto {i+1} ---")
                valor = float(input(f"Ingrese el valor del producto {i+1}: $"))
                if valor >= 0:
                    break
                else:
                    print("El valor debe ser positivo.")
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")
        
        # Preguntar si quiere usar impuesto personalizado
        usar_impuesto_custom = input("¿Desea usar un impuesto diferente al 19%? (s/n): ").lower()
        
        if usar_impuesto_custom == 's':
            while True:
                try:
                    impuesto_custom = float(input("Ingrese el porcentaje de impuesto: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un porcentaje válido.")
            
            valor_final = calcular_impuesto(valor, impuesto_custom)
            productos.append({
                'valor_base': valor, 
                'impuesto': impuesto_custom, 
                'valor_final': valor_final
            })
        else:
            valor_final = calcular_impuesto(valor)  # Usa el 19% por defecto
            productos.append({
                'valor_base': valor, 
                'impuesto': 19, 
                'valor_final': valor_final
            })
        
        # Acumular totales
        total_sin_impuesto += valor
        total_con_impuesto += valor_final
        
        print(f"Valor base: ${valor:,.2f}")
        print(f"Valor con impuesto: ${valor_final:,.2f}")
    
    # Mostrar resumen final
    print("\n=== RESUMEN FINAL ===")
    for i, producto in enumerate(productos, 1):
        print(f"Producto {i}: ${producto['valor_base']:,.2f} + {producto['impuesto']}% = ${producto['valor_final']:,.2f}")
    
    print(f"\nTotal sin impuesto: ${total_sin_impuesto:,.2f}")
    print(f"Total con impuesto: ${total_con_impuesto:,.2f}")
    print(f"Total de impuestos pagados: ${total_con_impuesto - total_sin_impuesto:,.2f}")

# Ejecutar el ejercicio
if __name__ == "__main__":
    ejercicio2()

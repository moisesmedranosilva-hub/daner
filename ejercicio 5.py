# Nombre completo: [danner5]
# Ejercicio 5 - Sistema de gestión de productos (Mini-proyecto)

def total_productos(lista):
    """
    Retorna el número total de productos en la lista.
    
    Args:
        lista (list): Lista de diccionarios con productos
    
    Returns:
        int: Número total de productos
    """
    return len(lista)

def precio_promedio(lista):
    """
    Calcula y retorna el precio promedio de todos los productos.
    
    Args:
        lista (list): Lista de diccionarios con productos
    
    Returns:
        float: Precio promedio de los productos
    """
    if not lista:  # Verificar lista vacía
        return 0
    
    total_precio = sum(producto['precio'] for producto in lista)
    return total_precio / len(lista)

def producto_mas_caro(lista):
    """
    Encuentra y retorna el producto más caro.
    
    Args:
        lista (list): Lista de diccionarios con productos
    
    Returns:
        dict: Diccionario con el nombre y precio del producto más caro
    """
    if not lista:  # Verificar lista vacía
        return None
    
    producto_caro = max(lista, key=lambda x: x['precio'])
    return {"nombre": producto_caro['nombre'], "precio": producto_caro['precio']}

def producto_mas_barato(lista):
    """
    Encuentra y retorna el producto más barato.
    
    Args:
        lista (list): Lista de diccionarios con productos
    
    Returns:
        dict: Diccionario con el nombre y precio del producto más barato
    """
    if not lista:  # Verificar lista vacía
        return None
    
    producto_barato = min(lista, key=lambda x: x['precio'])
    return {"nombre": producto_barato['nombre'], "precio": producto_barato['precio']}

def ordenar_productos_por_precio(lista, descendente=True):
    """
    Función bonus: Ordena los productos por precio.
    
    Args:
        lista (list): Lista de diccionarios con productos
        descendente (bool): True para orden descendente, False para ascendente
    
    Returns:
        list: Lista ordenada de productos
    """
    return sorted(lista, key=lambda x: x['precio'], reverse=descendente)

def ingresar_productos():
    """
    Función para ingresar productos usando un ciclo while.
    
    Returns:
        list: Lista de productos ingresados
    """
    productos = []
    
    print("=== INGRESO DE PRODUCTOS ===")
    print("Ingrese los productos (escriba 'fin' en el nombre para terminar)")
    
    while True:
        # Pedir nombre del producto
        nombre = input("\nNombre del producto: ").strip()
        
        # Verificar si el usuario quiere terminar
        if nombre.lower() == 'fin':
            break
        
        # Validar que el nombre no esté vacío
        if not nombre:
            print("El nombre del producto no puede estar vacío.")
            continue
        
        # Pedir precio del producto con validación
        while True:
            try:
                precio = float(input("Precio del producto: $"))
                if precio >= 0:
                    break
                else:
                    print("El precio debe ser un valor positivo.")
            except ValueError:
                print("Por favor, ingrese un precio válido (número).")
        
        # Agregar producto a la lista
        producto = {"nombre": nombre, "precio": precio}
        productos.append(producto)
        
        print(f"Producto agregado: {nombre} - ${precio:,.2f}")
        print(f"Total de productos ingresados: {len(productos)}")
    
    return productos

def generar_reporte(lista_productos):
    """
    Genera y muestra un reporte completo de los productos.
    
    Args:
        lista_productos (list): Lista de productos a reportar
    """
    if not lista_productos:
        print("No hay productos para generar el reporte.")
        return
    
    print("\n" + "="*50)
    print("           REPORTE FINAL DE PRODUCTOS")
    print("="*50)
    
    # Información básica
    print(f"\n📊 RESUMEN GENERAL:")
    print(f"   • Total de productos: {total_productos(lista_productos)}")
    print(f"   • Precio promedio: ${precio_promedio(lista_productos):,.2f}")
    
    # Producto más caro
    mas_caro = producto_mas_caro(lista_productos)
    print(f"\n💰 PRODUCTO MÁS CARO:")
    print(f"   • Nombre: {mas_caro['nombre']}")
    print(f"   • Precio: ${mas_caro['precio']:,.2f}")
    
    # Producto más barato  
    mas_barato = producto_mas_barato(lista_productos)
    print(f"\n🏷️  PRODUCTO MÁS BARATO:")
    print(f"   • Nombre: {mas_barato['nombre']}")
    print(f"   • Precio: ${mas_barato['precio']:,.2f}")
    
    # Lista completa de productos
    print(f"\n📝 LISTA COMPLETA DE PRODUCTOS:")
    for i, producto in enumerate(lista_productos, 1):
        print(f"   {i:2d}. {producto['nombre']:20} - ${producto['precio']:>8,.2f}")
    
    # Bonus: Productos ordenados por precio
    print(f"\n⭐ BONUS - PRODUCTOS ORDENADOS POR PRECIO (mayor a menor):")
    productos_ordenados = ordenar_productos_por_precio(lista_productos)
    for i, producto in enumerate(productos_ordenados, 1):
        print(f"   {i:2d}. {producto['nombre']:20} - ${producto['precio']:>8,.2f}")
    
    # Estadísticas adicionales
    precios = [p['precio'] for p in lista_productos]
    precio_total = sum(precios)
    
    print(f"\n📈 ESTADÍSTICAS ADICIONALES:")
    print(f"   • Valor total del inventario: ${precio_total:,.2f}")
    print(f"   • Diferencia precio más caro/barato: ${mas_caro['precio'] - mas_barato['precio']:,.2f}")
    
    # Clasificación por rangos de precio
    baratos = [p for p in lista_productos if p['precio'] < precio_promedio(lista_productos)]
    caros = [p for p in lista_productos if p['precio'] >= precio_promedio(lista_productos)]
    
    print(f"   • Productos por debajo del promedio: {len(baratos)}")
    print(f"   • Productos por encima del promedio: {len(caros)}")

def ejercicio5():
    """
    Función principal que ejecuta el sistema de gestión de productos.
    """
    print("🏪 SISTEMA DE GESTIÓN DE PRODUCTOS")
    print("-" * 40)
    
    # 1. Ingresar productos
    productos = ingresar_productos()
    
    # 2. Verificar si se ingresaron productos
    if not productos:
        print("\nNo se ingresaron productos. Terminando programa.")
        return
    
    # 3. Generar reporte final
    generar_reporte(productos)
    
    # 4. Opciones adicionales
    print("\n" + "="*50)
    print("¿Desea ver alguna información específica?")
    print("1. Ver solo estadísticas básicas")
    print("2. Ver productos ordenados por precio ascendente")  
    print("3. Buscar un producto específico")
    print("4. Salir")
    
    while True:
        try:
            opcion = int(input("\nSeleccione una opción (1-4): "))
            if opcion == 1:
                print(f"\n📊 ESTADÍSTICAS BÁSICAS:")
                print(f"Total: {total_productos(productos)} productos")
                print(f"Promedio: ${precio_promedio(productos):,.2f}")
                break
            elif opcion == 2:
                print(f"\n📈 PRODUCTOS ORDENADOS (menor a mayor precio):")
                ordenados_asc = ordenar_productos_por_precio(productos, descendente=False)
                for i, p in enumerate(ordenados_asc, 1):
                    print(f"   {i}. {p['nombre']} - ${p['precio']:,.2f}")
                break
            elif opcion == 3:
                buscar = input("Ingrese el nombre del producto a buscar: ").lower()
                encontrados = [p for p in productos if buscar in p['nombre'].lower()]
                if encontrados:
                    print(f"\n🔍 PRODUCTOS ENCONTRADOS:")
                    for p in encontrados:
                        print(f"   • {p['nombre']} - ${p['precio']:,.2f}")
                else:
                    print("❌ No se encontraron productos con ese nombre.")
                break
            elif opcion == 4:
                break
            else:
                print("Opción inválida. Seleccione 1-4.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    print("\n¡Gracias por usar el sistema de gestión de productos! 👋")

# Función para pruebas con datos de ejemplo
def ejercicio5_prueba():
    """
    Función para probar el sistema con datos de ejemplo.
    """
    print("🧪 MODO PRUEBA CON DATOS DE EJEMPLO")
    
    # Datos de ejemplo
    productos_ejemplo = [
        {"nombre": "Manzana", "precio": 2500},
        {"nombre": "Leche", "precio": 3500},
        {"nombre": "Pan", "precio": 1200},
        {"nombre": "Arroz", "precio": 4000},
        {"nombre": "Aceite", "precio": 8500}
    ]
    
    print(f"\nUsando {len(productos_ejemplo)} productos de ejemplo...")
    generar_reporte(productos_ejemplo)

# Ejecutar el ejercicio
if __name__ == "__main__":
    print("Seleccione el modo:")
    print("1. Modo interactivo (ingresar productos)")
    print("2. Modo prueba (usar datos de ejemplo)")
    
    try:
        modo = int(input("Opción (1-2): "))
        if modo == 1:
            ejercicio5()
        elif modo == 2:
            ejercicio5_prueba()
        else:
            print("Opción inválida. Ejecutando modo interactivo...")
            ejercicio5()
    except ValueError:
        print("Ejecutando modo interactivo...")
        ejercicio5()

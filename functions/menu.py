
def menu():

    menu = """
    ==== SISTEMA GESTION DE PEDIDOS ====
    
    1. Registrar clientes
    2. Registrar productos
    3. Crear pedidos
    4. Consultar pedidos
    5. Consultar ingresos de la jornada
    6. Generar reporte final
    7. Salir
    """
    print(menu)

    option = input("¿Que deseas realizar hoy?: ")
    return option

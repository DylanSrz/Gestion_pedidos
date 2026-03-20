
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


def msg_register_product(product_info):
    print("\n=== Registro de productos ===\n")    
    print(f"\nSe realizo el siguiente registro: \n")
    print(f" - id: {product_info[0]}")
    print(f" - nombre: {product_info[1]}")
    print(f" - precio: {product_info[2]}\n")

def msg_daily_income(daily_profit):
    print(f"\n El total de ingresos durante la jornada fue {daily_profit}\n")

def msg_order_created(total_order):
    print(f"\nPedido creado con éxito, el valor total del pedido es: {total_order}\n")
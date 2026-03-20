

from functions.screen_controller import deleteScreen


def final_report(pedidos_creados, daily_profit):
    total_orders = 0
    total_income = 0

    deleteScreen()

    print("\n ==== REPORTE FINAL DE LA JORNADA ====\n")
    for user_id, orders in pedidos_creados.items():
        for order_id in pedidos_creados[user_id]:
            total_orders += 1

    print(f" - Total de pedidos registrados: {total_orders}")

    print(f" - Total de ingresos generados: {daily_profit}")

    print(" - Pedidos agrupados por cliente:")
    for user_id, orders in pedidos_creados.items():
        print(f"\n   • Cliente ID: {user_id}")
        for order_id, order_info in orders.items():
            print(
                f"        Pedido ID: {order_id}, Producto: {order_info['product']}, Cantidad: {order_info['amount']}, Precio Total: {order_info['total_price']}")

    print("\n - Productos vendidos durante el día:")
    productos_vendidos = {}
    for user_id, orders in pedidos_creados.items():
        for order_id, order_info in orders.items():
            product_name = order_info['product']
            amount = order_info['amount']
            if product_name in productos_vendidos:
                productos_vendidos[product_name] += amount
            else:
                productos_vendidos[product_name] = amount

    for product, total_amount in productos_vendidos.items():
        print(f"   • Producto: {product}, Cantidad vendida: {total_amount}")

    print("\n ==== FIN DEL REPORTE ====\n")

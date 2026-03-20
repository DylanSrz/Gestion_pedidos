def check_orders(pedidos_creados):
    if not pedidos_creados:
        print("No se han realizado pedidos")
        return

    print("Historial de pedidos")
    print("─" * 50)
    print(f"{'client id':<7} | {'producto.':<7} | {'Cantidad.':<7} | {'Total':<10}")

    for user_id, orders in pedidos_creados.items():
        for order_id, order_info in orders.items():
            print(
                f"{user_id:<9} | {order_info['product']:<9} | {order_info['amount']:<9} | {order_info['total_price']:<10}")

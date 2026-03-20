from functions.screen_controller import deleteScreen


def check_orders(pedidos_creados):

    if not pedidos_creados:
        deleteScreen()
        print("\n     === Historial de pedidos ===")
        print("\nNo se han realizado pedidos.")
        print("\n ==== Fin del historial de pedidos ====\n")
        return

    deleteScreen()

    print("    ====  Historial de pedidos  ===   \n")
    print(f"{'client id':<7} | {'producto.':<7} | {'Cantidad.':<7} | {'Total':<10}")

    for user_id, orders in pedidos_creados.items():
        for order_id, order_info in orders.items():
            print(
                f"{user_id:<9} | {order_info['product']:<9} | {order_info['amount']:<9} | {order_info['total_price']:<10}")

    print("\n ==== Fin del historial de pedidos ====\n")
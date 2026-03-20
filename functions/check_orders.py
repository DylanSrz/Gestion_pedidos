def check_orders(pedidos):
    if not pedidos:
        print("No se han realizado pedidos")
        return

    print("Historial de pedidos")
    print("─" * 50)
    print(f"{'cliente':<16} | {'producto.':<7} | {'Cantidad.':<7} | {'Total':<10}")

    for p in pedidos:
        Total = sum(p["total"] for p in pedidos)
        print(f"{p['cliente']:<16} | {p['producto']:<7} | {p['cantidad']:<7} |{p['Total']:<10}")
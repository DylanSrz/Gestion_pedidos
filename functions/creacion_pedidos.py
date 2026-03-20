from data_dictionary import *


def order_creator(producto):

    first_counter = 0
    second_counter = 0
    third_counter = 0

    while first_counter != 1:

        user_id = input("\nIngrese su ID: ")

        if not user_id in clients:
            print("ID no existe, try again")
            continue

        else:
            first_counter = 1

    while second_counter != 1:

        print("\nProductos disponibles: \n")

        for key in producto:
            print(
                f" - Producto: {producto[key][1].capitalize()}, Precio: {producto[key][2]}")

        product = input("\nIngrese el nombre del producto: ").strip().lower()

        if not product in producto:
            print("\nProducto no existe, try again")
            continue
        else:
            second_counter = 1

    while third_counter != 1:

        amount = int(input("ingrese la cantidad del producto: "))

        if amount <= 0:
            print("Cantidad no válida, try again")
            continue
        else:
            print("\nPedido creado con éxito")
            third_counter = 1

        price = producto[product][2]
        total_order = price * amount

        if user_id not in pedidos_creados:
            pedidos_creados[user_id] = {}

        order_id = len(pedidos_creados[user_id]) + 1

        pedidos_creados[user_id][order_id] = {
            "product": product,
            "amount": amount,
            "total_price": total_order
        }

        print(f"El valor total del pedido es: {total_order}")

    return pedidos_creados

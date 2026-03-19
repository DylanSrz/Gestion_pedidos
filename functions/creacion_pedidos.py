from register_clients import *

pedidoscreados = {}

def order_creator():

    first_counter = 0
    second_counter = 0
    third_counter = 0

    while first_counter != 1:

        client = input("ingrese su nombre: ")

        if not client.replace(" ","").isalpha():
            continue

        else:
            first_counter = 1
    
    while second_counter != 1:

        product = input("ingrese el producto: ")

        if not product.replace(" ","").isalpha():
            print("No se aceptan valores numericos")
            continue

        else:
            second_counter = 1

    while third_counter != 1:

        amount = int(input("ingrese la cantidad del producto: "))

        if not amount.isdigit():
            print("No se aceptan valores alfabeticos")
            continue
        else:
            third_counter = 1

    pedidoscreados[client]={
        "product": product,
        "amount": amount,
    }

    total_order = product * amount

    print(f"El valor total del pedido es: {total_order}")

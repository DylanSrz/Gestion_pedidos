from data_dictionary import *


def order_creator():

    first_counter = 0
    second_counter = 0
    third_counter = 0

    while first_counter != 1:

        id = input("Ingrese su ID: ")
        
        if not id.replace(" ","").isalpha():
            continue
        
        if not id in clients:
            print("ID no existe")
            print("Try again")
            print("")
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

    pedidos_creados[client]={
        "product": product,
        "amount": amount,
    }

    total_order = product * amount

    print(f"El valor total del pedido es: {total_order}")

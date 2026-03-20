from data import producto
from functions.screen_controller import deleteScreen, pauseScreen


def register_producto():

    deleteScreen()

    print("\n=== Registro de productos ===\n")

    while True:
        try:
            product_id = (input("\nIngrese el id del producto: "))
            break
        except:
            print("\nError: debe ser un número.")

    while True:
        product_name = input(
            "Ingrese el nombre del producto: ").strip().lower()
        if product_name.replace(" ", "").isalpha():
            break
        else:
            print("Error: solo se permiten letras.\n")
            
    while True:
        try:
            unit_price = float(input("Ingrese el precio del producto: "))
            break
        except:
            print("Error: debe ser un número.\n")


    producto[product_name] = (product_id, product_name, unit_price)

    deleteScreen()
    print("\n=== Registro de productos ===\n")

    print(
        f"\nSe realizo el siguiente registro:")
    print(f" - id: {product_id}")
    print(f" - nombre: {product_name}")
    print(f" - precio: {unit_price}\n")

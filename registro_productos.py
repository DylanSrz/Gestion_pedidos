def Registrar_producto(product_id, product_name, unit_price):
    product = (product_id, product_name, unit_price)
    return product 


def pedir_producto():

    while True:
        try:
            product_id = int(input("Ingrese el id del producto: "))
            break
        except:
            print("Error: debe ser un número.")


    while True:
        product_name = input("Ingrese el nombre del producto: ")
        if product_name.replace(" ", "").isalpha():
            break
        else:
            print("Error: solo se permiten letras.")


    while True:
        try:
            unit_price = float(input("Ingrese el precio del producto: "))
            break
        except:
            print("Error: debe ser un número.")

    return Registrar_producto(product_id, product_name, unit_price)
products = {}
cantidad = int(input("cuantos productos desea registrar?: "))
for i in range(cantidad):
    print(f"\n producto{i+1}")
    product = pedir_producto()
    products[product[0]] = product

print("\nProductos registrados:")
for prod in products.values():
    print(prod)

from data_dictionary import producto


def pedir_producto():

    while True:
        try:
            product_id = int(input("\nIngrese el id del producto: "))
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
    
    producto[product_id] = (product_name, unit_price)
    
    print(f"\nSe realizo el siguiente registro: id: {product_id}, nombre: {product_name}, precio: {unit_price}")

    

from data import clients
from functions.screen_controller import deleteScreen, pauseScreen


def register_clients():

    while True:

        deleteScreen()
        print("\n=== Registro de clientes ===\n")        
        id = input("Enter your ID: ")

        if id in clients:
            print("\nThis ID already exists")
            print("Try again\n")
            pauseScreen()
            continue
        break

    name = input("Enter your name: ")
    email = input("Enter your email: ")

    clients[id] = {
        "name": name,
        "email": email
    }

    print("\nClient registered successfully\n")

    return clients



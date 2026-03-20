from data_dictionary import clients


def register_clients():
    while True:
        id = input("Enter your ID: \n")

        if id in clients:
            print("This ID already exists")
            print("Try again")
            print("")
            continue
        break

    name = input("Enter your name: \n")
    email = input("Enter your email: \n")

    clients[id] = {
        "name": name,
        "email": email
    }

    print("Client registered successfully")

    return clients


if __name__ == "__main__":
    register_clients()

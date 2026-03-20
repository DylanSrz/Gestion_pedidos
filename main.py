from functions.menu import menu
from functions.screen_controller import *
from functions.register_clients import register_clients
from functions.registro_productos import pedir_producto
from data_dictionary import producto
from functions.creacion_pedidos import order_creator


while True:
    deleteScreen()
    menu()
    
    option = input("¿Que deseas realizar hoy?: ")
    
    if option == "1":
        register_clients()
        pauseScreen()
    elif option == "2":
        pedir_producto()
        pauseScreen()
    elif option == "3":
        order_creator()
        pauseScreen()
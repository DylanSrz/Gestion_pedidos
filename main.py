from functions.menu import menu
from functions.screen_controller import *
from functions.register_clients import register_clients
from functions.registro_productos import register_producto
from data import producto, pedidos_creados, clients, daily_profit
from functions.creacion_pedidos import order_creator
from functions.check_orders import check_orders
from functions.daily_income import daily_income
from functions.final_report import final_report


while True:

    deleteScreen()
    
    option = menu()

    if option == "1":
        register_clients()
        pauseScreen()
    elif option == "2":
        register_producto()
        pauseScreen()
    elif option == "3":
        order_creator(producto)
        print(pedidos_creados)
        pauseScreen()
    elif option == "4":
        check_orders(pedidos_creados)
        pauseScreen()
    elif option == "5":
        daily_profit = daily_income(pedidos_creados)
        print(f"\n El total de ingresos durante la jornada fue {daily_profit}")
        pauseScreen()
    elif option == "6":
        final_report(pedidos_creados, daily_profit)
        pauseScreen()
    elif option == "7":
        break

print("Gracias por usar el sistema de gestión de pedidos. ¡Hasta luego!")

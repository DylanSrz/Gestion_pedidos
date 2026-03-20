from functions.msg import menu, msg_daily_income, msg_register_product, msg_order_created
from functions.screen_controller import *
from functions.register_clients import register_clients
from functions.registro_productos import register_producto
from data import producto, pedidos_creados, clients, daily_profit
from functions.order_creator import order_creator
from functions.check_orders import check_orders
from functions.daily_income import daily_income
from functions.final_report import final_report

counter = 0

while counter != 1:

    deleteScreen()
    
    option = menu()

    if option == "1":
        register_clients()
        pauseScreen()
    elif option == "2":
        result_rp = register_producto()
        msg_register_product(result_rp)
        pauseScreen()
    elif option == "3":
        result_oc = order_creator(producto)
        msg_order_created(result_oc[1])
        pauseScreen()
    elif option == "4":
        check_orders(pedidos_creados)
        pauseScreen()
    elif option == "5":
        daily_profit = daily_income(pedidos_creados)
        msg_daily_income(daily_profit)
        pauseScreen()
    elif option == "6":
        final_report(pedidos_creados, daily_profit)
        pauseScreen()
    elif option == "7":
        counter = 1

print("\nGracias por usar el sistema de gestión de pedidos. ¡Hasta luego!\n")

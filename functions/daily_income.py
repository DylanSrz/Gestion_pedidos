from data_dictionary import *


def daily_income(pedidos_creados):
    global daily_income
    daily_income = 0

    for user_id, orders in pedidos_creados.items():
        for order_id, order_info in orders.items():
            daily_income += order_info['total_price']

    print(f"\n El total de ingresos durante la jornada fue {daily_income}")
    return daily_income

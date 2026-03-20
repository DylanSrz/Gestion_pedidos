from data import *


def daily_income(pedidos_creados):
    
    daily_profit = 0

    for user_id, orders in pedidos_creados.items():
        for order_id, order_info in orders.items():
            daily_profit += order_info['total_price']
    
    return daily_profit 



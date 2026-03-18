from data_dictionary import *

daily_income = 0
def daily_income(pedidos):
    
    for item in pedidos:
        daily_income += item
    
    print(f"\n El total de ingresos durante la jornada fue {daily_income}")
    
        
        
    
daily_profit = 0

clients = {
    "123": {
        "name": "pepe",
        "email": "example@example.com"
    }
}

producto = {
    "manzana": ("001", "manzana", 1000),
    "pera": ("002", "pera", 2000),
    "naranja": ("003", "naranja", 3000)
}

pedidos_creados = {
    "123": {
        "1": {
            "product": "manzana",
            "amount": 2,
            "total_price": 2000
        },
        "2": {
            "product": "pera",
            "amount": 1,
            "total_price": 2000
        },
        "3": {
            "product": "naranja",
            "amount": 3,
            "total_price": 9000
        }
    },
    "456": {
        "1": {
            "product": "manzana",
            "amount": 10,
            "total_price": 10000
        },
        "2": {
            "product": "pera",
            "amount": 10,
            "total_price": 20000
        }
    }
}

orders_list = [{
    "client_name": "John Doe",
    "product_name": "keyboard",
    "quantity": 10,
    "price": 19.99,
    "status": "new"
},
]

def add_order():
    order = {}
    print()
    order["client_name"] = input("Введите ваше имя: ")
    order["product_name"] = input("Какой товар заказываете: ")
    order["quantity"] = int(input("Введите количество: "))
    order["price"] = float(input("Введите цену: "))
    order["status"] = "new"
    orders_list.append(order)


def show_orders():
    print(orders_list)

def find_order():
    print()

def delete_order():
    print()

def exit_program():
    print("Exiting the program...")
    exit()


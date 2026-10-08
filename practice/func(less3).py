def sayHello():
    print('Привет')

sayHello()

def greet(name):
    print(f"Привет, {name}")

greet('Алексей')

def calculate_total(price,quantity):
    total = price * quantity
    return total


print(calculate_total(5500,5))

# расчет скидки
def calculate_discount(price):
    if price > 7000:
       return price * 0.8

    return price

print(calculate_discount(8000))

# Практика:
# Задача 1
def create_order_message(name,product,price):
    return f"Клиент {name} заказал {product} на сумму {price} рублей"

# print(create_order_message('Алексей','кроссовки','20000'))


price = input('Скажите желаемую цену: ')

# вариант 1
# if (type(int(price)) == int):
#     print(create_order_message('Алексей','кроссовки',price))
# else:
#     print('конец условия')

# вариант 2

# try:
#     price = int(price)
#     print(create_order_message('Алексей','кроссовки',price))
# except ValueError:
#     print("Введите число")

try:
    price = int(price)
except ValueError:
    print('ошибка:введите число')
else:
   print(create_order_message('Алексей','кроссовки',price)) 

# Задача 2

# длинееpre
def is_free_delivery(amount):
    if amount > 3000:
        return True
    else:
        return False
    
# короче
def is_free_delivery2(amount):
    return amount > 3000

delivery = is_free_delivery(4000)
print('delivery',delivery)

delivery2 = is_free_delivery2(2000)
print('delivery2',delivery2)

# Задача 3
# тут ошибка будет,если 5000 вбить в функцию ниже
def calculate_manager_bonus(amount):
    if amount < 5000:
        return amount / 100 * 5
    else:
        return amount/ 100 * 10
    
# поправленный вариант
def calculate_manager_bonus2(amount):
    if amount < 5000:
        return amount * 0.05
    else:
        return amount * 0.10
    
print(calculate_manager_bonus(10000))                  
print(calculate_manager_bonus2(5000))                  


# Мини-челлендж на подумать
#я бы разбил такой функционал бота на 4 функции

def take_menu():
    print()

def make_order():
    print()

def checkPay():
    print()
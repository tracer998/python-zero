# практика
# задача 1
clients = [
    "Алексей",
    "Мария",
    "Иван"
]

print(clients)
# добавить 
clients.append("Ольга")
print(clients)
# длина
print(len(clients))
# перебрать
for client in clients:
    print(client)

# задача 2
orders = [1200, 3400, 800, 15000]

for order in orders:
    print('задача 2',order)

# задача 3(переименовал переменную чтобы не было ошибок)
orders2 = [1200, 3400, 800, 15000]

total = 0

for order in orders2:
    total = total + order
    print('total',total)
    
# Бизнес-задача
products = [
    "Ноутбук",
    "Мышка",
    "Клавиатура",
    "Монитор"
]

# вывод товаров в консоль
for product in products:
    print(product)

quantity = len(products)
print(quantity)

products.append('Наушники')
print(products)

'''Почему список плохо подходит 
для хранения одного клиента, но идеально подходит для хранения всех клиентов бота?'''
'''Ответ:думаю что подходят и для хранения одного клиента.Вопрос с подвохом'''
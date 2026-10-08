# temperature = 10

# if temperature > 0:
#     print('The weather is hot')
# else: 
#     print('The wether is cold')


# coffe = True
# message = input('Введите что нибудь:')
# print(type(message))

# if coffe:
#     print('i have my coffe:D')
# else:
#     print('i have no one coffe:(')

# money = 1000

# if money >= 1000:
#     print('i can bye ticket,because i have ' + 'money')
# else:
#     print('i can not bye nothing:(')

# time = True

# if time > 0:
#     print('lol')

# x = 1000

# if x > 2000:
#     print('more')
# else:
#     print('easy')

# age = 50
# if age < 18:
#     print("Несовершеннолетний")
# elif age < 65:
#     print("Взрослый")
# else:
#     print("Пенсионный возраст") 


# def check_user():
#     login = "linuxman"
#     password = 'admin123'
#     print_user_log = input('Введите логин: ')
#     print_user_pass = input('Введите пароль: ')
#     print(type(print_user_log), print_user_log, print_user_pass)
#     print(f"{print_user_log = }")

#     if login == print_user_log and password == print_user_pass:
#         print("Доступ разрешен")
#     else:
#         print("Неверный логин или пароль")

# check_user()

# name = "Alexey"
# age = 30

# print(f"{name} is {age} years old")
# print(name + " is " + str(age) + " years old")

# 1 вариант
# def calculate_discount():
#     visits = int(input('Количество посещений клиентом магазина: ')) # не пойму как умнее взять и считать данные
#     spent = int(input('Сумма заказов: ')) 
#     order = int(input('Цена текущего заказа: '))

#     if order >= 100:
#         if visits == 1:
#             print(f'Новый клиент и заказ от 100 евро,его скидка 15%.Итог к оплате:{order - (order / 100 * 15)}€')
#         elif visits >= 10 and spent >= 1000:
#             print(f'Новый клиент и заказ от 100 евро,его скидка 25%.Итог к оплате:{order - (order / 100 * 25)}€')
#         else:
#             print(f'Обычный клиент и заказ от 100 евро,его скидка 10%.Итог к оплате:{order - (order / 100 * 10)}€')
#     else:
#         if visits == 1:
#             print(f'Новый клиент,его скидка 10%.Итог к оплате:{order - (order / 100 * 10)}€')
#         elif visits >= 10 and spent >= 1000:
#             print(f'Новый клиент,его скидка 20%.Итог к оплате:{order - (order / 100 * 20)}€')
#         else:
#             print(f'Обычный клиент,его скидка 5%.Итог к оплате:{order - (order / 100 * 5)}€')


# calculate_discount()

# 2 вариант
# def calculate_discount():
#     visits = int(input('Количество посещений клиентом магазина: ')) 
#     spent = int(input('Сумма заказов: ')) 
#     order = int(input('Цена текущего заказа: '))
#     discount = 0

#     if visits == 1:
#         discount = 10
#         if order >= 100:
#             discount = discount + 5
#         print(f'Новый клиент,его скидка {discount}%.Итог к оплате:{order - (order / 100 * discount)}€')
#     elif visits >= 10 and spent >= 1000:
#         discount = 20
#         if order >= 100:
#             discount = discount + 5
#         print(f'VIP клиент,его скидка {discount}%.Итог к оплате:{order - (order / 100 * discount)}€')
#     else:
#         discount = 5
#         if order >= 100:
#             discount = discount + 5
#         print(f'Обычный клиент,его скидка {discount}%.Итог к оплате:{order - (order / 100 * discount)}€')

# calculate_discount()

# без бюджета высокая срочность не в счет:)
# def lead_scorer():
#     name = ('Ваше имя: ')
#     order = ('Какая услуга нужна: ')
#     budget = int(input('Ваш бюджет: '))
#     urgency = input('Срочность: ')

#     if budget >= 1000 and urgency == 'высокая':
#         status = 'HOT'
#     elif budget >= 500 and budget < 1000:
#         status = 'WARM'
#     else:
#         status = 'COLD'
    
#     print(status)
        
# lead_scorer()

cliens = ['Ivan','Petr']






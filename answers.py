# программа учета клиентов
def clients_all(client_count):
    hot_count = 0
    warm_count = 0
    cold_count = 0
    client_name_list = []

    for i in range(client_count):
        print(f"\n--- Заявка №{i + 1} ---")

        name = input("Имя клиента: ")
        budget = int(input("Бюджет: "))
        urgency = input("Срочность: ").strip().lower()

        client_name_list.append(name)

        if budget >= 1000 and urgency == "высокая":
            status = "HOT"
            hot_count += 1
        elif budget >= 500 or urgency == "средняя":
            status = "WARM"
            warm_count += 1
        else:
            status = "COLD"
            cold_count += 1

        print(f"Клиент: {name} | Статус: {status}")

    print("\n--- Итоговая статистика ---")
    print(f"HOT заявок: {hot_count}")
    print(f"WARM заявок: {warm_count}")
    print(f"COLD заявок: {cold_count}")

    return client_name_list


client_count = int(input("Количество клиентов: "))
names = clients_all(client_count)

print("\n--- Список клиентов ---")
for client in names:
    print(client)


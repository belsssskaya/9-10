import threading
import time

# Функция, выполняемая в потоке командира
def commander():
    print("Командир: Обнаружена цель!")
    time.sleep(2)  # Симуляция некоторой задержки до выдачи команды
    # Дать команду пушкам
    print("Командир: Нанести удар!")

# Функция, выполняемая в потоках пушек
def cannon(cannon_id):
    print(f"Пушка {cannon_id}: Готов к действию")
    time.sleep(1)  # Симуляция некоторой задержки до получения команды
    # Принять команды
    print(f"Пушка {cannon_id}: Получена команда от командира")
    # Выполнять действия пушки...

# Создание и запуск потоков
commander_thread = threading.Thread(target=commander)
commander_thread.start()

cannon_threads = []
num_cannons = 7
for i in range(num_cannons):
    cannon_thread = threading.Thread(target=cannon, args=(i+1,))
    cannon_threads.append(cannon_thread)
    cannon_thread.start()

# Ожидание завершения потоков
commander_thread.join()
for thread in cannon_threads:
    thread.join()

def find_password(n):
    # Переменная для хранения пароля
    result = ""

    # Внешний цикл по первому числу
    for i in range(1, n):
        # Внутренний цикл по второму числу, начиная с i+1, чтобы избежать дублирования
        for j in range(i + 1, n):
            # Проверка кратности
            if n % (i + j) == 0:  
                # Добавляем пару в строку результата
                result += str(i) + str(j)

    return result


for num in range(3, 21):
    password = find_password(num)
    print(f" Number {num} - password {password}")

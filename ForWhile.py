def task3():
    num = 0
    summ = 0
    while True:
        digit = input("Введите число (для завершения введите 0): ")
        if digit == '0':
            break
        digit = int(digit)
        summ += digit
        num += 1
    if num != 0:
        avg = summ / num
        print(f"Среднее значение: {avg}")
    else:
        print("Вы не ввели ни одного числа.")
#task3()


def task4():
    for i in range(101):
        print(i)
#task4()

def task5():
    for i in range(10):
        for j in range(10):
            result = i * j
            print(f"{i} * {j} = {result}")
#task5()

def task6():
    my_list = ["a", 15, "comp", "1,2,3"]
    my_dict = {"b": 22, "78": 15, "lenght": "short"}
    for i in my_list:
        print(i)
    for j in my_dict:
        print(j, my_dict[j])

#task6()


def task7():
    for i in range(1, 101):
        if i % 3 == 0:
            print(i)
#task7()

def task8():
    summ=0
    for i in range(1, 101):
        summ += i
    print(f"Сумма всех чисел от 1 до 100 = {summ}")
#task8()

def task9():
    for i in range(1,10):
            result = i * 2
            print(f"{i} * 2 = {result}")
#task9()


def task10():
    print("Простые числа от 2 до 50:")
    for num in range(2, 51):
        simple = True
        for i in range(2, num):
            if num % i == 0:
                simple = False
                break
        if simple:
            print(num)

#task10()

def task11():
    summ = 0
    for i in range(1,11):
        summ += i ** 2
    print(f"Сумма квадратов чисел от 1 до 10 = {summ}")

#task11()


def task12():
    y = 0
    for x in range(1, 21, 1):
        x = x / 2
        y = x ** 2
        print(f"y= {y}")

#task12()

def task13():
    factorial = 1
    for i in range(1, 6):
        factorial = factorial*i
        print(f"Факториал числа {i} = {factorial}")

#task13()
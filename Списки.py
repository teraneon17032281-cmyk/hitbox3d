ten = []
for i in range(1, 11):
    ten.append(i)

evens = []
for number in ten:
    if number % 2 == 0:
        evens.append(number)

squares = []
for number in evens:
    squares.append(number ** 2)

print(squares)  # [4, 16, 36, 64, 100]


def show_item(my_list=ten):
    while True:
        answer = input('Введите индекс (или exit для выхода): ')

        if answer == 'exit':
            print('Выход')
            break

        try:
            index = int(answer)
            print(my_list[index])
        except ValueError:
            print('Нужно ввести целое число')
        except IndexError:
            print('Такого индекса нет. Доступные индексы: от 0 до', len(my_list) - 1)


show_item()
contacts = [
    {'name': 'Geektech', 'phone': '0507052018'},
    {'name': 'Служба спасения', 'phone': '911'},
    {'name': 'Пожарная служба', 'phone': '101'},
]

def show_contacts():
    #все контакты с номерами
    for i in range(len(contacts)):
        print(i + 1, contacts[i]['name'], contacts[i]['phone'])

def create():
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    contacts.append({'name': name, 'phone': phone})
    print('Контакт добавлен')

def edit():
    name = input('Введите имя контакта, который хотите изменить: ')
    for contact in contacts:
        if contact['name'] == name:
            contact['name'] = input('Новое имя: ')
            contact['phone'] = input('Новый телефон: ')
            print('Контакт изменён')
            return
    print('Такого контакта нет')

def delete():
    name = input('Введите имя контакта, который хотите удалить: ')
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print('Контакт удалён')
            return
    print('Такого контакта нет')

while True:
    print()
    print('1 - Показать контакты')
    print('2 - Добавить контакт')
    print('3 - Изменить контакт')
    print('4 - Удалить контакт')
    print('0 - Выход')

    choice = input('Выберите действие: ')

    if choice == '1':
        show_contacts()
    elif choice == '2':
        create()
    elif choice == '3':
        edit()
    elif choice == '4':
        delete()
    elif choice == '0':
        print('Выход')
        break
    else:
        print('Неверный выбор, введите цифру из меню')
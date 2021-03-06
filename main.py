from handler import handler


def main():
    print('Вас приветствует Бот-помощник')
    print('Комманды доступные Вам: hello, add, change, phone, show all, exit, good bye, close')
    print('Правильная запись: функция, параметри(телефон, дата рождения в стиле 31.12.2000)')
    print('Команда пишеться через пробел')
    print('Параметры add: Имя телефон*, дата рождения*')
    print('Параметры change: Доп. параметр(change, delete, add),'
          ' Имя старий телефон, новый телефон, новая дата рождения*')
    print('* - не обязательно к заполнению')
    print('Параметр phone: Имя')
    print('Параметр days before birthday: Имя')

    while True:
        command = input('Введите название комманды и параметры: ')
        if handler(command) is False:
            print('До новых встреч!')
            break
        print(handler(command))


if __name__ == '__main__':
    main()



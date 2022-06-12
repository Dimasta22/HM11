from parser import parser
from input_error import input_error
from add_class import Record, Name, Phone, Birthday


@input_error
def handler(sentence: str, phone_dict={}, birthday_dict={}):
    def all_function(sentence: str):

        if parser(sentence) == 'HELLO':
            return "How can I help you?"

        if parser(sentence) == 'SHOW ALL':
            return '\n'.join(f'{key}: {value}' for key, value in phone_dict.items())

        if parser(sentence) == 'SHOW DAYS':
            return '\n'.join(f'{key}: {value}' for key, value in birthday_dict.items())

        if parser(sentence) in ['EXIT', 'CLOSE', 'GOOD BYE']:
            return False

        if parser(sentence) is None:
            return 'Введите команду из списка доступных команд!'

        if parser(sentence) == 'DAYS':
            _, name, *args = sentence.split(' ')
            if birthday_dict.get(name, None) is not None:
                record = Record(Name(name), Phone(phone_dict[name][0]), Birthday(birthday_dict[name]))
                return record.days_to_birthday()
            else:
                return 'ДР не задан'

        if parser(sentence) == 'ADD':
            _, name, *args = sentence.split(' ')
            if len(args) == 1:
                number = args[0]
                record = Record(Name(name), Phone(number))
            if len(args) >= 2:
                number, date = args[0], args[1]
                record = Record(Name(name), Phone(number), Birthday(date))
            else:
                record = Record(Name(name))
            record.add_rec()
            phone_dict.update({record.name: record.phones})
            birthday_dict.update({record.name: record.birthday})

        if parser(sentence) == 'PHONE':
            _, name, *args = sentence.split(' ')
            return phone_dict.get(name, 'Такого пользователья нет')

        if parser(sentence)[0] == 'CHANGE':

            if parser(sentence)[1] == 'CHANGE':
                _, _, name, old_number, new_number, *args = sentence.split(' ')
                if phone_dict.get(name, None) is not None or old_number in phone_dict.get(name, None):
                    #print(old_number, phone_dict.get(name, None)[0])
                    record = Record(Name(name), Phone(old_number))
                    record.change_rec(Phone(old_number), Phone(new_number))
                    phone_dict[name] = record.phones
                else:
                    return 'Такого пользователя нет или старый номер не совпадает с введенным номером'

            if parser(sentence)[1] == 'ADD':
                _, _, name, new_number, *args = sentence.split(' ')
                if phone_dict.get(name, None) is not None:
                    record = Record(Name(name))
                    record.add_rec(Phone(new_number))
                    phone_dict[name] = phone_dict.get(name, None) + record.phones
                else:
                    return 'Такого пользователя нет'

            if parser(sentence)[1] == 'DELETE':
                _, _, name, old_number, *args = sentence.split(' ')
                print(name, old_number)
                if phone_dict.get(name, None) is not None:
                    record = Record(Name(name), Phone(phone_dict.get(name)))
                    record.del_rec(Phone(old_number))
                    phone_dict[name] = record.phones
                else:
                    return 'Тут'

            if parser(sentence) is None:
                return 'Введите команду из списка доступных команд!'

            #_, name, new_number, *args = sentence.split(' ')
            #phone_dict[name] = new_number
            # Тут будет изменен подход: другой ввод: change (del_num, add_num, change_num), имя и номер
            # Имя и номер идут в рекорд, а пока, код работает в add_class



        return 'Операция прошла успешно'
    return all_function(sentence)


if __name__ == '__main__':
    sentence = 'add Vlad 067 Vlad 050 vfd    ljh'
    print(handler(sentence))
    sentence = 'add Dima 067 22.01.2000'
    print(handler(sentence))
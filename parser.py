import re


ACTION_LIST = [
    'HELLO',
    'ADD',
    'CHANGE',
    'PHONE',
    'SHOW ALL',
    'DAYS BEFORE BIRTHDAY'
    'GOOD BYE',
    'CLOSE',
    'EXIT'
]

ACTION_LIST_FOR_CHANGE_COMMAND = [
    'CHANGE NUMBER',
    'ADD NUMBER',
    'DELETE NUMBER'
]


def parser(sentence: str):
    sentence = sentence.upper().strip()
    for key in ACTION_LIST:
        func = re.search(fr'^{key}\b', sentence)
        if func is not None:
            if func.group() == 'CHANGE':
                code_word = func.group()
                sentence = sentence[func.span()[1]:].strip()
                for key_2 in ACTION_LIST_FOR_CHANGE_COMMAND:
                    func = re.search(fr'^{key_2}\b', sentence)
                    if func is not None:
                        return code_word, func.group()
            return func.group()


if __name__ == '__main__':
    sentence = 'change change number'
    print(parser(sentence)[0])


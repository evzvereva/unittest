documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def delete_a_document():
    """
    move_document() – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки
    на целевую. """
    number_documents = input('Напишите номер документа, который нужно удалить: ')
    # number_shelf = input('Напишите номер полки, на которую нужно перенести документ: ')
    for key_number_shelf, value in directories.items():
        if number_documents in value:
            print('Документ найден')
            for key_number_shelf, value in directories.items():
                if number_documents in value:
                    value.remove(number_documents)
                    return f'Номер документа {number_documents} удален из полки № {key_number_shelf}.'
    return f'Номер документа не найден.'


def add_a_document_to_the_shelf():
    number_documents = input('Напишите номер документа, который нужно перенести на целевую полку: ')
    number_shelf = input('Напишите номер полки, на которую нужно перенести документ: ')
    for key_number_shelf, value in directories.items():
        if number_shelf in key_number_shelf:  # проверяем есть ли такая полка
            print('Полка найдена.')
            directories[number_shelf] = value + [number_documents]
            return f'Номер документа {number_documents} добавлен на полку № {number_shelf}.'
    return f'Номер документа не найден или неверно указан номер полки.'

# print(directories)
# print(delete_a_document())
# print(add_a_document_to_the_shelf())
# print(directories)

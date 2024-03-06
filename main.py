import json

from impl import Repository


def read_file(in_filename):
    with open(in_filename, encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def write_file(out_filename, data):
    with open(out_filename, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile)


def list_notes(notes):
    for note in notes:
        print(note)


def add_note(notes):
    note_name = input('Введите название заметки: ')
    note_text = input('Введите текст заметки: ')
    notes[note_name] = note_text


def read_note(notes, note_name):
    return notes[note_name]


def delete_note(notes, note_name):
    del notes[note_name]


if __name__ == '__main__':
    filename = 'notebook.json'
    # dct = {'Заметка1': 'Сегодня хорошая погода', 'Заметка2': 'Всем пора спать', 'Заметка3': 'Бросай курить, вставай '
    #                                                                                         'на лыжи'}
    # write_file(filename, dct)
    repo = Repository(filename)

    data1 = repo.read_file()

    list_notes(data1)
    add_note(data1)
    repo
    data1 = read_file(filename)
    list_notes(data1)
    print(read_note(data1, input('Введите название заметки, которую хотите прочитать: ')))
    delete_note(data1, input('Введите название заметки, которую хотите удалить: '))
    write_file(filename, data1)
    print(list_notes(read_file(filename)))

    # for p in data:
    #     print()

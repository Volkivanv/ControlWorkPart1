import json
from datetime import datetime


class Repository:
    def __init__(self, filename):
        self.filename = filename
        self.max_id = 1

    def read_file(self):
        data = {}
        try:
            with open(self.filename, encoding='utf-8') as json_file:
                data = json.load(json_file)
                self.max_id = max([int(item) for item in data.keys()]) + 1
        except FileNotFoundError as err:
            print("Пока файл не создан. Чтобы он появился, добавьте первую заметку")
        return data

    def write_file(self, data):
        with open(self.filename, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, indent=4)

    def increment(self):
        self.max_id += 1


class Notebook:
    def __init__(self, filename, data):
        self.data_set = data
        self.filename = filename

    def list_notes(self):
        for note in self.data_set:
            print(f"{note}: {self.data_set[note]['title']} : {self.data_set[note]['date']}")

    def add_note(self, id):
        note_title = input('Введите название заметки: ')
        self.add_note_title(id, note_title)

    def add_note_title(self, id, title):
        note_text = input('Введите текст заметки: ')
        note_date = str(datetime.now())
        self.data_set[id] = {
            'title': title,
            'text': note_text,
            'date': note_date
        }

    def read_note(self, id):
        return self.data_set[id]

    def delete_note(self, id):
        del self.data_set[id]

    def get_notes_in_date(self, date_begin, date_end):
        notes = {}
        for note in self.data_set:
            note_date = datetime.strptime(self.data_set[note]['date'], '%Y-%m-%d %H:%M:%S.%f').date()
            if date_begin <= note_date <= date_end:
                notes[note] = self.data_set[note]
        return notes

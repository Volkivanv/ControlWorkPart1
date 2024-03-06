from datetime import datetime, date

from src.impl.data_work import Repository, Notebook


class View:
    def __init__(self, filename):
        self.filename = filename
        self.repository = Repository(filename)
        self.notebook = Notebook(filename, self.repository.read_file())

    def menu(self):
        while True:
            flag = len(self.notebook.data_set) > 0
            if flag:
                print('1. Список заметок')
            print('2. Добавить заметку')
            if flag:
                print('3. Просмотр заметки')
                print('4. Удалить заметку')
                print('5. Редактировать заметку')
                print('6. Сделать выборку по датам')
            print('7. Выход')

            choice = input('Введите выбор: ')
            if choice == '1':
                if not flag:
                    print('Список пуст')
                    continue
                self.notebook.list_notes()
            elif choice == '2':
                self.notebook.add_note(self.repository.max_id)
                self.repository.write_file(self.notebook.data_set)
                self.repository.increment()
                print('Заметка добавлена')
            elif choice == '3':
                if not flag:
                    print('Список пуст')
                    continue
                id = str(input('Введите id заметки: '))
                note = self.notebook.read_note(id)
                print(f"Заметка № {id}: {note['title']} : {note['date']}")
                print(note['text'])
            elif choice == '4':
                if not flag:
                    print('Список пуст')
                    continue
                id = str(input('Введите id удаляемой заметки: '))
                self.notebook.delete_note(id)
                self.repository.write_file(self.notebook.data_set)
                print('Заметка удалена')
            elif choice == '5':
                if not flag:
                    print('Список пуст')
                    continue
                id = str(input('Введите id редактируемой заметки: '))
                note_title = self.notebook.data_set[id]['title']
                self.notebook.add_note_title(id, title=note_title)
                self.repository.write_file(self.notebook.data_set)
                print('Заметка отредактирована')
            elif choice == '6':
                if not flag:
                    print('Список пуст')
                    continue
                date_begin = input('Введите начальную дату в формате: yyyy-mm-dd: ')
                date_begin = datetime.strptime(date_begin, '%Y-%m-%d').date()
                date_end = input('Введите конечную дату в формате: yyyy-mm-dd: ')
                date_end = datetime.strptime(date_end, '%Y-%m-%d').date()
                notes = self.notebook.get_notes_in_date(date_begin, date_end)
                if len(notes) == 0:
                    print('Список пуст')
                    continue
                for id in notes:
                    print(f"Заметка № {id}: {notes[id]['title']} : {notes[id]['date']}")
                   # print(note['text'])
            elif choice == '7':
                break
            else:
                print('Введите корректное число от 1 до 7')

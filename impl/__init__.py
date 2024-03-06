import json


class Repository:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data

    def write_file(self, data):
        with open(self.filename, 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile)

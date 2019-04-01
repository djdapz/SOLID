from open_closed_principle.Reader import Reader


class EvenLineReader(Reader):
    def read(self):
        return [line
                for index, line
                in enumerate(self.line_reader.read())
                if index % 2 == 0]

    def __init__(self, line_reader):
        self.line_reader = line_reader

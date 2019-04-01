from open_closed_principle.Reader import Reader


class LineReader(Reader):
    def read(self):
        output = []
        with open(self.file_name, '+r') as file:
            line = file.readline()
            while line:
                output.append(line)
                line = file.readline()
        return output

    def __init__(self, file_name):
        self.file_name = file_name

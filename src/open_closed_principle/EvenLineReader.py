from open_closed_principle.Reader import Reader


class EvenLineReader(Reader):
    def read(self):
        line_count = 0
        output = []
        with open(self.file_name, '+r') as file:
            line = file.readline()
            while line:
                if line_count % 2 == 0:
                    output.append(line)
                line_count += 1
                line = file.readline()
        return output

    def __init__(self, file_name):
        self.file_name = file_name

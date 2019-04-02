class ThirdLineReader:
    def read(self):
        output = []
        for index, line in enumerate(self.linereader.read()):
            if index % 3 == 2:
                output.append(line)
        return output

    def __init__(self, linereader):
        self.linereader = linereader

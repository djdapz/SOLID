class FourthLineReader:
    def read(self):
        output = []
        for index, line in enumerate(self.linereader.read()):
            if index % 4 == 0:
                output.append(line)
        return output

    def __init__(self, linereader):
        self.linereader = linereader

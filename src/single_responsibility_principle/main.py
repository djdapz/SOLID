class FileReporter:

    def __init__(self, output_file, input_file):
        self.output_file = output_file
        self.input_file = input_file

    def report(self):
        output_file = open("resources/" + self.output_file, "w+")
        input_file = open("resources/" + self.input_file, "r+")

        output_file.write(input_file.read())

        input_file.close()
        output_file.close()

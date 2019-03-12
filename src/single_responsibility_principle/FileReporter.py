class FileReporter:

    def __init__(self, output_file_name, file_contents):
        self.output_file_name = output_file_name
        self.file_contents = file_contents

    def report(self):
        with open(self.output_file_name, "w+") as output_file:
            output_file.write(self.file_contents)

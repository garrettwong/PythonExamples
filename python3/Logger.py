class Logger:
    def __init__(self, pathToFile):
        self.pathToFile = pathToFile

    def write(self, text):
        with open(self.pathToFile, 'a') as the_file:
            the_file.write(text + '\n')

# main
if __name__ == "__main__":
    logger = Logger('pathToLog.txt')
    logger.write('test message')
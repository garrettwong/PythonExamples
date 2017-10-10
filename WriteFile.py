from TimeManager import TimeManager
from RandomGenerator import RandomGenerator

class WriteFile:
    def write(self, baseDirectory):
        rg = RandomGenerator()
        randomStr = rg.getRandomString(10)

        ms = TimeManager().getTimeInMilliseconds()
        f = open(baseDirectory + 'workfile_' + str(randomStr), 'w')

        f.write('This is a test\n')

# main
if __name__ == "__main__":
    wf = WriteFile()
    wf.write('./file-watcher-folder/')
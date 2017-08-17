from os import listdir
from os.path import isfile, join
from os import walk


class DirectoryManager:
    def getFilesAndFolders(self, path):
        f = []
        for (dirpath, dirnames, filenames) in walk(path):
            f.extend(filenames)
            break
        return f

    def getFiles(self, path):
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        return onlyfiles

    def getFolders(self, path):
        onlyfolders = [f for f in listdir(path) if not isfile(join(path, f))]
        return onlyfolders


if __name__ == "__main__":
    dm = DirectoryManager()
    files = dm.getFiles('./file-watcher-folder/')
    folders = dm.getFolders('./file-watcher-folder/')
    print(files)
    print(folders)
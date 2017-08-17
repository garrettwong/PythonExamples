from TimeManager import TimeManager

baseDirectory = './file-watcher-folder/'
ms = TimeManager().getTimeInMilliseconds()
f = open(baseDirectory + 'workfile_' + str(ms), 'w')

f.write('This is a test\n')
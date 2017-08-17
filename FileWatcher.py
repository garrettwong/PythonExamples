import os
import time

class FileWatcher:
  def watch(self):
    path_to_watch = "./file-watcher-folder"
    before = dict([(f, None) for f in os.listdir(path_to_watch)])
    while 1:
        time.sleep(10)
        after = dict([(f, None) for f in os.listdir(path_to_watch)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        if added:
            print "Added: ", ", ".join(added)
        if removed:
            print "Removed: ", ", ".join(removed)
        before = after

f = FileWatcher()
f.watch()
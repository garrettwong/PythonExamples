import Queue

class FriendQueue:
    def __init__(self):
        self.queue = Queue.PriorityQueue()

    def add(self, person):
        self.queue.put(person)

    def get(self):
        return self.queue.get()

    def isEmpty(self):
        return self.queue.empty()
    

if __name__ == "__main__":
    fq = FriendQueue()
    fq.add((3, { 'name': 'Garrett '}))
    fq.add((6, { 'name': 'Eric '}))
    fq.add((5, { 'name': 'Bryan '}))

    while(not fq.isEmpty()):
        print(fq.get())

    

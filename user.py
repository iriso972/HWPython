class User:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def getFirst(self):
        return self.first

    def getLast(self):
        return self.last

    def getAll(self):
        print (f"{self.first} {self.last}")

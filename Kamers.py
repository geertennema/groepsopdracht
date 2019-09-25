class Kamer:

    def __init__(self, name, door, open, close, key):
        self.name = name 
        self.open = open 
        self.close = close
        self.key = key  
        self.open_door, self.close_door = door[1], door[0]

    def getout(self):
        if self.open_door > self.close_door:
            return 1 
        elif self.open_door == self.close_door:
            return 0 
        else:
            return key    



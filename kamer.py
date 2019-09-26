class Kamer:

    def __init__(self, naam):
        self.naam = naam
        #self.door = door

class Key:

    def __init__(self, keyCode):
        self.keyCode = keyCode

    def openDoor(self, door):
        if(self.keyCode == door.unlockCode):
            return True
        else:
            return False

class Door:

    def __init__(self,openDoor):
        self.openDoor = openDoor

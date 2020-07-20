class Park:
    def __init__(self, slotNumber):
        self.park = [None] * slotNumber

    def findAvailable(self):
        for i in range(0, len(self.park)):
            if self.park[i] == None:
                return i
        return -1

    def addCar(self, car):
        i = self.findAvailable()
        if(i != -1):
            self.park[i] = car
            return i+1
        return i

    def leaveCar(self, slotNumber):
        self.park[int(slotNumber)-1] = None

    def status(self):
        return self.park

    def findRegNumberWithColor(self, color):
        regNumbers = []
        for i in self.park:
            if i != None and i.color == color:
                regNumbers.append(i.regNumber)
        return regNumbers

    def findSlotNumberWithColor(self, color):
        slotNumbers = []
        for i in range(0, len(self.park)):
            car = self.park[i]
            if car != None and car.color == color:
                slotNumbers.append(str(i+1))
        return slotNumbers

    def findSlotNumberWithRegNumber(self, regNumber):
        slotNumbers = []
        for i in range(0, len(self.park)):
            car = self.park[i]
            if car != None and car.regNumber == regNumber:
                slotNumbers.append(str(i+1))
        return slotNumbers
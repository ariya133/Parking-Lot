from models.Park import Park
from models.Car import Car
from views import output 

class ParkController:
    def __init__(self):
        self.park = None  
              
    def createPark(self, slotNumber):
        s =int(slotNumber)
        self.park = Park(s)
        output.createdPark(s)

    def parkCar(self,regNumber, colour):
        i = self.park.addCar(Car(regNumber, colour))
        if(i == -1):
            output.parkedFail()
        else:
            output.parkedSuccessful(i)
    def leaveCar(self,slotNumber):
        self.park.leaveCar(slotNumber)
        output.leaved(slotNumber)

    def status(self):
        data = self.park.status()
        output.status(data)

    def findSlotNumberWithColour(self, colour):
        data = self.park.findSlotNumberWithColor(colour)
        if len(data) == 0:
            output.findFail()
        else:
            output.findSuccessful(data)

    def findSlotNumberWithRegNumber(self, regNumber):
        data = self.park.findSlotNumberWithRegNumber(regNumber)
        if len(data) == 0:
            output.findFail()
        else:
            output.findSuccessful(data)

    def findRegNumberWithColour(self, colour):
        data = self.park.findRegNumberWithColor(colour)
        if len(data) == 0:
            output.findFail()
        else:
            output.findSuccessful(data)
        
        
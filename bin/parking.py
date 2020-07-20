CMD_CREATE = 'create_parking_lot'
CMD_PARK = 'park'
CMD_LEAVE = 'leave'
CMD_STATUS = 'status'
CMD_FIND_SLOT_WITH_COLOR = 'slot_numbers_for_cars_with_colour'
CMD_FIND_SLOT_WITH_REG_NUMBER = 'slot_number_for_registration_number'
CMD_FIND_REG_NUMBER_WITH_COLOR = 'registration_numbers_for_cars_with_colour'


class Car:
    def __init__(self, regNumber, color):
        self.regNumber = regNumber
        self.color = color


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
        if(i == -1):
            print("Sorry, parking lot is full")
        else:
            self.park[i] = car
            print("park " + car.regNumber + " " + car.color)


park = None
while True:
    x = input(">>>")
    if x == 'exit':
        break
    cmd = x.split(" ")
    print(cmd[0])
    print(cmd[1])
    if(cmd[0] == CMD_CREATE):
        park = Park(int(cmd[1]))
        print('Created a parking lot with '+cmd[1]+' slots')

    elif(cmd[0] == CMD_PARK):
        park.addCar(Car(cmd[1], cmd[2]))

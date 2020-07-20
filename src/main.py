from parkController import ParkController
import sys

CMD_CREATE = 'create_parking_lot'
CMD_PARK = 'park'
CMD_LEAVE = 'leave'
CMD_STATUS = 'status'
CMD_FIND_SLOT_WITH_COLOR = 'slot_numbers_for_cars_with_colour'
CMD_FIND_SLOT_WITH_REG_NUMBER = 'slot_number_for_registration_number'
CMD_FIND_REG_NUMBER_WITH_COLOR = 'registration_numbers_for_cars_with_colour'


def operation(x):
    cmd = x.split(" ")
    if(cmd[0] == CMD_CREATE):
        parkController.createPark(cmd[1])

    elif(cmd[0] == CMD_PARK):
        parkController.parkCar(cmd[1], cmd[2])

    elif(cmd[0] == CMD_LEAVE):
        parkController.leaveCar(cmd[1])

    elif(cmd[0] == CMD_STATUS):
        parkController.status()

    elif(cmd[0] == CMD_FIND_REG_NUMBER_WITH_COLOR):
        parkController.findRegNumberWithColour(cmd[1])

    elif(cmd[0] == CMD_FIND_SLOT_WITH_COLOR):
        parkController.findSlotNumberWithColour(cmd[1])

    elif(cmd[0] == CMD_FIND_SLOT_WITH_REG_NUMBER):
        parkController.findSlotNumberWithRegNumber(cmd[1])


parkController = ParkController()
if(len(sys.argv) > 1):
    f = open(sys.argv[1])
    for line in f:
        operation(line.strip())

while True:
    x = input(">>>")
    if(x == 'exit'):
        break
    operation(x)

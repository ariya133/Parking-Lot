def createdPark(slotNumber):
    print('Created a parking lot with ' + str(slotNumber) + ' slots')


def parkedSuccessful(slotNumber):
    print("Allocated slot number: " + str(slotNumber))


def parkedFail():
    print("Sorry, parking lot is full")


def leaved(slotNumber):
    print("Slot number " + str(slotNumber) + " is free")


def status(cars):
    print("Slot No.     Registration No     Colour")
    for i in range(0, len(cars)):
        if(cars[i] != None):
            print(str(i+1) + "            "+cars[i].regNumber +
                  "       "+cars[i].color)


def findFail():
    print("Not found")


def findSuccessful(listData):
    print(", ".join(listData))

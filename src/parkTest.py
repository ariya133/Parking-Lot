import unittest
from models.Car import Car
from models.Park import Park


class TestPark(unittest.TestCase):
    def test_create_park(self):
        park = Park(3)
        expectPark = [None] * 3
        self.assertEqual(park.park, expectPark)
    
    def equalPark(self, park, expectedPark):
        self.assertEqual(len(park), len(expectedPark))
        for i in range(0,len(park)):
            if(expectedPark[i] == None):
                self.assertIsNone(park[i])
            else:
                self.assertEqual(expectedPark[i].regNumber, park[i].regNumber)
                self.assertEqual(expectedPark[i].color, park[i].color)

    def test_park_single_car(self):
        #prepare
        park = Park(3)
        expectedPark = [Car('xxx', 'red'), None, None]

        #execute
        park.addCar(Car('xxx','red'))

        #assert
        self.equalPark(park.park, expectedPark)

    def test_park_multi_car(self):
        #prepare
        park = Park(5)
        expectedPark = [Car('xxx', 'red'), Car('yyy', 'blue'), Car('zzz', 'green'), None, None]

        #execute
        park.addCar(Car('xxx','red'))
        park.addCar(Car('yyy','blue'))
        park.addCar(Car('zzz','green'))

        #assert
        self.equalPark(park.park, expectedPark)

    def test_park_full(self):
        #prepare
        park = Park(3)
        expectedPark = [Car('xxx', 'red'), Car('yyy', 'blue'), Car('zzz', 'green')]

        #execute
        park.addCar(Car('xxx','red'))
        park.addCar(Car('yyy','blue'))
        park.addCar(Car('zzz','green'))
        park.addCar(Car('aaa','red'))

        #assert
        self.equalPark(park.park, expectedPark)

    def test_leave_single_car(self):
        #prepare
        park = Park(5)
        park.park = [Car('xxx', 'red'), Car('yyy', 'blue'), Car('zzz', 'green'), Car('aaa', 'blue'), Car('bbb', 'red')]
        expectedPark = [Car('xxx', 'red'), None, Car('zzz', 'green'), Car('aaa', 'blue'), Car('bbb', 'red')]
        
        #execute
        park.leaveCar(2)

        #assert
        self.equalPark(park.park, expectedPark)

    def test_leave_multi_car(self):
        #prepare
        park = Park(5)
        park.park = [Car('xxx', 'red'), Car('yyy', 'blue'), Car('zzz', 'green'), Car('aaa', 'blue'), Car('bbb', 'red')]
        expectedPark = [None, Car('yyy', 'blue'), Car('zzz', 'green'), None, None]
        
        #execute
        park.leaveCar(1)
        park.leaveCar(4)
        park.leaveCar(5)

        #assert
        self.equalPark(park.park, expectedPark)
        
    def test_park_and_leave(self):
        #prepare
        park = Park(5)
        expectedPark = [Car('bbb', 'red'), Car('yyy', 'blue'), None, Car('aaa', 'blue'), None]
        
        #execute
        park.addCar(Car('xxx','red'))
        park.addCar(Car('yyy','blue'))
        park.addCar(Car('zzz','green'))
        park.addCar(Car('aaa','blue'))
        park.leaveCar(1)
        park.leaveCar(3)
        park.addCar(Car('bbb','red'))
        
        #assert
        self.equalPark(park.park, expectedPark)

    def test_find_reg_number_with_colour_not_found(self):
        #prepare
        park = Park(5)
        park.park = [Car('xxx', 'red'), Car('yyy', 'blue'), Car('zzz', 'green'), Car('aaa', 'blue'), Car('bbb', 'red')]
        expectedRegNumbers = []
        
        #execute
        regNumbers = park.findRegNumberWithColor('white')

        #assert
        self.assertListEqual(regNumbers,expectedRegNumbers)

    def test_find_reg_number_with_colour_single(self):
        #prepare
        park = Park(5)
        park.park = [Car('xxx', 'red'), Car('yyy', 'blue'), Car('zzz', 'green'), Car('aaa', 'blue'), Car('bbb', 'red')]
        expectedRegNumbers = ['zzz']
        
        #execute
        regNumbers = park.findRegNumberWithColor('green')

        #assert
        self.assertListEqual(regNumbers,expectedRegNumbers)

    def test_find_reg_number_with_colour_multi(self):
        #prepare
        park = Park(5)
        park.park = [Car('xxx', 'red'), Car('yyy', 'blue'), Car('zzz', 'green'), Car('aaa', 'blue'), Car('bbb', 'red')]
        expectedRegNumbers = ['xxx','bbb']
        
        #execute
        regNumbers = park.findRegNumberWithColor('red')

        #assert
        self.assertListEqual(regNumbers,expectedRegNumbers)
    
    def test_find_slot_number_with_colour_not_found(self):
        #prepare
        park = Park(5)
        park.park = [Car('xxx', 'red'), Car('yyy', 'blue'), Car('zzz', 'green'), Car('aaa', 'blue'), Car('bbb', 'red')]
        expectedSlotNumbers = []
        
        #execute
        regNumbers = park.findSlotNumberWithColor('white')

        #assert
        self.assertListEqual(regNumbers, expectedSlotNumbers)

    def test_find_slot_number_with_colour_single(self):
        #prepare
        park = Park(5)
        park.park = [Car('xxx', 'red'), Car('yyy', 'blue'), Car('zzz', 'green'), Car('aaa', 'blue'), Car('bbb', 'red')]
        expectedSlotNumbers = ['3']
        
        #execute
        regNumbers = park.findSlotNumberWithColor('green')

        #assert
        self.assertListEqual(regNumbers, expectedSlotNumbers)

    def test_find_slot_number_with_colour_multi(self):
        #prepare
        park = Park(5)
        park.park = [Car('xxx', 'red'), Car('yyy', 'blue'), Car('zzz', 'green'), Car('aaa', 'blue'), Car('bbb', 'red')]
        expectedSlotNumbers = ['1','5']
        
        #execute
        regNumbers = park.findSlotNumberWithColor('red')

        #assert
        self.assertListEqual(regNumbers, expectedSlotNumbers)

    def test_find_slot_number_with_reg_number_not_found(self):
        #prepare
        park = Park(5)
        park.park = [Car('xxx', 'red'), Car('yyy', 'blue'), Car('zzz', 'green'), Car('aaa', 'blue'), Car('bbb', 'red')]
        expectedSlotNumbers = []
        
        #execute
        regNumbers = park.findSlotNumberWithRegNumber('sss')

        #assert
        self.assertListEqual(regNumbers, expectedSlotNumbers)

    def test_find_slot_number_with_reg_number(self):
        #prepare
        park = Park(5)
        park.park = [Car('xxx', 'red'), Car('yyy', 'blue'), Car('zzz', 'green'), Car('aaa', 'blue'), Car('bbb', 'red')]
        expectedSlotNumbers = ['2']
        
        #execute
        regNumbers = park.findSlotNumberWithRegNumber('yyy')

        #assert
        self.assertListEqual(regNumbers, expectedSlotNumbers)


if __name__ == '__main__':
    unittest.main()

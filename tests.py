import unittest
from elevator import Elevator


class ValidateElevatorClass(unittest.TestCase):

    def test_init_params(self):
        """should store correct initial parameters when elevator is initalized"""
        elevator = Elevator(5, 2)
        self.assertEqual(elevator.num_floors, 5)
        self.assertEqual(elevator.current_floor, 2)
        self.assertSetEqual(elevator.requested_floors, set())
        self.assertListEqual(elevator.visited_floors, [])
        self.assertEqual(elevator.num_floors_traveled, 0)


    def test_request_floor(self):
        """should register requested floors"""
        elevator = Elevator(5, 1)
        elevator.request_floor(3)
        elevator.request_floor(5)
        self.assertSetEqual(elevator.requested_floors, {3, 5})


    def test_visited_floors(self):
        """should register visited floors in order"""
        elevator = Elevator(num_floors=5, starting_floor=5)
        elevator.request_floor(4)
        elevator.request_floor(2)
        elevator.travel()
        self.assertListEqual(elevator.visited_floors, [4, 2])


    def test_current_floor_after_travel(self):
        """should set current floor to last visited floor"""
        elevator = Elevator(num_floors=6, starting_floor=4)
        elevator.request_floor(5)
        elevator.request_floor(2)
        elevator.travel()
        self.assertEqual(elevator.current_floor, 2)


    def test_num_floors_traveled_up(self):
        """should keep track of the number of floors traveled going up and should provide message showing that elevator is now at desired floor"""
        elevator = Elevator(num_floors=5, starting_floor=1)
        elevator.request_floor(5)
        elevator.travel()
        self.assertEqual(elevator.num_floors_traveled, 4)

   

    def test_num_floors_traveled_down(self):
        """should keep track of the number of floors traveled going down"""
        elevator = Elevator(num_floors=5, starting_floor=5)
        elevator.request_floor(1)
        elevator.travel()
        self.assertEqual(elevator.num_floors_traveled, 4)


    def test_num_floors_traveled_up_down(self):
        """should keep track of the number of floors traveled going up then down"""
        elevator = Elevator(num_floors=5, starting_floor=3)
        elevator.request_floor(5)
        elevator.request_floor(1)
        elevator.travel()
        self.assertEqual(elevator.num_floors_traveled, 6)

    def test_num_current_floor(self):
         
        """view the current floor of the elevator at any given time."""   
        elevator = Elevator(num_floors=5, starting_floor=1)
        elevator.request_floor(5)
        elevator.travel()
        self.assertEqual(elevator.num_floors_traveled, 4)

    def test_duplicate_floor_requests(self):
        """gnore duplicate floor requests"""
        elevator = Elevator(num_floors=5, starting_floor=1)
        elevator.request_floor(3)
        elevator.request_floor(3)
        self.assertSetEqual(elevator.requested_floors, {3})
        elevator.travel()
        self.assertListEqual(elevator.visited_floors, [3])


if __name__ == '__main__':
    unittest.main()
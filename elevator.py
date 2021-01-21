class Elevator:

    # Initializes a new Elevator object
    def __init__(self, num_floors, starting_floor):
        # Total number of floors accessible by the elevator
        self.num_floors = num_floors
        # Current floor number
        self.current_floor = starting_floor
        # An unordered set of floor numbers that have been requested
        self.requested_floors = set()
        # An ordered list of floors that have been visited
        self.visited_floors = []
        # Number of floors traveled since the elevator was started
        self.num_floors_traveled = 0

    def request_floor(self, floor):
        self.requested_floors.add(floor)

    
    def get_floor_difference(self, floor):
        return abs(self.current_floor - floor)

    # Travels to the given floor to pick up or drop off passengers
    def visit_floor(self, floor):
        self.num_floors_traveled += self.get_floor_difference(floor)
        self.current_floor = floor
        self.visited_floors.append(self.current_floor)
        self.requested_floors.discard(self.current_floor)

    # Starts elevator and travels computed route according to current requests
    def travel(self):
       
        while len(self.requested_floors) != 0:
            closest_floor = min(
                self.requested_floors, key=self.get_floor_difference)
            self.visit_floor(closest_floor)

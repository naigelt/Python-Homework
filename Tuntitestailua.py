
class Elevator:

    def __init__(self, first_floor, top_floor):
        self.first_floor = first_floor
        self.top_floor = top_floor
        self.floor = first_floor

    def info(self):
        print(f"Buildings first floor: {self.first_floor}\n")
        print(f"Buildings top floor: {self.top_floor}\n")
        print(f"The current floor you are on: {self.floor}\n")

    def floor_up(self):
        self.floor += 1

    def floor_down(self):
        self.floor -= 1

    def move_to_floor(self, target_floor):
        while self.floor != target_floor:
            if target_floor > self.floor:
                self.floor_up()
                print(self.floor)
            else:
                self.floor_down()
                print(self.floor)


elevator = Elevator(1, 10)
elevator.move_to_floor(5)
elevator.info()
elevator.move_to_floor(elevator.first_floor)
elevator.info()
#Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen.
#Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

class Building:

    def __init__(self, first_floor, top_floor, elevator_number):
        self.first_floor = first_floor
        self.top_floor = top_floor
        self.elevators = []
        self.elevator_number = elevator_number
        for i in range(elevator_number):
            self.elevators.append(Elevator(first_floor, top_floor))

    def info(self):
        print(f"Buildings top floor is {self.top_floor} the first floor is {self.first_floor} and there are {self.elevator_number}  elevators in the building.")


    def run_elevator(self, elevator_number, elevator_floor):
        elevator = self.elevators[elevator_number - 1]
        print(f"Riding elevator number {elevator_number}")
        elevator.move_to_floor(elevator_floor)

    def fire_alarm(self):
        print("Fire alarm caution caution fire alarm")
        for i in self.elevators:
            i.move_to_floor(i.first_floor)
        print("All elevators are in the first floor")



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
        print(f"Your are at floor {self.floor}")


    def floor_down(self):
        self.floor -= 1
        print(f"You are at floor {self.floor}")

    def move_to_floor(self, target_floor):
        while self.floor != target_floor:
            if target_floor > self.floor:
                self.floor_up()
            else:
                self.floor_down()


if __name__ == '__main__':
    building = Building(1, 6, 3)
    building.info()
    building.run_elevator(3, 5)
    building.fire_alarm()
    building.info()


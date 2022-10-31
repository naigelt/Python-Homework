# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.


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
        for i in self.elevators:
            pass

    def run_elevator(self, elevator_number, elevator_floor):
        elevator = self.elevators[elevator_number - 1]
        print(f"Riding elevator number {elevator_number}")
        elevator.move_to_floor(elevator_floor)


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
                print(f"Floor number{self.floor}")
            else:
                self.floor_down()
                print(f"Floor number{self.floor}")

if __name__ == '__main__':
    building = Building(1, 6, 3)
    building.info()
    building.run_elevator(1, 3)



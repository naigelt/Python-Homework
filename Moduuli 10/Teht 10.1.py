#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen
# ja sen jälkeen takaisin alimpaan kerrokseen.



class Elevator:

    def __init__(self, first_floor, top_floor, current_floor):
        self.first_floor = first_floor
        self.top_floor = top_floor
        self.current_floor = first_floor

    def info(self):
        print(f"Buildings first floor: {self.first_floor}\n")
        print(f"Buildings top floor: {self.top_floor}\n")
        print(f"The current floor you are on: {self.current_floor}\n")

    def move_to_floor(self, floor):
        if self.first_floor < floor > self.top_floor:
            self.curret_floor = floor
        elif floor < 0:
            self.current_floor = 0
        else:
            self.current_floor = 10

    def floor_up(self):
        if self.current_floor < 10:
            self.current_floor = self.current_floor +1

    def floor_down(self):
        if self.current_floor > 0:
            self.current_floor -= 1

elevator = Elevator(1, 10, 0)
Elevator.info(elevator)
elevator.floor_up()
Elevator.info(elevator)
elevator.floor_down()
Elevator.info(elevator)


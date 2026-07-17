class WinnerMessi:
    def __init__(self):
        self.name = "Lionel"
        self.surname = "Messi"
        self.age = 38
        self.gender = "Male"
        self.height = 1.70  # metri
        self.weight = 64    # kg

    def show_info(self):
        print(f"Nome: {self.name}")
        print(f"Cognome: {self.surname}")
        print(f"Età: {self.age}")
        print(f"Genere: {self.gender}")
        print(f"Altezza: {self.height} m")
        print(f"Peso: {self.weight} kg")


winner_messi = WinnerMessi()

if __name__ == "__main__":
    winner_messi.show_info()
    print("Messi")
    print("Lionel")
    print("Only Final")

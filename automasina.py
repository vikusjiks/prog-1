class Automasina:
    def __init__(self, krasa, marka, modelis):
        self.krasa = krasa
        self.marka = marka
        self.modelis = modelis

    def est(self):
        print(f"{self.marka} {self.modelis} sabruka")

bmw = Automasina("Rozā", "BMW", "e36")
audi = Automasina("Melns", "Audi", "X5")

bmw.est()
audi.est()
class Vrchol:
    def __init__(self, cislo: int, cena: int) -> None:
        self.cislo = cislo
        self.cena = cena
        self.z = 0
        self.k = 0
        self.stupen = 0

    def __str__(self) -> str:
        return f"{self.cislo:4} {self.cena:8} {self.z:9} {self.k:8}"

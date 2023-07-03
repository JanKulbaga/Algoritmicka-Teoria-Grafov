class Hrana:
    def __init__(self, u: int, v: int, kapacita: int) -> None:
        self.u = u
        self.v = v
        self.kapacita = kapacita
        self.tok = 0

    def __str__(self) -> str:
        return f"{self.u:4} {self.v:9} {self.kapacita:10} {self.tok:6}"

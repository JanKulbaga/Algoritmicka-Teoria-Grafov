from __future__ import annotations


class Digraf:
    def __init__(self, pocet_vrcholov: int, pocet_hran: int) -> None:
        self.pocet_vrcholov = pocet_vrcholov
        self.pocet_hran = pocet_hran
        self.hrany = [[0 for _ in range(3)] for _ in range(self.pocet_hran)]

    @staticmethod
    def nacitajSubor(nazovSuboru: str) -> Digraf:
        pocet_vrcholov = 1
        pocet_hran = 0
        with open(nazovSuboru) as file:
            for line in file:
                u, v, _ = map(int, line.split())
                pocet_hran += 1
                pocet_vrcholov = max(pocet_vrcholov, u, v)

        g = Digraf(pocet_vrcholov, pocet_hran + 1)

        with open(nazovSuboru) as file:
            for j, line in enumerate(file, start=1):
                u, v, c = map(int, line.split())
                g.hrany[j][0] = u
                g.hrany[j][1] = v
                g.hrany[j][2] = c

        return g

    def tried_podla_prveho_druheho_stlpca(self) -> None:
        self.hrany.sort(key=lambda x: (x[0], x[1]))

    def vytvor_smernik_vrcholov(self) -> None:
        self.smernikVrcholov = [0] * (self.pocet_vrcholov + 2)
        for i in range(self.pocet_hran):
            vrchol = self.vrchol_u(i)
            if self.smernikVrcholov[vrchol] == 0:
                self.smernikVrcholov[vrchol] = i
        self.smernikVrcholov[self.pocet_vrcholov + 1] = self.pocet_hran
        for i in range(self.pocet_vrcholov, 0, -1):
            if self.smernikVrcholov[i] == 0:
                self.smernikVrcholov[i] = self.smernikVrcholov[i + 1]

    def vrchol_u(self, i: int) -> int:
        return self.hrany[i][0]

    def vrchol_v(self, i: int) -> int:
        return self.hrany[i][1]

    def cena(self, i: int) -> int:
        return self.hrany[i][2]

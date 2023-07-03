from __future__ import annotations


class Graf:
    def __init__(self, pocet_vrcholov: int, pocet_hran: int) -> None:
        self.pocet_vrcholov = pocet_vrcholov
        self.pocet_hran = pocet_hran
        self.hrany = [[0 for _ in range(3)] for _ in range(self.pocet_hran)]

    @staticmethod
    def nacitajSubor(nazovSuboru) -> Graf:
        pocet_vrcholov = 1
        pocet_hran = 0
        with open(nazovSuboru) as file:
            for line in file:
                u, v, _ = map(int, line.split())
                pocet_hran += 1
                pocet_vrcholov = max(pocet_vrcholov, u, v)

        g = Graf(pocet_vrcholov, pocet_hran + 1)

        with open(nazovSuboru) as file:
            for j, line in enumerate(file, start=1):
                u, v, c = map(int, line.split())
                g.hrany[j][0] = u
                g.hrany[j][1] = v
                g.hrany[j][2] = c

        return g

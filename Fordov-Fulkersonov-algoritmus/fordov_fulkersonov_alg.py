from queue import Queue
from graf import Graf


class FordovFulkersonovAlg:
    def __init__(self, graf: Graf) -> None:
        self.graf = graf

    def maximalny_tok(self) -> None:
        zdroj = 1
        ustie = self.graf.pocet_vrcholov

        pole_predchodcov = [-1] * (self.graf.pocet_vrcholov + 1)
        maximalny_tok = 0

        while self.zvacsujuca_polocesta(zdroj, ustie, pole_predchodcov):
            rezerva_polocesty = float("inf")

            v = ustie
            while v != zdroj:
                u = pole_predchodcov[v]
                for hrana in self.graf.hrany[1:]:
                    if hrana.u == u and hrana.v == v:
                        rezerva_polocesty = min(
                            rezerva_polocesty, hrana.kapacita - hrana.tok
                        )
                v = u

            maximalny_tok += rezerva_polocesty

            v = ustie
            while v != zdroj:
                u = pole_predchodcov[v]
                for hrana in self.graf.hrany[1:]:
                    if hrana.u == u and hrana.v == v:
                        hrana.tok += rezerva_polocesty
                v = u

        print(f"Zdroj: {zdroj}")
        print(f"Ustie: {ustie}")
        print(f"Maximalny tok: {maximalny_tok}")
        print("Vrchol_U  Vrchol_V  Kapacita  Tok")
        for hrana in self.graf.hrany[1:]:
            print(hrana)

    def zvacsujuca_polocesta(self, zdroj, ustie, pole_predchodcov) -> bool:
        navstivene = [False] * (self.graf.pocet_vrcholov + 1)

        epsilon = Queue()
        epsilon.put(zdroj)
        navstivene[zdroj] = True

        while not epsilon.empty():
            r = epsilon.get()
            for hrana in self.graf.hrany[1:]:
                if (
                    hrana.u == r
                    and not navstivene[hrana.v]
                    and (hrana.kapacita - hrana.tok) > 0
                ):
                    navstivene[hrana.v] = True
                    pole_predchodcov[hrana.v] = r
                    epsilon.put(hrana.v)

        return navstivene[ustie]

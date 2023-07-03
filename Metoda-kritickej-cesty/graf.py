from hrana import Hrana
from vrchol import Vrchol


class Graf:
    def nacitaj_hrany_zo_suboru(self, file_name: str) -> None:
        self.hrany = [Hrana(0, 0, 0)]
        with open(file_name) as file:
            for line in file:
                u, v, c = map(int, line.split())
                self.hrany.append(Hrana(u, v, c))

    def nacitaj_vrcholy_s_cinnostami(self, file_name: str) -> None:
        self.vrcholy = [Vrchol(-1, -1)]
        with open(file_name) as file:
            self.vrcholy.extend(
                Vrchol(int(cislo + 1), int(cena)) for cislo, cena in enumerate(file)
            )

    def monotonne_ocisluj_vrcholy(self) -> None:
        for hrana in self.hrany[1:]:
            self.vrcholy[hrana.vrchol_v].stupen += 1

        self.monotonne_ocislovane_vrcholy = [
            vrchol for vrchol in self.vrcholy[1:] if vrchol.stupen == 0
        ]

        for vrchol in self.monotonne_ocislovane_vrcholy:
            for hrana in self.hrany:
                if vrchol.cislo != hrana.vrchol_u:
                    continue
                v = self.vrcholy[hrana.vrchol_v]
                v.stupen -= 1
                if v.stupen == 0:
                    self.monotonne_ocislovane_vrcholy.append(v)

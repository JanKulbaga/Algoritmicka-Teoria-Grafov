from graf import Graf


class CPM:
    def __init__(self, graf: Graf) -> None:
        self.graf = graf

    def cpm(self) -> None:
        trvanie_projektu = 0

        for v in self.graf.monotonne_ocislovane_vrcholy:
            for hrana in self.graf.hrany:
                if v.cislo != hrana.vrchol_u:
                    continue
                vrchol = self.graf.vrcholy[hrana.vrchol_v]
                vrchol.z = max(vrchol.z, v.z + v.cena)
                trvanie_projektu = max(trvanie_projektu, vrchol.z + vrchol.cena)

        for vrchol in self.graf.vrcholy:
            vrchol.k = trvanie_projektu

        for v in reversed(self.graf.monotonne_ocislovane_vrcholy):
            for hrana in self.graf.hrany:
                if v.cislo != hrana.vrchol_v:
                    continue
                vrchol = self.graf.vrcholy[hrana.vrchol_u]
                vrchol.k = min(vrchol.k, v.k - v.cena)

        print("Cinnost  Trvanie  Zaciatok  Koniec")
        for vrchol in self.graf.vrcholy[1:]:
            print(vrchol)

        print(f"Doba trvania projektu: {trvanie_projektu}")

        print("Kriticke cinnosti:", end=" ")
        kriticke_cinnosti = []
        for vrchol in self.graf.vrcholy[1:]:
            rezerva = vrchol.k - vrchol.z - vrchol.cena
            if rezerva == 0:
                kriticke_cinnosti.append(vrchol.cislo)
        print(",".join([str(vrchol) for vrchol in kriticke_cinnosti]))

        print("Kriticka cesta:", end=" ")
        kriticka_cesta = []
        for vrchol in self.graf.monotonne_ocislovane_vrcholy:
            rezerva = vrchol.k - vrchol.z - vrchol.cena
            if rezerva == 0:
                kriticka_cesta.append(vrchol.cislo)
        print(" -> ".join([str(vrchol) for vrchol in kriticka_cesta]))

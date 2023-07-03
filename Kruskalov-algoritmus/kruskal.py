from graf import Graf


class Kruskal:
    def __init__(self, graf: Graf) -> None:
        self.graf = graf

    def najlacnejsia_kostra(self) -> None:
        hrany = self.graf.hrany[:]
        hrany.sort(key=lambda x: x[2])
        hrany.pop(0)

        hranyKostry = []
        komponenty = list(range(self.graf.pocet_vrcholov + 1))

        while hrany and len(hranyKostry) != self.graf.pocet_vrcholov - 1:
            hrana_u, hrana_v, hrana_c = hrany.pop(0)
            if komponenty[hrana_u] != komponenty[hrana_v]:
                hranyKostry.append((hrana_u, hrana_v, hrana_c))
                stary_komponent = komponenty[hrana_v]
                novy_komponent = komponenty[hrana_u]
                for i in range(len(komponenty)):
                    if komponenty[i] == stary_komponent:
                        komponenty[i] = novy_komponent

        cenaKostry = sum(hrana_c for _, _, hrana_c in hranyKostry)

        print(f"Cena najlacnejšej kostry: {cenaKostry}")
        print("Hrany najlacnejšej kostry:")
        print([(hrana_u, hrana_v) for hrana_u, hrana_v, _ in hranyKostry])

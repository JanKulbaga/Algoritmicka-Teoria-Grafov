from graf import Graf
from CPM import CPM


def main() -> None:
    graf = Graf()
    graf.nacitaj_hrany_zo_suboru("data/CPM_midi.hrn")
    graf.nacitaj_vrcholy_s_cinnostami("data/CPM_midi.tim")
    graf.monotonne_ocisluj_vrcholy()
    cpm = CPM(graf)
    cpm.cpm()


if __name__ == "__main__":
    main()

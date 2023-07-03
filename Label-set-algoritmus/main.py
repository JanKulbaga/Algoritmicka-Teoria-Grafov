from labelset import LabelSet
from digraf import Digraf


def main() -> None:
    digraf = Digraf.nacitajSubor("data/SlovRep.hrn")
    digraf.tried_podla_prveho_druheho_stlpca()
    digraf.vytvor_smernik_vrcholov()
    labelset = LabelSet(digraf)
    while True:
        try:
            u = int(input("Nacitaj zaciatocny vrchol: "))
            v = int(input("Nacitaj koncovy vrchol: "))
            labelset.najdi_najkratsiu_cestu(u, v)
        except ValueError:
            print("Zadajte platne cele cislo.")
            continue

        while True:
            ukoncit = input("Chcete ukoncit program? (a/n) ").lower()
            if ukoncit == "a":
                exit(0)
            elif ukoncit == "n":
                break


if __name__ == "__main__":
    main()

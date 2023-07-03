from graf import Graf
from kruskal import Kruskal


def main() -> None:
    graf = Graf.nacitajSubor("data/pr3.hrn")
    kruskal = Kruskal(graf)
    kruskal.najlacnejsia_kostra()


if __name__ == "__main__":
    main()

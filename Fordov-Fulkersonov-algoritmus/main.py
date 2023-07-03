from graf import Graf
from fordov_fulkersonov_alg import FordovFulkersonovAlg


def main() -> None:
    graf = Graf()
    graf.nacitaj_hrany_zo_suboru("data/Tok_mini.hrn")
    alg = FordovFulkersonovAlg(graf)
    alg.maximalny_tok()


if __name__ == "__main__":
    main()

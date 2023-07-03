from queue import PriorityQueue
from digraf import Digraf


class LabelSet:
    def __init__(self, digraf: Digraf) -> None:
        self.MAX_HODNOTA = float("inf") / 2
        self.digraf = digraf

    def najdi_najkratsiu_cestu(self, u: int, v: int) -> None:

        vzdialenosti = [self.MAX_HODNOTA] * (self.digraf.pocet_vrcholov + 1)
        predchadzajuci = [0] * (self.digraf.pocet_vrcholov + 1)

        vzdialenosti[u] = 0

        epsilon = PriorityQueue()
        epsilon.put((0, u))

        while not epsilon.empty():

            _, r = epsilon.get()

            for i in range(
                self.digraf.smernikVrcholov[r], self.digraf.smernikVrcholov[r + 1]
            ):
                nova_vzdialenost = vzdialenosti[r] + self.digraf.cena(i)
                if vzdialenosti[self.digraf.vrchol_v(i)] > nova_vzdialenost:
                    vzdialenosti[self.digraf.vrchol_v(i)] = nova_vzdialenost
                    predchadzajuci[self.digraf.vrchol_v(i)] = r
                    epsilon.put(
                        (
                            vzdialenosti[self.digraf.vrchol_v(i)],
                            self.digraf.vrchol_v(i),
                        )
                    )

        if vzdialenosti[v] == self.MAX_HODNOTA:
            print(f"Vrchol {v} nie je dosiahnutelny!")
            return

        path = []
        curr = v
        while curr != u:
            path.append(curr)
            curr = predchadzajuci[curr]
        path.append(u)

        print(f"Najkratsia cesta z vrchola {u} do vrchola {v}")
        print("Cesta: ", end="")
        print(" -> ".join([str(num) for num in reversed(path)]))
        print(f"Vzdialenost: {vzdialenosti[v]}")

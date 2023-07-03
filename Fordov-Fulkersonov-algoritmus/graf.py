from hrana import Hrana


class Graf:
    def nacitaj_hrany_zo_suboru(self, file_name: str) -> None:
        self.hrany = [Hrana(0, 0, 0)]
        self.pocet_vrcholov = 1
        with open(file_name) as file:
            for line in file:
                u, v, kapacita = map(int, line.split())
                self.pocet_vrcholov = max(self.pocet_vrcholov, u, v)
                self.hrany.append(Hrana(u, v, kapacita))

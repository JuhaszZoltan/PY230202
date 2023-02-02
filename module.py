class Versenyzo:
    def __init__(self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.rajtszam:str = v[0]
        self.kategoria:str = v[1]
        self.nev:str = v[2]
        self.egyesulet:str = v[3]
        self.ido:str = v[4]

        if   self.rajtszam[0] == 'M': self.tav:str = 'Mini'
        elif self.rajtszam[0] == 'R': self.tav:str = 'Rövid'
        elif self.rajtszam[0] == 'K': self.tav:str = 'Közép'
        elif self.rajtszam[0] == 'H': self.tav:str = 'Hosszú'
        elif self.rajtszam[0] == 'E': self.tav:str = 'Pedelec'
        else:                         self.tav:str = '_'

        if   self.kategoria[-1] == 'f': self.nem = 'férfi'
        elif self.kategoria[-1] == 'n': self.nem = 'nő'
        else:                           self.nem = '_'

        id:list[str] = self.ido.split(':')
        self.ido_mpben:int = int(id[0]) * 3600 + int(id[1]) * 60 + int(id[2])


def versenyzok_szama(lista:list[Versenyzo], tav:str, nem:str) -> int:
    c:int = 0
    for v in lista:
        if v.tav == tav and v.nem == nem:
            c += 1
    return c


def versenyzo_orafolott(lista:list[Versenyzo], ora:float) -> bool:
    for v in lista:
        if v.ido_mpben > ora * 3600:
            return True
    return False


def gyoztes_versenyzo(lista:list[Versenyzo], tav:str, kategoria:str) -> Versenyzo:
    szurt:list[Versenyzo] = []
    for v in lista:
        if v.tav == tav and v.kategoria == kategoria:
            szurt.append(v)
    mini:int = 0
    for i in range(1, len(szurt)):
        if szurt[i].ido_mpben < szurt[mini].ido_mpben:
            mini = i
    return szurt[mini]


def statisztika(lista:list[Versenyzo], nem:str):
    dc:dict[str, int] = {}
    for ver in lista:
        if ver.nem == nem:
            if ver.kategoria not in dc.keys():
                dc[ver.kategoria] = 1
            else: dc[ver.kategoria] += 1
    return dc.items()
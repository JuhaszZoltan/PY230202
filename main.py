from module import Versenyzo, versenyzok_szama, versenyzo_orafolott, gyoztes_versenyzo, statisztika

versenyzok:list[Versenyzo] = []
file = open(file='bukkm2019.txt', encoding='UTF-8')
for s in file.readlines()[1:]:
    versenyzok.append(Versenyzo(s))

f4:float = 100 - (len(versenyzok) / 691 * 100)
print(f'4f: versenytávot nem teljesítők: {round(f4, 3)}%')

f5:int = versenyzok_szama(versenyzok, 'Rövid', 'nő')
print(f'5f: női versenyzők száma rövid távú versenyen: {f5} fő')

f6:bool = versenyzo_orafolott(versenyzok, 6)
if f6: print('f6: volt ilyen versenyző')
else: print('f6: nem volt ilyen versenyző')

f7:Versenyzo = gyoztes_versenyzo(versenyzok, 'Rövid', 'ff')
print('f7: ff kategória győztese rövid távon:')
print(f'\trajtszám: {f7.rajtszam}')
print(f'\tnév: {f7.nev}')
print(f'\tegyesület: {f7.egyesulet}')
print(f'\tidő: {f7.ido}')

f8 = statisztika(versenyzok, 'férfi')
print('f8: statisztika')

for k, v in f8:
    print(f'\t{k} - {v} fő')
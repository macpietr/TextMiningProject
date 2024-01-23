from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager

objectsManager = ObjectsManager()

slownik = objectsManager.getSavedObject('dictOfDictsOfAirlinesClustersOpinions')

# Słowo do wyszukania
szukane_slowo = 'rude'

# Przeszukiwanie słownika
znalezione = []

for klucz, lista in slownik.items():
    if szukane_slowo in lista:
        indeks_slowa = lista.index(szukane_slowo)
        znalezione.append((klucz, indeks_slowa))

# Wyświetlanie wyników
if znalezione:
    for klucz, indeks_slowa in znalezione:
        print(f'Słowo "{szukane_slowo}" zostało znalezione w liście związanym z kluczem {klucz} na pozycji {indeks_slowa}.')
else:
    print(f'Słowo "{szukane_slowo}" nie zostało znalezione w słowniku.')
def parzyste(lista):
    wynik = []
    for liczba in lista:
        if liczba % 2 == 0:
            wynik.append(liczba)
    return wynik


lista1 = [5, 17, 7, 9, 1, 25, 22, 8, 7, 11]
wynik = parzyste(lista1)
print(wynik)

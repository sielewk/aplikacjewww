"""Stwórz funkcję, która jako parametry przyjmuje dwie listy a_list oraz b_list. Następnie zwróć listę,
która będzie posiadać parzyste indeksy z listy a_list oraz nieparzyste z b_list."""

def zad1(a_list=[2,4,3],b_list=[3,4,5]):
    if a_list%2==0:
        return (a_list)
    if b_list%2==1:
        return (b_list)
print(zad1(a_list=[2,4,3],b_list=[3,4,5]))
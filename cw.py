import pandas as pd
import random

lista1 = []
for el in range(10):
    lista1.append( random.randint(0,100))

dane1 = pd.Series(lista1)

#print(dane1)
print (lista1)

print(dane1[dane1.values>50].mean())
print (dane1[dane1>60][:5].count())
print(dane1[:5][dane1>60].count())
print(dane1.max())












lista2 = [31,28,30,31]
indeksy = ["styczen","luty","marzec","kwiecien"]
dane2 = pd.Series(lista2,index=indeksy)
#print(dane2)

#print(dane2.loc["styczeń"]) szuka po etykietach (styczen, luty...)
#print(dane2.iloc[0:2]) # szuka po indeksach ;        (iloc[:3]-> wszystkie el do 3)



# krotka = (13,21,5,5,43)
# dane3 = pd.Series(krotka)
# print(f"Krotka: {dane3}")



# slownik = {"styczen":31,"luty":28,"marzec":30,"kwiecień":31}
# dane4 = pd.Series(slownik)
# print( {dane4})


# print(dane[dane>6][dane<70])
# print(dane.to_string()) <- zobaczyszmy wszystkie dane

# dane.head() - nagłówel
# dane.tail() - stopka
# dane.head().mean() - srednia wartość z 5 pierwszych elementów -> mean() - średnia





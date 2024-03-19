import pandas as pd
import random

lista1 = []
for el in range(10):
    lista1.append( random.randint(0,100))

dane1 = pd.Series(lista1)


df = pd.DataFrame(lista1)
# print(df)

csv1 = pd.read_csv("Pracownicy 1.csv",sep=";")
csv2 = pd.read_csv("Pracownicy 1.csv")

print(csv1)
print("===============")
print(csv2)


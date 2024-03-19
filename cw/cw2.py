import pandas as pd
import random

# lista1 = []
# for el in range(10):
#     lista1.append( random.randint(0,100))

# dane1 = pd.Series(lista1)


# df1 = pd.DataFrame(lista1)
# #print(df)


# csv1 = pd.read_csv("Pracownicy 1.csv",sep=";")
csv2 = pd.read_csv("Pracownicy 2.csv")

df2 = pd.DataFrame(csv2)

PLN = []
for el in df2["Zarobki"]:
    PLN.append(float((el[:-4]).replace(' ','')))

df2["PLN"] = PLN
del df2["Zarobki"]

df2["USD"] = df2["PLN"]/3.98


# print(len(df2[df2["USD"]> 2000]))

ZarobkiK = []
for k in df2["Zarobki"]:
    if((df2[df2["Płeć"] == "M"])):
        ZarobkiK.append(float((k[-4]).replace(' ','')))









# zU
# SD = [] 
# for el in df2["Zarobki"]:
#     zUSD.append(f"{(float(el[:-4].replace('',''))*4.5)}")
# df2["ZarobkiUSD"] = zUSD




# print(csv1.to_string())
# print("===============")
# print(csv2.to_string())


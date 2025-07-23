
Luku4 = int(input("Anna kokonaisluku: "))
Luku5 = int(input("Anna kokonaisluku: "))
Luku6 = int(input("Anna kokonaisluku: "))

Luvut = [Luku4, Luku5, Luku6]
Luvut.sort()
Suurin = Luvut[-1]
Toiseksi_suurin = Luvut[-2]
Ero = abs(Suurin - Toiseksi_suurin)
Pituus = len(str(Suurin))

print(f"Suurin luku on: {Suurin}")
print(f"Suurimman ja toiseksi suurimman ero on: {Ero}")
print(f"Suurimman luvun pituus on: {Pituus} merkkiä")
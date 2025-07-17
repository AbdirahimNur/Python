#T1
Ikä = int(input("Nykyinen ikäsi:"))
Tulevaikä = Ikä + 1
print(f"Ensi vuonna olet {Tulevaikä} vuotta vanha.")

#T2
Luku1 = int(input("Anna kokonaisluku:"))
Luku2 = int(input("Anna kokonaisluku:"))
Summa = Luku1 + Luku2
print(f"Lukujen summa on {Summa}")

#T3
Sivu = int(input("Anna sivunpituus:"))
Neliö = Sivu * Sivu
print(f"Neliön pinta-ala on {Neliö}.")

#T4
Celsius = int(input("Anna lämpötila Celsiuksena:"))
F = (Celsius * 9/5) + 32
print(f"Lämpötila on {F} Fahrenheit.")

#T5
Luku3 = int(input("Anna kokonaisluku:"))
Luku4 = int(input("Anna kokonaisluku:"))
Kokoinaisjako = Luku3 // Luku4
Jakojäännös = Luku3 % Luku4
print(Kokoinaisjako)
print(Jakojäännös)

#T6
Luku5 = int(input("Anna kokonaisluku:"))
Luku6 = int(input("Anna kokonaisluku:"))

Summa = Luku5 + Luku6
Erotus = Luku5 - Luku6
Tulo = Luku5 * Luku6
Osamäärä = Luku5 / Luku6

print(f"Tulokset ovat {Summa}, {Erotus}, {Tulo}, {Osamäärä}.")

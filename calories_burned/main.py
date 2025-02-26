from functions import calculate_calories_burned

print("Laipni lūgti Kaloriju Patēriņa Kalkulatorā!")
aktivitate = input("Ievadiet aktivitāti (piem., skriešana, riteņbraukšana, peldēšana): ")
ilgums = float(input("Ievadiet aktivitātes ilgumu minūtēs: "))
svars = float(input("Ievadiet savu svaru kilogramos: "))

sadedzinatas_kalorijas = calculate_calories_burned(aktivitate, ilgums, svars)

if isinstance(sadedzinatas_kalorijas, str):
    print(sadedzinatas_kalorijas)
else:
    print("Jūs esat sadedzinājis kalorijas:", sadedzinatas_kalorijas)

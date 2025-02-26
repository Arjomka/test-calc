from functions import calculate_bmi, interpret_bmi

print("Laipni lūgti ĶMI kalkulatorā!")

svars_kg = float(input("Ievadiet savu svaru kilogramos: "))
augums_m = float(input("Ievadiet savu augumu metros: "))

kmi = calculate_bmi(svars_kg, augums_m)
interpretacija = interpret_bmi(kmi)

print("Jūsu ĶMI ir {:.2f}".format(kmi))
print("Interpretācija: ", interpretacija)
from functions import calculate_monthly_payment

print("Laipni lūgti Hipotēku kalkulatorā!")
amount = float(input("Ievadiet aizdevuma summu: €"))
annual_interest_rate = float(input("Ievadiet gada procentu likmi (piemēram, 5 - 5%): "))
years = int(input("Ievadiet aizdevuma termiņu gados: "))

monthly_payment = calculate_monthly_payment(amount, annual_interest_rate, years)

print("\nJūsu ikmēneša maksājums būs:  €{:.2f}".format(monthly_payment))
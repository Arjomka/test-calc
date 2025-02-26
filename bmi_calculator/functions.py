def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Zems svars"
    elif bmi < 25:
        return "Normāls svars"
    elif bmi < 30:
        return "Liekais svars"
    else:
        return "Aptaukošanās"
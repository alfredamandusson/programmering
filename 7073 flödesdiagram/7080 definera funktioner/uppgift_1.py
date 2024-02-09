# anrop av funktionen print
print("Hello!")
# skriver ut blankrad
print()
# skriver ut: 5 kr
print(5, "kr")


def celsius_to_kelvin(celsius):
    kelvin = celsius + 273
    return kelvin

celsius_user = float(input("ange temp i celsius: "))
print("temp i kelvin: ", celsius_to_kelvin(celsius_user))
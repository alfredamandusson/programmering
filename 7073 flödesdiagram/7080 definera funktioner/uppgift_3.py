def kelvin_to_farenheight(kelvin):
    farenheight = kelvin /(1.8 +32) -273
    return farenheight

kelvin_user = float(input("ange temp i kelvin: "))
print("temp i farenheight: ", kelvin_to_farenheight(kelvin_user))
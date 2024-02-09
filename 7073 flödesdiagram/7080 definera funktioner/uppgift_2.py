def celsius_to_farenheight(celsius):
    # F = C * 1.8 + 32
    # F - 32 = C * 1.8
    # C = (F - 32) / 1.8
    farenheight = celsius *1.8+32
    return farenheight

celsius_user = float(input("ange temp i celsius: "))
print("temp i farenheight: ", celsius_to_farenheight(celsius_user))


def farenheight_to_celsius(farenheight):
    celsius = (farenheight - 32)/ 1.8
    return celsius

farenheight_user = float(input("ange temp i farenheight: "))
print("temp i celsius: ", farenheight_to_celsius(farenheight_user))

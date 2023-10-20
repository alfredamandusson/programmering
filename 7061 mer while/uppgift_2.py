gissningar = 0

tal = int(input("Gissa ett tal: "))
gissningar += 1

while tal != 42:
    if tal < 42:
        print("För litet.")
    else:
        print("För stort.")
    tal = int(input("Gissa igen: "))
    gissningar += 1

print(f"Du behövde {gissningar} gissningar för att hitta rätt svar.")


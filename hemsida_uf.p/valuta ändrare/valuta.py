class Valutavaxlare:
    def __init__(self):
        self.kurser = {
            'SEK': 1.0,
            'USD': 0.09,  
            'EUR': 0.09,  
            'MXN': 1.55
            }

    def konvertera(self, belopp, fran_valuta, till_valuta):
        if fran_valuta != 'SEK':
            belopp = belopp / self.kurser[fran_valuta]
        konverterat_belopp = belopp * self.kurser[till_valuta]
        return konverterat_belopp
valutavaxlare = Valutavaxlare()

belopp = float(input("Ange belopp: "))
fran_valuta = input("Från valuta (SEK, USD, EUR, MXN): ").upper()
till_valuta = input("Till valuta (SEK, USD, EUR, MXN): ").upper()

resultat = valutavaxlare.konvertera(belopp, fran_valuta, till_valuta)
print(f"{belopp} {fran_valuta} är {resultat} {till_valuta}")   

    
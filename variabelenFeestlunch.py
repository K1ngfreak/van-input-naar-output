croissant = 0.39
stokbrood = 2.78
korting = 0.50

aantalCroissant = int(input('Croissant aantal: '))
aantalStokbrook = int(input('Stokbrood aantal: '))
aantalKorting = int(input ('Kortingsbonnen aantal: '))

croissants = float(croissant * aantalCroissant)
stokbroden = float(stokbrood * aantalStokbrook)
kortingen = float(korting * aantalKorting)
receipt = float(croissants + stokbroden - kortingen)

print(str(receipt) + ' euro')
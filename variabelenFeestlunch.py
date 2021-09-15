croissant = 0.39
stokbrood = 2.78
korting = 0.50

aantalCroissant = float(input('Croissant aantal: '))
aantalStokbrook = float(input('Stokbrood aantal: '))
aantalKorting = float(input ('Kortingsbonnen aantal: '))

croissants = croissant * aantalCroissant
stokbroden = stokbrood * aantalStokbrook
kortingen = korting * aantalKorting
receipt = croissants + stokbroden - kortingen

print(str(receipt) + ' euro')
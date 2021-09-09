croissant = 0.39
stokbrood = 2.78
korting = 0.50

aantalCroissant = int(input('Croissant aantal: '))
aantalStokbrook = int(input('Stokbrood aantal: '))
aantalKorting = int(input ('Kortingsbonnen aantal: '))

croissants = croissant * aantalCroissant
stokbroden = stokbrood * aantalStokbrook
kortingen = korting * aantalKorting
receipt = croissants + stokbroden - kortingen

print(receipt)
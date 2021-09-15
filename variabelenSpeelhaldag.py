toegang = 7.45
vijf_minuten = 0.37

aantal = float(input('Aantal personen: '))
aantal_tijd = int(input('Aantal pesonen tijd: '))
lengte = float(input('Tijdsduur: '))


tijdsDuurKoste = lengte/5
toegangKosten = aantal * toegang
tijdskosten =  vijf_minuten * tijdsDuurKoste * aantal_tijd
totaalKosten = tijdskosten + toegangKosten

print(str(totaalKosten) + ' euro')
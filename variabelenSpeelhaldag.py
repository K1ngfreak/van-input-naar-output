toegang = 7.45
vijf_minuten = 0.37

aantal = int(input('Aantal personen: '))
lengte = int(input('Tijdsduur: '))


tijdsDuurKoste = lengte/5
toegangKosten = aantal * toegang
tijdskosten =  vijf_minuten * tijdsDuurKoste
totaalKosten = tijdskosten + toegangKosten

print(totaalKosten)
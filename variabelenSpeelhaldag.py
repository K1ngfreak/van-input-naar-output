toegang = 7.45
vijf_minuten = 0.37

aantal = int(input('Aantal personen: '))
aantal_tijd = int(input('Aantal pesonen VR: '))
lengte = int(input('Tijdsduur: '))

tijdsDuurKoste = float(lengte/5)
toegangKosten = float(aantal * toegang)
vrkosten =  float(vijf_minuten * tijdsDuurKoste * aantal_tijd)
totaalKosten = float(vrkosten + toegangKosten)

print(str(totaalKosten) + ' euro')
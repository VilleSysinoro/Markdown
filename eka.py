# Se ihan ensimmäinen hei maailma -esimekki

print('Hello World!')

print('Ja tämän sovelluksen koodasi Jakke Jäynä')

# ESIMERKKEJÄ MUUTUJIEN KÄYTÖSTÄ
# ==============================

# YKSINKERTAISET MUUTTUJAT
# ------------------------

etunimi = 'Jonne' # Merkkijono string (str)
ika = 16 # Kokonaisluku integer (int)
ytoaineiden_keskiarvo = 2.5 # Liukuluku floating point number (float)
valmistunu = False # Totuusarvo voolean (bool)

print(etunimi, 'sai keskiarvoksi Yto-aineista', ytoaineiden_keskiarvo)
print(etunimi, 'onvalmistunut', valmistunu)

# RAKENTEELLISET MUUTTUJAT
# ------------------------

nimilista = ['Jonne', 'Jasmin', 'Aleksanteri'] # Lista list
print('Listassa ensimmäisenä on', nimilista[0]) # Indeksissä 0 oleva arvo
jasenia = len(nimilista) # Listan jäsenmäärä selviää len-komennolla
print('Nimilistassa on', jasenia, 'henkilöä')
nimilista.sort() # Järjestää listan aakkosjärjestykseen
print('aakkosettu lista on', nimilista)

ryhmat = ('TiVi24A', 'TiVi23b', 'TiVi20oa') # Monikko tupple
print('Meidän ryhmä on', ryhmat[2])
# ryhmat[2] = 'TiVi20ka' # Yksittäistä jäsentä ei voi muuttaa
ryhmat = ('TiVi24A', 'TiVi23b', 'TiVi20ka') # Koko monikon voi muuttaa
print('Meidän uusi ryhmä on', ryhmat[2])

joukko = {'Tuittu', 'Assi', 'Calle'} # Joukko set
print('Ja joukkoon kuuluvat', joukko) # Huomaa järjestys
# print(joukko[2]) ei toimi, koska jäseneen ei voi viitata indeksillä

# Sanakirja dictionary (dict)
henkilotiedot = {'etunimi': 'Jonne', 'sukunimi': 'Janttari', 'ikä': 16}

print('Opiskelijan', henkilotiedot['etunimi'], 'ikä on', henkilotiedot['ikä'])

opiskelija1 = {'etunimi': 'Jonne', 'sukunimi': 'Janttari', 'ikä': 16}
opiskeliaj2 = {'etunimi': 'Iina', 'sukunimi': 'Urpo', 'ikä': 17}
opiskelija3 = {'etunimi': 'Tuittu', 'sukunimi': 'Kiukkunen', 'ikä': 27}

# Lista sanakirjoista -> Taulukko
opiskelijalista = [opiskelija1, opiskeliaj2, opiskelija3]
print('Opiskelija lista on', opiskelijalista)

uusi_opiskelija = {'etunimi': 'Assi', 'sukunimi': 'Kalma', 'ikä': 65}

# Lisätään uusi arvo olemassa olevaan listaan
opiskelijalista.append(uusi_opiskelija)

# Tulostetaan opiskelijalistan ensimmäinen ja viimeinen jäsen
print('Listassa ensimmäinen on', opiskelijalista.pop(0))
print('Ja viimeisenä on', opiskelijalista.pop())
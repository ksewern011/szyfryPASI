def szyfruj_vigenere(tekst, klucz):
    wynik = ""
    klucz = klucz.upper()
    indeks_klucza = 0
    for znak in tekst:
        if znak.isupper():
            przesuniecie = ord(klucz[indeks_klucza % len(klucz)]) - ord('A')
            nowy_znak = chr((ord(znak) - ord('A') + przesuniecie) % 26 + ord('A'))
            wynik += nowy_znak
            indeks_klucza += 1
        else:
            wynik += znak
    return wynik

def deszyfruj_vigenere(tekst, klucz):
    wynik = ""
    klucz = klucz.upper()
    indeks_klucza = 0
    for znak in tekst:
        if znak.isupper():
            przesuniecie = ord(klucz[indeks_klucza % len(klucz)]) - ord('A')
            nowy_znak = chr((ord(znak) - ord('A') - przesuniecie) % 26 + ord('A'))
            wynik += nowy_znak
            indeks_klucza += 1
        else:
            wynik += znak
    return wynik

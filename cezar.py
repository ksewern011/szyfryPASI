def szyfruj_cezar(tekst, klucz):
    zaszyfrowany = ""
    for litera in tekst:
        if litera.isupper():
            nowy_kod = ord(litera) + klucz
            if nowy_kod > ord('Z'):
                nowy_kod -= 26
            elif nowy_kod < ord('A'):
                nowy_kod += 26
            zaszyfrowany += chr(nowy_kod)
        else:
            zaszyfrowany += litera
    return zaszyfrowany

def deszyfruj_cezar(tekst, klucz):
    return szyfruj_cezar(tekst, -klucz)
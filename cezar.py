def szyfrcezar(tekst, klucz):
    zaszyfrowany = ""
    klucz = klucz % 26 
    
    for litera in tekst:
        if litera.isupper():
            nowy_kod = ord(litera) + klucz
            if nowy_kod > ord('Z'):
                nowy_kod -= 26
            zaszyfrowany += chr(nowy_kod)
        elif litera.islower():
            nowy_kod = ord(litera) + klucz
            if nowy_kod > ord('z'):
                nowy_kod -= 26
            zaszyfrowany += chr(nowy_kod)
        else:
            zaszyfrowany += litera
    return zaszyfrowany

def deszyfruj_cezar(tekst, klucz):
    
    return szyfrcezar(tekst, -klucz)

from cezar import szyfruj_cezar, deszyfruj_cezar


def main():
    tekst = "Szyfrcezara"
    klucz = 3
    zaszyfrowany = szyfruj_cezar(tekst, klucz)
    odszyfrowany = deszyfruj_cezar(zaszyfrowany, klucz)

    print(f"Tekst oryginalny: {tekst}")
    print(f"Zaszyfrowany: {zaszyfrowany}")
    print(f"Odszyfrowany: {odszyfrowany}")


if __name__ == "__main__":
    main()
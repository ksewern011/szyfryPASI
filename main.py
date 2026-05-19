from vigenere import szyfruj_vigenere


def main():
    # Dane do testu
    tekst = "TAJNAWIADOMOSC"
    klucz = "KLUCZ"

    # Wywołanie funkcji z pliku vigenere.py
    zaszyfrowany = szyfruj_vigenere(tekst, klucz)

    print("--- TEST SZYFRU VIGENERE'A ---")
    print(f"Tekst jawny: {tekst}")
    print(f"Klucz: {klucz}")
    print(f"Zaszyfrowany: {zaszyfrowany}")


if __name__ == "__main__":
    main()
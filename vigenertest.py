def uruchom_testy_vigenere():
    print("Rozpoczęcie testów poprawności szyfru Vigenère'a...\n")
    
   przypadki_testowe = [
        ("ATTACKATDAWN", "LEMON", "LXFOPVEOFNHR"),  
        ("KRYPTOGRAFIA", "A", "KRYPTOGRAFIA"),     
        ("A B C", "B", "B C D"),                    
        ("TO JEST TAJNY TEKST", "KOD", "DS XSTW hoxbm hshgh")]
    
    przypadki_testowe[3] = ("TO JEST TAJNY TEKST", "KOD", "DS XSTW TAJNY TEKST")
     bledy = 0
    
    for i, (jawny, klucz, oczekiwany) in enumerate(przypadki_testowe, 1):
        wynik_szyfrowania = szyfruj_vigenere(jawny, klucz)
        wynik_deszyfrowania = deszyfruj_vigenere(wynik_szyfrowania, klucz)
        
        print(f"Test {i}: Tekst: '{jawny}', Klucz: '{klucz}'")
        
        warunek_szyfru = (wynik_szyfrowania == oczekiwany)
        warunek_odszyfrowania = (wynik_deszyfrowania == jawny)
        
        if warunek_szyfru and warunek_odszyfrowania:
            print(f"  -> status: OK (Zaszyfrowany: '{wynik_szyfrowania}')")
        else:
            print(f"  -> status: BŁĄD!")
            if not warunek_szyfru:
                print(f"     Oczekiwano szyfru: '{oczekiwany}', a otrzymano: '{wynik_szyfrowania}'")
            if not warunek_odszyfrowania:
                print(f"     Błąd deszyfrowania! Otrzymano: '{wynik_deszyfrowania}' zamiast: '{jawny}'")
            bledy += 1
            
          print("-" * 50)
    if bledy == 0:
        print("Wszystkie testy zakończone SUKCESEM! Algorytm działa prawidłowo.")
    else:
        print(f"Znaleziono błędy w {bledy} przypadkach.")


uruchom_testy_vigenere()

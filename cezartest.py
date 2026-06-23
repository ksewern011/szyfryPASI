def uruchom_testy():
    print("Rozpoczęcie testów poprawności...\n")
    przypadki_testowe = [
        ("ABC", 3, "DEF"),         
        ("XYZ", 3, "ABC"),         
        ("A B C", 1, "B C D"),     
        ("TEST", 26, "TEST"),       
        ("TEST", 0, "TEST"),        
        ("NieSzyfrujMnie123", 5, "SnjXdevjtsMs123")]
    
    bledy = 0
    for i, (jawny, klucz, oczekiwany) in enumerate(przypadki_testowe, 1):
       wynik_szyfrowania = szyfrcezar(jawny, klucz)
       wynik_deszyfrowania = deszyfruj_cezar(wynik_szyfrowania, klucz)
        print(f"Test {i}: Tekst: '{jawny}', Klucz: {klucz}")
        
        if wynik_szyfrowania == oczekiwany and wynik_deszyfrowania == jawny:
            print(f"  -> status: OK (Zaszyfrowany: '{wynik_szyfrowania}')")
        else:
            print(f"  -> status: BŁĄD!")
            print(f"     Oczekiwano szyfru: '{oczekiwany}', a otrzymano: '{wynik_szyfrowania}'")
            print(f"     Po deszyfrowaniu otrzymano: '{wynik_deszyfrowania}'")
            bledy += 1
    
    print("-" * 30)
    if bledy == 0:
        print("Wszystkie testy zakończone SUKCESEM! Kod działa poprawnie.")
    else:
        print(f"Znaleziono błędy w {bledy} przypadkach.")

uruchom_testy()

kolorRED = '\033[91m'
koniec_koloru = CEND = '\033[0m'

def wyswietl_menu():
    print("---------------------------------------------------------------------------------------------".center(70))
    print(kolorRED,"1. Wyświetl aktualny rejestr  2. Dodaj do rejestru  3. Usuń z rejestru  0. Wyjście z programu".center(70),koniec_koloru)

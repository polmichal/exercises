import sqlite3
import time
import menu
from time import *
import pandas as pd
from tabulate import tabulate
#import os
#import subprocess

print('---------------------------------------------------------------------------------------------'.center(70))
print('PROGRAM REJESTR VER 1.0'.center(90))
print('---------------------------------------------------------------------------------------------'.center(70))

try:
    db = sqlite3.connect('baza.db')
    cursor = db.cursor()
    print('Połączenie z bazą danych - OK')
    print('')
    #time.sleep(2)
except sqlite3.Error:
    print("Nie można połączyć z bazą danych, baza.db")
    print('Plik "baza.db" powinien znajdować się w folderze głównym programu.')
    time.sleep(3)
    print('Koniec programu')

def clear():
    print('\n' * 70)
    #c = lambda: os.system('clear') or None
    #c()
    #subprocess.call("clear", shell=True)

def stworz_tabele():
    # Create table
    cursor.execute('''CREATE TABLE rejestr (numer text,  nazwa text, godzina text, data text)''')
    db.commit()
    db.close()
#Tabela juz stworzona

def wyswietl_wszystko():
    cursor.execute('''SELECT * FROM rejestr ORDER BY numer DESC''')
    all_rows = cursor.fetchall()
    for row in all_rows:
        print(row)
    #db.close()

def wyswietl_wszystko_pandas():
    print('PROGRAM REJESTR VER 1.0')
    df = pd.read_sql("SELECT * from rejestr ", db)
    print(tabulate(df, headers='keys', tablefmt='psql'))

def ostatni_wiersz():
    cursor.execute('''SELECT * FROM rejestr ORDER BY godzina DESC LIMIT 1''')
    all_rows = cursor.fetchall()
    for row in all_rows:
        ostatni = row[0]
    return ostatni


def dodaj_wpis(nazwa):
    #print('Ostatni numer to', ostatni_wiersz())
    no = input('Podaj numer wpisu: (ostatni numer to {})'.format(ostatni_wiersz()))
    clear()
    data = strftime("%Y-%m-%d")
    godzina = strftime("%H:%M")
    cursor.execute('''
        INSERT INTO rejestr (numer,  nazwa, godzina, data ) VALUES(?,?,?,?)''',
                   (no, nazwa, godzina, data))
    print('Wpis', nazwa, 'został dodany')
    print('-----------------------------------------------')
    print('')
    #time.sleep(1)
    db.commit()
    #db.close()
def usun_wpis(numer):
    no = numer
    cursor.execute('''
            DELETE FROM rejestr WHERE numer = ?''', (numer,))

    db.commit()
    #db.close()



while True:

    menu.wyswietl_menu()
    wybor = input()
    if wybor =='1':
        clear()
        wyswietl_wszystko_pandas()
    if wybor =='2':
        clear()
        print('Podaj nazwę wpisu:')
        nazwa = input()
        dodaj_wpis(nazwa)
        wyswietl_wszystko_pandas()
    if wybor =='3':
        clear()
        print('Podaj numer wpisu do usunięcia:')
        nazwa = input()
        usun_wpis(nazwa)
        print('Usunięto ',nazwa)
        print('-----------------------------------------------')
        print('')
    if wybor =='0':
        #clear()
        print('Czy na pewno chcesz zamknąć program? t/n')
        zakoncz = input()
        if zakoncz =='t':
            db.close()
            break
        if zakoncz =='n':
            clear()
            #menu.wyswietl_menu()



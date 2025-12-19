from funktsioonid import *

while True:
    print("""
--- MENÜÜ ---
1 - Arithmetica
2 - Is year leap
3 - Square
4 - Season
5 - Bank
6 - Prime check
7 - Date check
8 - XOR cipher
9 - Average
10 - Min and Max
11 - Unique elements
0 - Exit
""")
    valik = input("Tee valik: ")

    if valik == "1":
        print("Tulemus:", arithmetic())

    elif valik == "2":
        year = int(input("Sisesta aasta: "))
        print(is_year_leap(year))

    elif valik == "3":
        side = float(input("Sisesta külje pikkus: "))
        perimeter, area, diagonal = square(side)
        print(f"Perimeeter: {perimeter}, Pindala: {area}, Diagonaal: {diagonal}")

    elif valik == "4":
        month = int(input("Sisesta kuu number: "))
        print(season(month))

    elif valik == "5":
        amount = float(input("Sisesta summa: "))
        years = int(input("Sisesta aastate arv: "))
        print(bank(amount, years))

    elif valik == "6":
        n = int(input("Sisesta arv (0-1000): "))
        if is_prime(n):
            print(f"{n} on algarv")
        else:
            print(f"{n} ei ole algarv")

    elif valik == "7":
        day = int(input("Sisesta päev: "))
        month = int(input("Sisesta kuu: "))
        year = int(input("Sisesta aasta: "))
        if date(day, month, year):
            print("Kuupäev on korrektne")
        else:
            print("Kuupäev ei ole korrektne")

    elif valik == "8":
        text = input("Sisesta sõne: ")
        key = input("Sisesta võti (üks tähemärk): ")
        ciphered = XOR_cipher(text, key)
        print("Krüpteeritud:", ciphered)
        print("Dekrüpteeritud:", XOR_uncipher(ciphered, key))

    elif valik == "9":
        numbers = input("Sisesta arvud eraldatult tühikuga: ").split()
        numbers = [float(num) for num in numbers]
        print("Keskmine:", average(numbers))

    elif valik == "10":
        numbers = input("Sisesta arvud eraldatult tühikuga: ").split()
        numbers = [float(num) for num in numbers]
        min_val, max_val = min_max(numbers)
        print(f"Väikseim: {min_val}, Suurim: {max_val}")

    elif valik == "11":
        lst = input("Sisesta elemendid eraldatult tühikuga: ").split()
        print("Ainulaadsed elemendid:", unique_elements(lst))

    elif valik == "0":
        print("Programmi lõpetamine...")
        break
    else:
        print("Vale valik!")

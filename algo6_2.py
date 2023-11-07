print("@@@ @  @@@ @@@@   @   @ @ @@@@@@     @@@")
print("@ @ @ @  @ @   @  @   @ @ @     @   @   @")
print("@ @ @ @@@@ @  @   @@@@@ @ @@@@@@    @@@@@")
print("@ @@@ @  @ @@     @   @ @ @    @    @   @")


import math

def luas_permukaan_kubus(sisi):
    return 6 * sisi**2

def luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

def luas_permukaan_tabung(jari_jari, tinggi):
    luas_selimut = 2 * math.pi * jari_jari * tinggi
    luas_dasar = math.pi * jari_jari**2
    return luas_selimut + 2 * luas_dasar

def luas_permukaan_kerucut(jari_jari, tinggi):
    s = math.sqrt(jari_jari**2 + tinggi**2)
    luas_selimut = math.pi * jari_jari * s
    luas_dasar = math.pi * jari_jari**2
    return luas_selimut + luas_dasar

def luas_permukaan_bola(jari_jari):
    return 4 * math.pi * jari_jari**2

while True:
    print("---KALKULATOR LUAS---")
    print("1. kubus")
    print("2. balok")
    print("3. tabung")
    print("4. kerucut")
    print("5. bola")
    print("6. Keluar")

    bentuk = input("Pilih bentuk bangun ruang (1, 2, 3, 4, 5, 6): ")

    if bentuk == "6":
        print(f"---TERIMA KASIH---")
        break

    if bentuk in ("1", "2", "3", "4", "5"):
        if bentuk == "1":
            sisi = float(input("Masukkan panjang sisi kubus: "))
            luas = luas_permukaan_kubus(sisi)
        elif bentuk == "2":
            panjang = float(input("Masukkan panjang balok: "))
            lebar = float(input("Masukkan lebar balok: "))
            tinggi = float(input("Masukkan tinggi balok: "))
            luas = luas_permukaan_balok(panjang, lebar, tinggi)
        elif bentuk == "3":
            jari_jari = float(input("Masukkan jari-jari tabung: "))
            tinggi = float(input("Masukkan tinggi tabung: "))
            luas = luas_permukaan_tabung(jari_jari, tinggi)
        elif bentuk == "4":
            jari_jari = float(input("Masukkan jari-jari kerucut: "))
            tinggi = float(input("Masukkan tinggi kerucut: "))
            luas = luas_permukaan_kerucut(jari_jari, tinggi)
        elif bentuk == "5":
            jari_jari = float(input("Masukkan jari-jari bola: "))
            luas = luas_permukaan_bola(jari_jari)

        print(f"Luas permukaan {bentuk} adalah {luas}")
    else:
        print("Bentuk bangun ruang tidak valid.")


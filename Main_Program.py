# PROGRAM NGUNTUNK
# BY ALIF DIO AF'ALLY
# Main_Program.py 

import Fungsi_Keliling
import Fungsi_Luas

def hitung_luas_keliling(bangun_datar, opsi):
    if bangun_datar == 1:
        sisi = int(input("sisi-nya? : "))
        if opsi == "L":
            Fungsi_Luas.Luas_Persegi(sisi)
        elif opsi == "K":
            Fungsi_Keliling.Kel_persegi(sisi)

    elif bangun_datar == 2:
        panjang = int(input("Panjang-nya? : "))
        lebar = int(input("Lebar-nya? : "))
        if opsi == "L":
            Fungsi_Luas.Luas_Persegi_Panjang(panjang, lebar)
        elif opsi == "K":
            Fungsi_Keliling.Kel_Persegi_Panjang(panjang, lebar)

    elif bangun_datar == 3:
        alas = int(input("Alas-nya? : "))
        tinggi = int(input("Tinggi-nya? : "))
        if opsi == "L":
            Fungsi_Luas.Segitiga(alas, tinggi)
        elif opsi == "K":
            Fungsi_Keliling.Kel_Segitiga(alas, tinggi)

    elif bangun_datar == 4:
        sisi1 = int(input("Sisi sejajar 1? : "))
        sisi2 = int(input("Sisi sejajar 2? : "))
        if opsi == "L":
            tinggi = int(input("Berapa tinggi-nya? : "))
            Fungsi_Luas.Luas_Trapesium(sisi1, sisi2, tinggi)
        elif opsi == "K":
            sisi3 = int(input("Sisi sejajar 3? : "))
            sisi4 = int(input("Sisi sejajar 4? : "))
            Fungsi_Keliling.Kel_Trapesium(sisi1, sisi2, sisi3, sisi4)

    elif bangun_datar == 5:
        if opsi == "L":
            Diagonal1 = int(input("Masukan besaran Diagonal 1 : "))
            Diagonal2 = int(input("Masukan besaran Diagonal 2 : "))
            Fungsi_Luas.Luas_Layang_layang(Diagonal1, Diagonal2)
        elif opsi == "K":
            sisi1 = int(input("Masukan besaran Sisi 1 : "))
            sisi2 = int(input("Masukan besaran Sisi 2 : "))
            Fungsi_Keliling.Kel_Layang_layang(sisi1, sisi2)

    elif bangun_datar == 6:
        r = int(input("Masukan besaran jari-jari lingkaran anda : "))
        if opsi == "L":
            Fungsi_Luas.Luas_Lingkaran(r)
        elif opsi == "K":
            Fungsi_Keliling.Kel_Lingkaran(r)
    else:
        print("Pilihan bangun datar tidak valid.")

loop = "ya"

while loop == "ya":
    print(
        "+------------------------------------------------------------+\n"
        "Selamat Datang di Program NgunTunk\n"
        "+------------------------------------------------------------+\n"
        "Silahkan Pilih bangun datar yang hendak dihitung\n"
        "1. --> persegi\n"
        "2. --> persegi panjang\n"
        "3. --> segitiga\n"
        "4. --> Trapesium\n"
        "5. --> Layang-layang\n"
        "6. --> Lingkaran\n"
        "+------------------------------------------------------------+"
        " "
    )
    
    try:
        bangun_datar = int(input("Bangun apa yang ingin anda ukur? : "))
        print("+------------------------------------------------------------+")
        opsi = input("Keliling / Luas? : (L/K) ").upper()
        print("+------------------------------------------------------------+")

        hitung_luas_keliling(bangun_datar, opsi)
    except ValueError:
        print("Input tidak valid. Silahkan coba lagi.")

    print("+------------------------------------------------------------+")
    
    loop = input("Apakah anda masih ingin melakukan penghitungan lagi? (ya/tidak) : ").lower()
    if loop == "tidak":
        print("Terima kasih Sudah Menggunakan Aplikasi Ini!")
        print()

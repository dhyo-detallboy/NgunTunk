# PROGRAM NGUNTUNK
# BY ALIF DIO AF'ALLY
# Fungsi_Keliling.py 

import math

# Fungsi Keliling Persegi
def Kel_persegi(sisi):
    keliling = 4 * sisi
    print(keliling)

# Fungsi Keliling Persegi Panjang
def Kel_Persegi_Panjang(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    print(keliling)

# Fungsi Keliling Segitiga
def Kel_Segitiga(alas, tinggi):
    sisi_miring =  math.sqrt(alas**2 + tinggi**2)
    keliling = alas + tinggi + sisi_miring
    print(keliling)

# Fungsi Keliling Trapesium
def Kel_Trapesium(sisi1, sisi2, sisi3, sisi4):
    keliling = sisi1 + sisi2 + sisi3 + sisi4
    print("Keliling Trapesium:", keliling)

# Fungsi Keliling Layang-layang
def Kel_Layang_layang(sisi1, sisi2):
    keliling = 2 * (sisi1 + sisi2)
    print("Keliling Layang-layang:", keliling)

# Fungsi Keliling Lingkaran
def Kel_Lingkaran(r):
    phi1 = 22/7
    phi2 = 3.14

    if r % 7 == 0:
        keliling = 2 * phi1 * r
    else:
        keliling = 2 * phi2 * r
    print("Keliling Lingkaran:", keliling)
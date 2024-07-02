# PROGRAM NGUNTUNK
# BY ALIF DIO AF'ALLY
# Fungsi_Luas.py 

# Fungsi Luas Persegi
def Luas_Persegi(sisi):
    luas = sisi**2
    print(luas)

# Fungsi Luas Persegi Panjang
def Luas_Persegi_Panjang(panjang, lebar):
    luas = panjang * lebar
    print(luas)

# Fungsi Luas Segitiga
def Luas_Segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print(luas)

# Fungsi Luas Trapesium
def Luas_Trapesium(sisi1,sisi2,tinggi):
    luas = (sisi1 + sisi2)* tinggi / 2
    print(luas)

# Fungsi Luas Layang-layang
def Luas_Layang_layang(Diagonal1, Diagonal2):
    luas = (Diagonal1 * Diagonal2)/2
    print(luas)

# Fungsi Luas Lingkaran
def Luas_Lingkaran(r):
    phi1 = 22/7
    phi2 = 3.14

    if r % 7 == 0:
        luas = (phi1 * r**2)
        print(luas)
    else :
        luas = (phi2 * r**2)
        print(luas)


    

sayı = int(input("1.SAYIYI GİRİNİZ : "))
sayı2 = int(input("2.SAYIYI GİRİNİZ : "))
değer_al = int(input("""Toplama için : 1
Çıkarma için : 2
Çarpma için  : 3
Bölme        : 4
TUŞLAYINIZ = """))

if değer_al == 1:
    print("TOPLAMA SONUCU :" , sayı + sayı2)
elif değer_al == 2:
    print("ÇIKARMA SONUCU :" , sayı - sayı2)
elif değer_al == 3:
    print("ÇARPMA SONUCU :" , sayı * sayı2)
elif değer_al == 4:
    print("BÖLME SONUCU :" , sayı / sayı2)
else:
    exit()
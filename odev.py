hobiler = {}
hobiler["Ayşe"] = "Resim yapmak"
hobiler["Berk"] = "Bisiklete binmek"
hobiler["Ceren"] = "Kitap okumak"
hobiler["Emre"] = "Müzik dinlemek"
hobiler["Gökhan"] = "Futbol oynamak"


# İsimleri ve tahmin edilen hobileri yazdırma
print("Sınıf arkadaşlarının isimleri ve tahmin edilen hobileri:")
for isim, hobi in hobiler.items():
    print(isim, hobi)





kelime = "adana"
harf_sayilari = {}

for harf in kelime:
    harf_sayilari[harf] = kelime.count(harf)
    
print(kelime.count('a'))    

print("Kelimenin harfleri ve tekrarlanma sayıları:")
print(harf_sayilari)
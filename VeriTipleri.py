a = 5  # int
b = 3.5  # float
c = "Baki"  # str
d = True  # bool
print(a+b)  # float ve integer veri tipleri işleme alınabilir
# print(a+c) kodu hata verir çünkü int ve str veri tipi dönüşümü yapılmadan toplanamaz
print(b-d)  # bool veri tipi int ve float ile işleme alınabiliyor True=1(d=1) ve False=0
# print(c+d) kodu hata verir çünkü str ile bool veri tipi dönüşümü yapılmadan toplanamaz
# Veri Tipi Dönüşümü Yaparak İşleme Alma
print(str(a)+c)  # 5Baki olarak sonuç verir 5 sayısı str tipine dönüştü
# print(a+int(c)) kodu hata verir çünkü c değeri "Baki" 10'luk tabanda bir sayıya dönüşemez.
print(bool(c)+d)  # 2() sonucunu verir çünkü "Baki" ifadesi bool tipinde aksi belirtilmedikçe True değeri alır.
print(c+str(d))  # BakiTrue sonucunu verir çünkü True değeri str tipine dönüştürüldü.
# yukarıdaki dönüşümler işlem içerisinde kullanılmak için yapılmış olup verilerin türleri hala ilk belirlendiği gibidir
print(type(a))
print(type(b))
print(type(c))
print(type(d))
# değeri sürekli olarak farklı türde kullanmak için yeni bir değişkene atayabiliriz
e = str(d)  # e değişkenine atanmış str tipinde bir True değeri
print(e)  # True sonucunu verir veri tipi ise str dir
print(type(e))  # <class 'str'>
print(e+c)  # TrueBaki sonucunu verir, dikkat>iki veri tipide str olduğu için print(c+d) deki gibi hata vermemiştir

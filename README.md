
## Password Generator

Merhaba! Bu projede iki tür şifre oluşturucu bulunmaktadır. Birinde kullanıcıya soru sorularak ve kullanıcıdan input alınarak şifre oluşturulmaktadır. Diğerinde ise şifre oluşturmak için komut satırındaki argümanlar kullanılmaktadır.

 - Python Version: 3.11

## Komut Satırı Kullanımı

Açıklayıcı:

	$ python password-generator -h

Çıktı:

    Şifre oluşturucu
    
    positional arguments:
      uzunluk          Karakter Uzunluğu
    
    options:
      -h, --help       show this help message and exit
      -b, --buyukharf  Büyük harf içermesi için
      -k, --kucukharf  Küçük Harf içermesi için
      -r, --rakam      Rakam içermesi için
      -s, --sembol     Sembol içermesi için

Basit Kullanım:

> 	Argüman girilmezse varsayılan değerler kullanılarak şifre oluşturulur

    $ python password-generator.py

Çıktı:

    Oluşturulan Şifre: 1mSmuH%B
    Oluşturulan şifreyi kaydetmek ister misiniz? (E/H) - E
    Şifre Başarıyla C:\Users\username\Desktop\password-generator.txt dizinine kaydedilmiştir.

Detaylı Kullanım:

> Şifre uzunluğu ve kullanılmak istenen karakterler seçilir

    $ python password-generator.py 20 -bkrs

Çıktı:

    Oluşturulan Şifre: N}v@~"<a8#(n/^i`X(0!
    Oluşturulan şifreyi kaydetmek ister misiniz? (E/H) - E
    Şifre Başarıyla C:\Users\username\Desktop\password-generator.txt dizinine kaydedilmiştir.

Detaylı Kullanım:

> Detaylı kullanıma bir diğer örnek

    $ python password-generator.py 12 -bks

Çıktı:

    Oluşturulan Şifre: s\WQ*^wTgRGK
    Oluşturulan şifreyi kaydetmek ister misiniz? (E/H) - E
    Şifre Başarıyla C:\Users\username\Desktop\password-generator.txt dizinine kaydedilmiştir.

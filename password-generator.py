import random
import string
import os
import argparse


def generate_password(uzunluk, buyukHarf, kucukHarf, rakam, sembol):

    karakterler = ''

    if buyukHarf:
        karakterler += string.ascii_uppercase
    if kucukHarf:
        karakterler += string.ascii_lowercase
    if rakam:
        karakterler += string.digits
    if sembol:
        karakterler += string.punctuation

    if buyukHarf==False and kucukHarf==False and rakam==False and sembol==False:
        karakterler += string.ascii_uppercase
        karakterler += string.ascii_lowercase
        karakterler += string.digits
        karakterler += string.punctuation

    sifre = ''

    for _ in range(uzunluk):
        randomSayi = random.randint(1, len(karakterler)-1)
        sifre += karakterler[randomSayi]

    return sifre


parser = argparse.ArgumentParser(description='Şifre oluşturucu')
parser.add_argument('uzunluk', type=int, nargs='?', default=8, help='Karakter Uzunluğu')
parser.add_argument('-b', '--buyukharf', action='store_true', help='Büyük harf içermesi için')
parser.add_argument('-k', '--kucukharf', action='store_true', help='Küçük Harf içermesi için')
parser.add_argument('-r', '--rakam', action='store_true', help='Rakam içermesi için')
parser.add_argument('-s', '--sembol', action='store_true', help='Sembol içermesi için')

argumanlar = parser.parse_args()


sifre = generate_password(argumanlar.uzunluk, argumanlar.buyukharf, argumanlar.kucukharf, argumanlar.rakam, argumanlar.sembol)
print("[->] Oluşturulan Şifre: "+sifre)


kayit = input("[*] Oluşturulan şifreyi kaydetmek ister misiniz? (E/H) - ")

if kayit.upper() == 'E':
    directory = "C:\\Users\\"+os.getlogin()+"\\Desktop\\password-generator.txt"
    sifreKayit = open(directory,"a")
    metin = "Oluşturulan Şifre: "+sifre+"\n"
    sifreKayit.write(metin)
    sifreKayit.close()
    print("[->] Şifre Başarıyla",directory,"dizinine kaydedilmiştir.")

elif kayit.upper() != 'E' and kayit.upper() != 'H':
    print("[!] Geçersiz Giriş!")

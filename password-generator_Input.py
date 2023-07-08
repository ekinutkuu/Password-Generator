import random
import string
import os


print('''

██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░

░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

''')

uzunluk = int(input("[*] Şifre uzunluğunu giriniz: "))

karakterler = "";

buyukHarf = input("[*] Büyük harf kullanılsın mı? (E/H) - ")
kucukHarf = input("[*] Küçük harf kullanılsın mı? (E/H) - ")
rakam = input("[*] Rakam  kullanılsın mı? (E/H) - ")
sembol = input("[*] Sembol kullanılsın mı? (E/H) - ")


if buyukHarf.upper() == 'E':
    karakterler += string.ascii_uppercase

if kucukHarf.upper() == 'E':
    karakterler += string.ascii_lowercase

if rakam.upper() == 'E':
    karakterler += string.digits
    
if sembol.upper() == 'E':
    karakterler += string.punctuation

sifre = ''

for _ in range(uzunluk):
    randomSayi = random.randint(1, len(karakterler)-1)
    sifre += karakterler[randomSayi]

print("[->] Oluşturulan Şifre:",sifre)

kayit = input("[*] Şifreyi kaydetmek ister misiniz? (E/H) - ")

if kayit.upper() == 'E':
    directory = "C:\\Users\\"+os.getlogin()+"\\Desktop\\password-generator.txt"
    sifreKayit = open(directory,"a")
    metin = "Oluşturulan Şifre: "+sifre+"\n"
    sifreKayit.write(metin)
    sifreKayit.close()
    print("[->] Şifre Başarıyla",directory,"dizinine kaydedilmiştir.")

elif kayit.upper() != 'E' and kayit.upper() != 'H':
    print("[!] Geçersiz Giriş!")

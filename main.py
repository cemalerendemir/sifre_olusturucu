import random

karakterler = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

count = int(input("Kaç karakterli bir şifre istiyorsun?"))

sifre = ""

for i in range(count):

    sifre += random.choice(karakterler)

print(sifre)
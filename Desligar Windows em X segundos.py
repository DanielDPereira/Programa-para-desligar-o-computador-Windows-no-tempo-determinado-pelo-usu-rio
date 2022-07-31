import os

t = str(input("Gostaria de desligar o seu pc em quantos segundos? "))

os.system("shutdown /s /t "+t)

print("O seu computador será desligado em "+t+" segundos")
input()

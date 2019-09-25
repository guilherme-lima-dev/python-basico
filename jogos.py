import forca
import adivinhacao

print("=+=+=+==+=+=+==+=+=+==+=+=")
print("Qual jogo você quer jogar?")
print("=+=+=+==+=+=+==+=+=+==+=+=")

print("[1]Forca [2]Adivinhação")

jogo = int(input("Escolha o jogo: "))

if(jogo == 1):
    forca.jogar()
elif(jogo == 2):
    adivinhacao.jogar()

import desenho
import random
import os
from unicodedata import normalize

def jogar():
    print("=+=+=+==+=+=+==+=+=+==+=+=+")
    print("Bem vindo ao jogo da Forca!")
    print("=+=+=+==+=+=+==+=+=+==+=+=+")

    print("\n Escolha a modalidade da forca: ")
    modalidade = int(input("[1]Frutas [2]Partes corpo \n"))
    if(modalidade == 1):
        palavra_secreta = carrega_palavra_secreta("frutas.txt")
    elif(modalidade == 2):
        palavra_secreta = carrega_palavra_secreta("pch.txt")

    print("###################################")
    print("# OBS: desconsidere acentos e 'Ç' #")
    print("###################################")

    palavra_secreta = remover_acentos(palavra_secreta)
    lista_palavra = ["_" for letra in palavra_secreta]
    palavra_jogador = palavra_secreta
    enforcou = False
    acertou = False
    j = 0
    erros = 0
    print(lista_palavra)
    while(not enforcou and not acertou):
        chute = input("Escolha uma letra: ")
        chute = chute.strip().upper()
        i = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute == letra):
                    lista_palavra[i] = chute

                i += 1
        else:
            erros += 1

            os.system('cls' if os.name == 'nt' else 'clear')
        desenho.forca(erros)
        print(lista_palavra)
        enforcou = erros == 6
        acertou = "_" not in lista_palavra

    if(acertou == True):
        desenho.venceu()
    elif(enforcou == True):
        desenho.perdeu(palavra_secreta)

def carrega_palavra_secreta(modalidade):
    arquivo = open(modalidade, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


if(__name__ == "__main__"):
    jogar()

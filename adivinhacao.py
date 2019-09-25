import random
def jogar():
    print("=+=+=+==+=+=+==+=+=+==+=+=+==+=+=")
    print("Bem vindo ao jogo de adivinhação!")
    print("=+=+=+==+=+=+==+=+=+==+=+=+==+=+=")

    numero_secreto = random.randrange(1,101)

    pontos = 1000

    print("Qual o nivel de dificuldade?\n")
    print("[1]Fácil [2]Médio [3]Difícil\n")
    nivel = int(input("Digite o nível: "))

    while(nivel < 1 or nivel > 3):
        print("Esse nível não existe!!")
        nivel = int(input("Digite o nível: "))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1,tentativas+1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute = int(input("Digite seu chute: "))
        if(chute < 1 or chute > 100):
            print("SEU ASNO, pedi um numero entre 1 e 100!!")
            continue
        if(chute == numero_secreto):
            print("Parabéns, você acertou!!")
            break
        elif(chute > numero_secreto):
            print("Você errou!")
            print("O numero é menor que {}".format(chute))
            pontos_perdidos = chute - numero_secreto
            pontos = pontos - pontos_perdidos
        elif(chute < numero_secreto):
            print("Você errou!")
            print("O numero é maior que {}".format(chute))
            pontos_perdidos = numero_secreto - chute
            pontos = pontos - pontos_perdidos

    print("FIM DO JOGO!!!")
    print("Sua pontuação foi: {}".format(pontos))

if(__name__ == "__main__"):
    jogar()

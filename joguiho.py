import random
numero_secreto= random.randint(1,100)
tentativas=0
print("Bem-vindo ao jogo de adivinhação!")
print(' Eu pensei em um numero de 1 a 100. Tente adivinhar')
while True:
    palpite=int(input('digite seu palpite: '))
    tentativas=tentativas +1
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break
    elif palpite > numero_secreto:
        print(f"Seu palpite é muito alto. Tente novamente.")
    else:
        print(f"O numero é menor. Tente novamente.")
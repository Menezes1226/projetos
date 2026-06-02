import random
presidentes = [
    "Bolsonaro",
    "Lula",
    "Dilma",
    "FLAVIO"
    'Davi menezes'
]
presidente_secreto = random.choice(presidentes)
tentativas = 0
print("Bem-vindo ao jogo da adivinhação de presidentes!")
print("Eu pensei em um presidente brasileiro. Tente adivinhar!")
while True:
    palpite = input('digite seu palpite:')
    tentativas = tentativas + 1
    if palpite == presidente_secreto:
        print(f'parabens! Você acertou o presidente em {tentativas} tentativas.')
        break
    else:
        print(f"voce errou tente novamente.")
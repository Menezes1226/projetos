import turtle
import time
import random

# Configuração da tela
tela = turtle.Screen()
tela.title("Jogo da Cobrinha")
tela.bgcolor("black")
tela.setup(width=600, height=600)
tela.tracer(0)

# Cabeça da cobra
cabeca = turtle.Turtle()
cabeca.speed(0)
cabeca.shape("square")
cabeca.color("green")
cabeca.penup()
cabeca.goto(0, 0)
cabeca.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(100, 100)

# Corpo da cobra
segmentos = []

# Pontuação
pontos = 0

# Texto da pontuação
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Pontos: 0", align="center", font=("Arial", 24, "normal"))

# Funções de movimento
def cima():
    if cabeca.direction != "down":
        cabeca.direction = "up"

def baixo():
    if cabeca.direction != "up":
        cabeca.direction = "down"

def esquerda():
    if cabeca.direction != "right":
        cabeca.direction = "left"

def direita():
    if cabeca.direction != "left":
        cabeca.direction = "right"

def mover():
    if cabeca.direction == "up":
        y = cabeca.ycor()
        cabeca.sety(y + 20)

    if cabeca.direction == "down":
        y = cabeca.ycor()
        cabeca.sety(y - 20)

    if cabeca.direction == "left":
        x = cabeca.xcor()
        cabeca.setx(x - 20)

    if cabeca.direction == "right":
        x = cabeca.xcor()
        cabeca.setx(x + 20)

# Teclas
tela.listen()
tela.onkeypress(cima, "w")
tela.onkeypress(baixo, "s")
tela.onkeypress(esquerda, "a")
tela.onkeypress(direita, "d")

# Loop principal
while True:
    tela.update()

    # Colisão com a parede
    if (
        cabeca.xcor() > 290 or
        cabeca.xcor() < -290 or
        cabeca.ycor() > 290 or
        cabeca.ycor() < -290
    ):
        time.sleep(1)
        cabeca.goto(0, 0)
        cabeca.direction = "stop"

        for segmento in segmentos:
            segmento.goto(1000, 1000)

        segmentos.clear()

        pontos = 0
        texto.clear()
        texto.write(f"Pontos: {pontos}", align="center", font=("Arial", 24, "normal"))

    # Colisão com a comida
    if cabeca.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        novo_segmento = turtle.Turtle()
        novo_segmento.speed(0)
        novo_segmento.shape("square")
        novo_segmento.color("lightgreen")
        novo_segmento.penup()
        segmentos.append(novo_segmento)

        pontos += 10
        texto.clear()
        texto.write(f"Pontos: {pontos}", align="center", font=("Arial", 24, "normal"))

    # Movimento do corpo
    for i in range(len(segmentos)-1, 0, -1):
        x = segmentos[i-1].xcor()
        y = segmentos[i-1].ycor()
        segmentos[i].goto(x, y)

    if len(segmentos) > 0:
        x = cabeca.xcor()
        y = cabeca.ycor()
        segmentos[0].goto(x, y)

    mover()

    # Colisão com o próprio corpo
    for segmento in segmentos:
        if segmento.distance(cabeca) < 20:
            time.sleep(1)
            cabeca.goto(0, 0)
            cabeca.direction = "stop"

            for s in segmentos:
                s.goto(1000, 1000)

            segmentos.clear()

            pontos = 0
            texto.clear()
            texto.write(f"Pontos: {pontos}", align="center", font=("Arial", 24, "normal"))

    time.sleep(0.1)

tela.mainloop()
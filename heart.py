import turtle
import math
import time
import pygame
import os

diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_musica = os.path.join(diretorio_do_script, "i-wanna-be-yours.mp3")

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

try:
    if os.path.exists(caminho_musica):
        pygame.mixer.music.load(caminho_musica)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1, start=45.0)
except:
    pass

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("❤️")
screen.setup(width=800, height=800)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()

def draw_heart(scale, color):
    t.penup()
    t.color(color)
    t.begin_fill()
    for i in range(0, 635, 10):
        angle = i / 100
        x = scale * 16 * math.sin(angle)**3
        y = scale * (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) + 50
        t.goto(x, y)
        if i == 0:
            t.pendown()
    t.end_fill()

def draw_stickman(x, y, walk_cycle, direction, is_female=False, is_strong=False, kiss=False):
    t.color("white")
    t.pensize(6 if is_strong else 3)
    
    # cabeça
    t.penup(); t.goto(x, y + 50); t.pendown(); t.circle(10)
    
    # corpo
    if is_female:
        t.pensize(3)
        t.penup()
        t.goto(x, y + 35)
        t.pendown()
        t.begin_fill()
        # 👗 vestido MAIS FINO
        t.goto(x - 8, y + 12)
        t.goto(x + 8, y + 12)
        t.goto(x, y + 35)
        t.end_fill()
        t.penup(); t.goto(x, y + 12); t.pendown()
    else:
        t.penup(); t.goto(x, y + 40); t.pendown(); t.goto(x, y + 20)
    
    # pernas
    leg_swing = 0 if kiss else math.sin(walk_cycle) * 12
    base_y = 12 if is_female else 20
    t.goto(x + leg_swing, y)
    t.penup(); t.goto(x, base_y); t.pendown(); t.goto(x - leg_swing, y)

    # braços
    arm_y = y + 40
    t.penup(); t.goto(x, arm_y); t.pendown()

    if kiss:
        t.goto(x + (20 * direction), y + 40)
        t.penup(); t.goto(x, arm_y); t.pendown()
        t.goto(x + (20 * direction), y + 30)
    else:
        arm_swing = math.sin(walk_cycle) * 10
        t.goto(x - arm_swing, y + 20)
        t.penup(); t.goto(x, arm_y); t.pendown()
        t.goto(x + arm_swing, y + 20)

while True:
    message = "I LOVE YOU"
    steps = 150

    for i in range(steps + 1):
        if pygame.mixer.music.get_pos() / 1000 > 29:
            pygame.mixer.music.play(-1, start=45.0)

        t.clear()

        # coração
        for s in range(18, 14, -1):
            draw_heart(s, "#330000")
        draw_heart(14, "#ff1a1a")

        progress = i / steps
        offset = progress * 52 
        walk_speed = i * 0.35
        is_kissing = (i >= steps - 2)

        # personagens
        draw_stickman(-60 + offset, 0, walk_speed, 1, is_female=False, is_strong=True, kiss=is_kissing)
        draw_stickman(60 - offset, 0, walk_speed, -1, is_female=True, is_strong=False, kiss=is_kissing)

        # texto
        char_count = int(progress * len(message))
        current_text = message[:char_count + 1] if i > 10 else ""

        t.penup()
        t.goto(0, -250)
        t.color("#ff1a1a")
        t.write(current_text, align="center", font=("Segoe UI", 28, "bold"))

        screen.update()
        time.sleep(0.05)

    time.sleep(4)
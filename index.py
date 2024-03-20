import turtle
import time
import random
import pygame

# init data for player
score = 0
life = 2

# init music
pygame.init()
pygame.mixer.init()

# start music theme
pygame.mixer_music.load('music/theme.mp3')
pygame.mixer_music.play(-1, 0.0, 0)
pygame.mixer_music.set_volume(0.05)

turtle.color("white")
turtle.write("Eat the green, dodge the red", align="center", font=("Verdana",15, "normal"))

# init window
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor('black')
screen.title(f"Turtle game | {score} | Life(s) : {life}")

# init monster
monster = turtle.Turtle()
monster.shape('circle')
monster.color('Red')
monster.penup()
monster.goto(random.randint(-234, 235), random.randint(-234, 235))

# init collectible
collectible = turtle.Turtle()
collectible.shape('circle')
collectible.color('green')
collectible.penup()
collectible.goto(random.randint(-234, 235), random.randint(-234, 235))

# init boost
boost = turtle.Turtle()
boost.shape('circle')
boost.color('blue')
boost.penup()
boost.hideturtle()
boost.goto(random.randint(2000, 2000), random.randint(2000, 2000))

# init player
time.sleep(0.3)
player = turtle.Turtle()
player.shape('turtle')
player.color('Yellow')
player.penup()

# random boost spawn
def show_life():
    boost.goto(random.randint(-200, 200), random.randint(-200, 200))
    boost.showturtle()
    screen.ontimer(hide_life, 5000)

def hide_life():
    boost.hideturtle()
    next_appearance = random.randint(20000, 30000)
    screen.ontimer(show_life, next_appearance)

def collectible_utils():
    global score
    sound = pygame.mixer.Sound('music/collectible.mp3')
    sound.play()
    collectible.hideturtle()
    collectible.goto(random.randint(-234, 235), random.randint(-234, 235))
    collectible.showturtle()
    score += 1

def life_utils():
    global life
    sound = pygame.mixer.Sound('music/collectible.mp3')
    sound.play()
    boost.goto(random.randint(2000, 2000), random.randint(2000, 2000))
    life += 1
    boost.hideturtle
    screen.title(f"Turtle game | Score : {score} | Life(s) : {life}")

def eat():
    if player.distance(collectible) <= 10:
        collectible_utils()
        screen.title(f"Turtle game | Score : {score} | Life(s) : {life}")
    elif player.distance(boost) <= 10:
        life_utils()

# monster follow player
def monster_follow():
    global life
    if monster.distance(player) <= 13:
        if life == 1:
            sound = pygame.mixer.Sound('music/over.mp3')
            sound.play()
            time.sleep(3)
            turtle.bye()
        if life > 1:
            life -= 1
            screen.title(f"Turtle game | Score : {score} | Life(s) : {life}")
            sound = pygame.mixer.Sound('music/hit.mp3')
            sound.play()
            player.goto(0.00, 0.00)
            monster.goto(random.randint(-234, 235), random.randint(-234, 235))
    monster.setheading(monster.towards(player))
    monster.forward(10)
    screen.ontimer(monster_follow, 300)

# init game moves
def left():
    eat()
    print("POS: ", player.pos())
    player.left(10)

def forward():
    eat()
    print("POS: ", player.pos())
    player.forward(10)

def right():
    eat()
    print("POS: ", player.pos())
    player.right(10)

def back():
    eat()
    print("POS: ", player.pos())
    player.back(10)

def quit():
    time.sleep(3)
    turtle.bye()

hide_life()
monster_follow()
    
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
screen.onkeypress(forward, "Up")
screen.onkeypress(back, "Down")
screen.onkeypress(quit, "Escape")
screen.listen()

turtle.mainloop()

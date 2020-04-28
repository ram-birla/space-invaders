import turtle
import math
import winsound
import random
from tkinter import PhotoImage

w = turtle.Screen()
w.title("Space Invaders")
w.bgcolor("black")
w.bgpic("bg.png")
w.tracer(0)
w.register_shape("p2.gif")
w.register_shape("e2.gif")


border = turtle.Turtle()
border.speed(2)
border.color("white")
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(600)
    border.lt(90)

border.hideturtle()

#scoreboard
 
score = 0

s = turtle.Turtle()
s.color("yellow")
s.penup()
s.speed(0)
s.setposition(-350,250)
s.write("S",align="center",font=("Arial",30,"normal"))
s.hideturtle()

c = turtle.Turtle()
c.color("yellow")
c.penup()
c.speed(0)
c.setposition(-350,200)
c.write("C",align="center",font=("Arial",30,"normal"))
c.hideturtle()

o = turtle.Turtle()
o.color("yellow")
o.penup()
o.speed(0)
o.setposition(-350,150)
o.write("O",align="center",font=("Arial",30,"normal"))
o.hideturtle()

r = turtle.Turtle()
r.color("yellow")
r.penup()
r.speed(0)
r.setposition(-350,100)
r.write("R",align="center",font=("Arial",30,"normal"))
r.hideturtle()

e = turtle.Turtle()
e.color("yellow")
e.penup()
e.speed(0)
e.setposition(-350,50)
e.write("E",align="center",font=("Arial",30,"normal"))
e.hideturtle()

scr = turtle.Turtle()
scr.color("blue")
scr.penup()
scr.speed(0)
scr.setposition(-350,0)
scrstr = "%s" %score
scr.write(scrstr,False,align="center",font=("Arial",30,"normal"))
scr.hideturtle()

end = turtle.Turtle()
end.color("red")
end.penup()
end.speed(1)
end.setposition(0,0)
end.hideturtle()

right = turtle.Turtle()
right.color("red")
right.penup()
right.speed(0)
right.setposition(-251,268)
right.hideturtle()

head = turtle.Turtle()
head.color("white")
head.penup()
head.speed(0)
head.setposition(0,250)
head.write("SPACE-INVADERS",align="center",font=("Arial",35,"normal"))
head.hideturtle()

#player
player = turtle.Turtle()
player.color("red")
player.shape("p2.gif")

player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 3

#bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.shapesize(0.5,0.5)
bullet.setheading(90)
bullet.hideturtle()

bulletspeed = 5

bulletstate = "ready"


def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x>280:
        x= 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False 

w.listen()
w.onkeypress(move_left,"Left")
w.onkeypress(move_right,"Right")
w.onkeypress(fire_bullet,"space")


def level1():
    right.clear()
    right.write("Level-1",align="center",font=("Arial",20,"normal"))
    
    no_of_enemies = 5
    global score
    global bulletstate 
    enemies = []

    for i in range(no_of_enemies):
        enemies.append(turtle.Turtle())

    for enemy in enemies:
        enemy.color("green")
        enemy.shape("e2.gif")
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200,200)
        y = random.randint(100,250)
        enemy.setposition(x,y)
    enemyspeed = 0.2
    
    while score != 100:
        w.update()
        for enemy in enemies:
            x = enemy.xcor()
            x +=enemyspeed
            enemy.setx(x)

            if enemy.xcor() > 280:
                for e in enemies:
                    y = e.ycor()
                    y -=40
                    e.sety(y)
                enemyspeed *= -1

            if enemy.xcor() < -280:
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                enemyspeed *= -1

            if isCollision(bullet,enemy):
                winsound.PlaySound("eexp.wav", winsound.SND_ASYNC)
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0,-400)
                x = random.randint(-200,200)
                y = random.randint(100,250)
                enemy.setposition(x,y)
                score += 10
                scrstr = "%s" %score
                scr.clear()
                scr.write(scrstr,False,align="center",font=("Arial",30,"normal"))

            if isCollision(player,enemy):
                winsound.PlaySound("pexp.wav", winsound.SND_ASYNC)
                player.hideturtle()
                enemy.hideturtle()
                end.write("GAME OVER!",align="center",font=("Arial",35,"normal"))
                print("Game Over")

        if bulletstate == "fire":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)
        
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"
        
        if score == 100:
            for e in enemies:
                e.setposition(0,-10000)
            level2()

def level2():
    
    right.clear()
    right.write("Level-2",align="center",font=("Arial",20,"normal"))
    
    no_of_enemy = 30
    global score
    global bulletstate
    enemi = []
    enemy_start_x = -225
    enemy_start_y = 250
    enemy_number = 0

    for i in range(no_of_enemy):
        enemi.append(turtle.Turtle())

    for enemy in enemi:
        enemy.color("green")
        enemy.shape("e2.gif")
        enemy.penup()
        enemy.speed(0)
        x = enemy_start_x + (50*enemy_number)
        y = enemy_start_y
        enemy.setposition(x,y)
        
        enemy_number += 1

        if enemy_number == 10:
            enemy_start_y -= 50
            enemy_number = 0

    enemyspeed = 0.1

    while score != 400:
        w.update()
        for enemy in enemi:
            x = enemy.xcor()
            x +=enemyspeed
            enemy.setx(x)

            if enemy.xcor() > 280:
                for e in enemi:
                    y = e.ycor()
                    y -=40
                    e.sety(y)
                enemyspeed *= -1

            if enemy.xcor() < -280:
                for e in enemi:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                enemyspeed *= -1

            if isCollision(bullet,enemy):
                winsound.PlaySound("eexp.wav", winsound.SND_ASYNC)
                bullet.hideturtle()
                bulletstate = "ready"
                bullet.setposition(0,-400)
                enemy.setposition(0,10000)
                score += 10
                scrstr = "%s" %score
                scr.clear()
                scr.write(scrstr,False,align="center",font=("Arial",30,"normal"))

            if isCollision(player,enemy):
                winsound.PlaySound("pexp.wav", winsound.SND_ASYNC)
                player.hideturtle()
                enemy.hideturtle()
                end.clear()
                end.write("GAME OVER!",align="center",font=("Arial",35,"normal"))
                print("Game Over")

        if bulletstate == "fire":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)
        
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"

        if score == 400:
            for e in enemi:
                e.setposition(10000,0)
            level3()

def level3():
    pass







if score <= 100:
    level1()



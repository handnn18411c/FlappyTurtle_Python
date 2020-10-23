# Import the Turtle module
import turtle
import time

# Import message box
import tkinter as tk
from tkinter import messagebox


def createScreen():
    # Setting for screen
    sc = turtle.Screen()
    sc.title("Flappy Turtle by Nhật Hàn SP")
    # sc.bgcolor("lightblue")
    sc.bgpic("ocean.gif")
    sc.setup(500, 700)
    sc.tracer(0)  # stop screen updating
    return sc


def MessageStart():
    MsgBox = tk.messagebox.askquestion(
        "Welcome to Flappy Turtle", "Are you ready to play", icon="question"
    )
    if MsgBox == "yes":
        onStart()
    else:
        turtle.done()


def onRetry(score):
    ListScore.append(score)
    highscore = ListScore[0]
    for i in range(len(ListScore) - 1):
        if i == 0:
            continue
        if ListScore[i] > highscore:
            highscore = ListScore[i]

    if score > highscore:
        highscore = score
    MsgBox = tk.messagebox.askquestion(
        "Your score: %s" % (score),
        "Your highscore: %s\nDo you want to play again?" % (highscore),
        icon="question",
    )
    if MsgBox == "yes":
        onStart()
    else:
        turtle.done()


def onClear(sc, player, top1, bottom1, top2, bottom2):
    sc.clear()
    player.clear()
    top1.clear()
    bottom1.clear()
    top2.clear()
    bottom2.clear()


def onStart():
    sc = createScreen()
    # Create Score UI
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.penup()
    pen.color("white")
    pen.goto(0, 250)
    pen.write("0", move=False, align="left", font=("Arial", 32, "normal"))

    # setting player
    player = turtle.Turtle()
    player.speed(0)
    player.penup()  # pen up to not create a line draw
    sc.addshape("sea-turtle.gif")
    player.shape("sea-turtle.gif")
    player.goto(-200, 0)
    player.dx = 0  # set location
    player.dy = 1

    pipe1_top = turtle.Turtle()
    pipe1_top.speed(0)
    pipe1_top.penup()
    pipe1_top.color("green")
    pipe1_top.shape("square")
    pipe1_top.shapesize(18, 3, None)
    pipe1_top.goto(300, 250)
    pipe1_top.dx = -2
    pipe1_top.dy = 0
    pipe1_top.value = 1

    pipe1_bottom = turtle.Turtle()
    pipe1_bottom.speed(0)
    pipe1_bottom.penup()
    pipe1_bottom.color("green")
    pipe1_bottom.shape("square")
    pipe1_bottom.shapesize(18, 3, None)
    pipe1_bottom.goto(300, -300)
    pipe1_bottom.dx = -2
    pipe1_bottom.dy = 0

    pipe2_top = turtle.Turtle()
    pipe2_top.speed(0)
    pipe2_top.penup()
    pipe2_top.color("green")
    pipe2_top.shape("square")
    pipe2_top.shapesize(18, 3, None)
    pipe2_top.goto(600, 300)
    pipe2_top.dx = -2
    pipe2_top.dy = 0
    pipe2_top.value = 1

    pipe2_bottom = turtle.Turtle()
    pipe2_bottom.speed(0)
    pipe2_bottom.penup()
    pipe2_bottom.color("green")
    pipe2_bottom.shape("square")
    pipe2_bottom.shapesize(18, 3, None)
    pipe2_bottom.goto(600, -200)
    pipe2_bottom.dx = -2
    pipe2_bottom.dy = 0

    # setting player animation
    gravity = -0.3
    # Initialize score
    player.score = 0
    # Define function:
    def go_up():
        player.dy += 8
        if player.dy > 8:
            player.dy = 8

    # Keyboard binding
    sc.listen()
    sc.onkeypress(go_up, "space")
    while True:
        # Pause
        time.sleep(0.02)
        # Update the screen
        sc.update()

        # Setting gravity
        player.dy += gravity

        # Player movement
        y = player.ycor()
        y += player.dy
        player.sety(y)

        # Bottom Border
        if player.ycor() < -390:
            player.dy = 0
            player.sety(-390)

        # Move Pipe 1
        x = pipe1_top.xcor()
        x += pipe1_top.dx
        pipe1_top.setx(x)

        x = pipe1_bottom.xcor()
        x += pipe1_bottom.dx
        pipe1_bottom.setx(x)

        # Return pipes 1 to start
        if pipe1_top.xcor() < -350:
            pipe1_top.setx(350)
            pipe1_bottom.setx(350)
            pipe1_top.value = 1

        # Move Pipe 2
        x = pipe2_top.xcor()
        x += pipe2_top.dx
        pipe2_top.setx(x)

        x = pipe2_bottom.xcor()
        x += pipe2_bottom.dx
        pipe2_bottom.setx(x)

        # Return pipes 2 to start
        if pipe2_top.xcor() < -350:
            pipe2_top.setx(350)
            pipe2_bottom.setx(350)
            pipe2_top.value = 1

        # Check if collisions with pipes
        # Pipe 1
        if (player.xcor() + 10 > pipe1_top.xcor() - 30) and (
            player.xcor() - 10 < pipe1_top.xcor() + 30
        ):
            if (player.ycor() + 10 > pipe1_top.ycor() - 180) or (
                player.ycor() - 10 < pipe1_bottom.ycor() + 180
            ):
                pen.clear()
                pen.write(
                    "Game Over",
                    move=False,
                    align="center",
                    font=("Arial", 16, "normal"),
                )
                sc.update()
                onClear(sc, player, pipe1_top, pipe1_bottom, pipe2_top, pipe2_bottom)
                onRetry(player.score)
                time.sleep(3)
                # Reset score
                player.score = 0
                # Move Pipes Back
                pipe1_top.setx(300)
                pipe1_bottom.setx(300)
                pipe1_top.setx(600)
                pipe1_bottom.setx(600)
                # Move Player back
                player.goto(-200, 0)
                player.dy = 0

        # Check for score
        if pipe1_top.xcor() + 30 < player.xcor() - 10:
            player.score += pipe1_top.value
            pipe1_top.value = 0
            pen.clear()
            pen.write(
                player.score, move=False, align="center", font=("Arial", 32, "normal")
            )

        # Check for collisions with pipes
        # Pipe 2
        if (player.xcor() + 10 > pipe2_top.xcor() - 30) and (
            player.xcor() - 10 < pipe2_top.xcor() + 30
        ):
            if (player.ycor() + 10 > pipe2_top.ycor() - 180) or (
                player.ycor() - 10 < pipe2_bottom.ycor() + 180
            ):
                pen.clear()
                pen.write(
                    "Game Over", move=False, align="left", font=("Arial", 16, "normal")
                )
                sc.update()
                onClear(sc, player, pipe1_top, pipe1_bottom, pipe2_top, pipe2_bottom)
                onRetry(player.score)
                time.sleep(3)
                # Reset score
                player.score = 0
                # Move Pipes Back
                pipe2_top.setx(300)
                pipe2_bottom.setx(300)
                pipe2_top.setx(600)
                pipe2_bottom.setx(600)
                # Move Player back
                player.goto(-200, 0)
                player.dy = 0
                # Clear the pen
                pen.clear()

        # Check for score
        if pipe2_top.xcor() + 30 < player.xcor() - 10:
            player.score += pipe2_top.value
            pipe2_top.value = 0
            pen.clear()
            pen.write(
                player.score, move=False, align="left", font=("Arial", 32, "normal")
            )


ListScore = list()  # Save HighScore
createScreen()
MessageStart()


turtle.done()
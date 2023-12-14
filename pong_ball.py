import turtle

score = 0
high_score = 0

#screen window of the game
window = turtle.Screen()
window.title("Pong Ball Game with Python")
window.setup(width=600, height=600)
window.cv._rootwindow.resizable(False, False)
window.bgcolor("#222")
window.tracer(0)

#bat
bat = turtle.Turtle()
bat.shape("square")
bat.color("#DA3B01")
bat.shapesize(stretch_wid=1, stretch_len=5)
bat.goto(0, -250)
bat.speed(0)
bat.penup()

#ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("#FFF")
ball.goto(0, 0)
ball.speed(0)
ball.penup()
ball.dy = 0.5
ball.dx = 0.5

#pen of score
pen = turtle.Turtle()
pen.shape("square")
pen.color("#FFF")
pen.goto(0, 250)
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.write("Score: {}      High Score: {}".format(score, high_score), align="center", font=("Arial", 25, "bold"))

#movement of bat
def goright():
    bat.setx(bat.xcor() + 20)
def goleft():
    bat.setx(bat.xcor() - 20)

window.listen()
window.onkeypress(goright, "d")
window.onkeypress(goleft, "a")

#gameplay loop
while True:
    window.update()

    #movement of ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    #reverse direction of ball when collision with wall
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
    if ball.xcor() > 280:
        ball.setx(280)
        ball.dx *= -1
    if ball.xcor() < -280:
        ball.setx(-280)
        ball.dx *= -1

    #check if ball falls out bottom of screen
    if ball.ycor() < -280:
        ball.goto(0, 0)
        ball.dy *= -1
        if score > 5:
            score -= 5
        elif score < 5:
            score = 0
        pen.clear()
        pen.write("Score: {}      High Score: {}".format(score, high_score), align="center", font=("Arial", 25, "bold"))

    #check if ball collisions with bat
    if (ball.ycor() > -250 and ball.ycor() < -240) and (ball.xcor() < bat.xcor() + 40 and ball.xcor() > bat.xcor() - 40):
        score += 1
        if score > high_score:
            high_score = score
        bat.sety(-250)
        ball.dy *= -1
        pen.clear()
        pen.write("Score: {}      High Score: {}".format(score, high_score), align="center", font=("Arial", 25, "bold"))
import turtle
screen = turtle.Screen()
screen.title("Pong by Aayana ")
screen.bgcolor("black")
screen.setup(width= 600, height= 600)

#ball
ball = turtle.Turtle()
ball.color("#ffcef")
ball.shape("circle")
ball.speed(30)
ball.up()#penup
ball.goto(0,0)
ball.dx = 5
ball.dy = 5

#player 1
player1 = turtle.Turtle()
player1.color("purple")
player1.shape("square")
player1.up()
player1.speed(0)
player1.goto(-300,0)
player1.shapesize(stretch_wid= 3, stretch_len=1)


#player 2
player2 = turtle.Turtle()
player2.color("blue")
player2.shape("square")
player2.up()
player2.goto(300,0)
player2.shapesize(stretch_wid=2,stretch_len=1)


#Score
score1 = 0
score2 = 0
Score = turtle.Turtle()
Score.color("red")
Score.penup()
Score.goto(0,200)
Score.write("Score: {} | {} ".format(score1, score2))

#function - holds a bunch of code that you can call at any time
def Game(x,y):
    #infinte loop
    while True:
        screen.update()
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)






#wait till click screen to start
screen.onscreenclick(Game())

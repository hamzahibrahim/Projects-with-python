import turtle as t
import random 

t.bgcolor('white')
t.setup(width = 900, height = 650)

snake = t.Turtle()
snake.color('red')
snake.shape("square")
snake.speed(0)
snake.penup()
snake.hideturtle()

leaf = t.Turtle()
leaf.shape('circle')
leaf.color('dark blue')
leaf.penup()
leaf.hideturtle()
leaf.speed()

game_started = False
text_turtle = t.Turtle()
text_turtle.write('To gain score eat the leafs\n    Press SPACE to start',align='center',font=('Arial',16,'bold'))
text_turtle.color('green')
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = snake.pos()
    outside = x < left_wall or  x > right_wall or  y < bottom_wall or y > top_wall
    return outside

def game_over():
    snake.color('white')
    leaf.color('white')
    t.penup()
    t.hideturtle()
    t.color("red")
    t.write('GAME OVER!',align='center' , font=('Aerial',30,'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2)-45
    y = (t.window_height() / 2)-55
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score) , align = 'right',font=('Arial',40,'bold'))

def place_leaf():
    leaf.hideturtle()
    leaf.setx(random.randint(-300,300))
    leaf.sety(random.randint(-300,300))
    leaf.showturtle()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

    snake_speed = 1
    snake_length = 1
    snake.shapesize(1,snake_length,1)
    snake.showturtle()
    display_score(score)
    place_leaf()

    while True:
        snake.forward(snake_speed)
        if snake.distance(leaf)<30:
            place_leaf()
            snake_length = snake_length + 1
            snake.shapesize(1,snake_length,1)
            snake_speed = snake_speed + 1
            score = score + 10
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(90)

def move_down():
    if snake.heading() == 0 or snake.heading() == 180:
        snake.setheading(270)

def move_left():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(180)

def move_right():
    if snake.heading() == 90 or snake.heading() == 270:
        snake.setheading(0)


t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()

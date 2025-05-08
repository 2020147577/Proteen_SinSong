# testing snake game
from turtle import Turtle, Screen
import time
import random

# 뱀 방향 제어 함수
def up():
    if snakes[0].heading() != 270:
        snakes[0].setheading(90)

def down():
    if snakes[0].heading() != 90:
        snakes[0].setheading(270)

def left():
    if snakes[0].heading() != 0:
        snakes[0].setheading(180)

def right():
    if snakes[0].heading() != 180:
        snakes[0].setheading(0)

# 뱀 몸통 생성
def create_snake(pos):
    snake_body = Turtle()
    snake_body.shape("square")
    snake_body.color("orangered")
    snake_body.penup()
    snake_body.goto(pos)
    snakes.append(snake_body)

# 먹이 위치 랜덤
def rand_pos():
    rand_x = random.randint(-250, 250)
    rand_y = random.randint(-250, 250)
    return rand_x, rand_y

# 점수 업데이트
def score_update():
    global score
    score += 1
    score_pen.clear()
    score_pen.write(f"점수 : {score}", font=("", 15, "bold"))

# 화면 설정
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("khaki")
screen.title("Snake Game")
screen.tracer(0)

# 뱀 초기 위치
start_pos = [(0, 0), (-20, 0), (-40, 0)]
snakes = []

for pos in start_pos:
    create_snake(pos)

# 먹이 설정
food = Turtle()
food.shape("circle")
food.color("snow")
food.penup()
food.speed(0)
food.goto(rand_pos())

# 점수판
score = 0
score_pen = Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.goto(-270, 250)
score_pen.write(f"점수 : {score}", font=("", 15, "bold"))

# 키보드 입력
screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

# 게임 루프
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    # 몸통 이동
    for i in range(len(snakes) - 1, 0, -1):
        snakes[i].goto(snakes[i - 1].pos())

    # 머리 전진
    snakes[0].forward(20)

    # 먹이 먹음
    if snakes[0].distance(food) < 15:
        score_update()
        food.goto(rand_pos())
        create_snake(snakes[-1].pos())

    # 벽에 부딪힘
    if snakes[0].xcor() > 280 or snakes[0].xcor() < -280 or \
       snakes[0].ycor() > 280 or snakes[0].ycor() < -280:
        game_on = False

    # 몸통에 부딪힘
    for body in snakes[1:]:
        if snakes[0].distance(body) < 10:
            game_on = False

# 게임 종료 메시지
score_pen.goto(0, 0)
score_pen.write("Game Over", align="center", font=("", 30, "bold"))

screen.mainloop()

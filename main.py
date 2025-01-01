import turtle as t
import time
from snake import Snake
from food import Food
from score import Score

WALL = 290

screen = t.Screen()
screen.setup(600,600)
screen.title("Snake Game")
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')


is_game_on = True
while is_game_on:
    screen.update()
    snake.move()
    time.sleep(0.1)

    # x = food.food_location()[0] - snake.snake_location()[0]
    # y = food.food_location()[1] - snake.snake_location()[1]

    #Detect collision with food
    if snake.head.distance(food) <= 15:
        food.refresh()
        score.update_score()
        snake.extend()

    #Detect collision with wall
    x = snake.head.xcor()
    y = snake.head.ycor()
    if x >= WALL or x <= -WALL or y >= WALL or y <= -WALL:
        score.reset()
        food.refresh()
        snake.reset()

#collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <= 15:
            score.reset()
            food.refresh()
            snake.reset()



screen.exitonclick()
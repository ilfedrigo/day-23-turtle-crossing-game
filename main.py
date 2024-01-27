import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()

scoreboard = Scoreboard()

car_manager = CarManager()


screen.listen()
screen.onkey(turtle.go_up, "w")
screen.onkey(turtle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Detect next level
    if turtle.ycor() > 280:
        turtle.reset_position()
        scoreboard.point()
        car_manager.increase_speed()

screen.exitonclick()
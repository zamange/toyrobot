
# -------------------------------------------------------------------------------------------------
#
# TODO: Please replace this placeholder code with your solution for Toy Robot 4, and work from there.
#
# -------------------------------------------------------------------------------------------------
import turtle as t
#from world import obstacles
import random


t.pencolor("red")
t.getscreen()
t.penup()
t.goto(-100,200)



t.pendown()
t.goto(100,200)
t.goto(100,-200)
t.goto(-100,-200)
t.goto(-100,200)
t.penup()
t.home()

random_number_obstacle=random.randint(0,10)

obstacle_coord_list=[]
for i in range(random_number_obstacle):
        obstacle_coord_list.append((random.randint(-100,100),random.randint(-200,200)))


for coord in obstacle_coord_list:
        t.penup()
        t.goto(coord[0],coord[1])
        t.pendown()
        t.goto(coord[0] + 4,coord[1])
        t.goto(coord[0] + 4,coord[1]+4)
        t.goto(coord[0] ,coord[1]+4)
        t.goto(coord[0],coord[1])




t.penup()
t.home()
t.exitonclick()

import turtle
import sys
import import_helper

global obstacles

def return_obst_import():
    """
        function returns module
        :returns obstacles: this module
    """
    global obstacles

    return obstacles

import turtle
import sys
import import_helper


def setup_turtle(robot_name):
    """
        init the turle
    """
    turtle.title(robot_name)
    turtle.tracer(5,2)
    turtle.penup()
    turtle_draw_constraints_box()
    turtle_draw_obstacles(robot_name)
    turtle_reset_and_center()
    turtle.penup()
    turtle.tracer(1)


def turtle_draw_constraints_box():
    """
        func draws the robots constraints box
    """
    turtle.goto(-100,200)
    turtle.pencolor("red")
    turtle.pensize(3)
    turtle.pendown()
    turtle.goto(100,200)
    turtle.goto(100,-200)
    turtle.goto(-100,-200)
    turtle.goto(-100,200)
    turtle.penup()


def turtle_reset_and_center():
    """
        func resets and recenters turtle
    """
    turtle.color("purple")
    turtle.home()
    turtle.left(90)


def turtle_turn_left():
    """
        make turle turn left
    """
    turtle.left(90)


def turtle_turn_right():
    """
        makes turn turn right
    """
    turtle.right(90)


def draw_one_obstacle(x,y):
    """
        function draws one obstacle in turtle mode
        :param x: obstacle x position
        :param y: obstacle y position
    """
    turtle.begin_fill()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+4,y)
    turtle.goto(x+4,y+4)
    turtle.goto(x,y+4)
    turtle.goto(x,y)
    turtle.end_fill()
    turtle.penup()


def turtle_draw_obstacles(robot_name):
    """
        draws all obstacles one by one and resets turtle
    """
    global obstacles

    #importing obstacles module
    argv_value = sys.argv[len(sys.argv)-1].lower()
    if argv_value == "turtle":
        argv_value = "obstacles"
    
    obstacles = import_helper.dynamic_import("maze."+argv_value)
    print(''+robot_name+': Loaded '+argv_value+'.')

    #Drawing obstacles
    list_of_obst = obstacles.get_obstacles()
    for each in list_of_obst:
        draw_one_obstacle(each[0], each[1])


def print_obstacles(robot_name):
    """
        function prints a list of obstacles
    """
    pass


def show_position(robot_name, position_x, position_y):
    """
        moves turtle to given posistion
        :robot_name: name of bot
        :position_x: x coordinate
        :postion_y: y coordinate
    """
    turtle.goto(position_x,position_y)


def is_position_allowed(new_x, new_y, position_x, position_y):
    """
        Checks if the new position will still fall within the max area limit
        :param new_x: the new/proposed x position
        :param new_y: the new/proposed y position
        :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    # area limit vars
    min_y, max_y = -200, 200
    min_x, max_x = -100, 100

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y,\
             obstacles.is_path_blocked(position_x,position_y, new_x, new_y)


def update_position(steps, position_x, position_y, current_direction_index):
    """
        Update the current x and y positions given the current direction, and specific nr of steps
        :param steps:
        :return: True if the position was updated, else False
    """
    directions = ['forward', 'right', 'back', 'left']

    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    zone_flag, obst_flag = \
                    is_position_allowed(new_x, new_y, position_x, position_y)
    if zone_flag and not obst_flag:
        return zone_flag, obst_flag, new_x, new_y
    return zone_flag, obst_flag, position_x, position_y
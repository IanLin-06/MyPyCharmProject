"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


def jump():
    """
    Pre-condition:Karel is on the left side of the wall，facing East
    Post-condition:Karel is on the right side of the wall
    """
    up()
    cross()
    down()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def up():
    """
    Pre-condition:Karel is on the left side of the wall，facing East
    Post-condition:Karel is on the right side of the wall
    """
    turn_left()
    while not right_is_clear():
       move()
    #alternative:
    #while not front_is_clear
    #    turn_left()
    #    move()
    #    turn_right()


def cross():
    """
    Pre-condition:Karel is on the left side of the wall，facing East
    Post-condition:
    """
    turn_right()
    move()
    turn_right()

def down():
    """
    Pre-condition:Karel is on the left side of the wall，facing East
    Post-condition:
    """
    while front_is_clear():
        move()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)

import pygame
import math

# parameters

OwnInput = int(input("parameter selbst festlegen (1/0)"))

if OwnInput == 1:
    lengthA = int(input("gib die Länge der Grundseite an"))
    rekDepth = int(input("gib die Rekursionstiefe an"))
else:
    lengthA = 500
    rekDepth = 3

# screen size
screenWidth = int((4/3) * (math.sqrt(3) / 2) * lengthA * 1.1)
screenHeight = screenWidth

# starting point
turtle_x = 0.5 * (screenWidth - lengthA)
turtle_y = 0.5*screenHeight - ((1/3) * (math.sqrt(3) / 2) * lengthA)
turtle_angle = 0

# line properties
line_color = (0, 0, 0)
line_thickness = 1

# initialization
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
screen.fill((255,255,255))
pygame.display.flip()


def turn(angle: int):
    global turtle_angle
    turtle_angle += angle * math.pi / 180


def move(distance: int):
    global turtle_x, turtle_y
    old_y = turtle_y
    old_x = turtle_x
    turtle_y -= distance * math.sin(turtle_angle)
    turtle_x += distance * math.cos(turtle_angle)
    pygame.draw.line(screen, line_color, (old_x, old_y), (turtle_x, turtle_y), line_thickness)
    pygame.display.flip()


# your code here:
def koch(length: int, depth: int):
    if depth == 0:
        move(length)
        
    else:
        koch(length / 3, depth-1)
        turn(60) 
        koch(length / 3, depth-1)
        turn(-120)
        koch(length / 3, depth-1)
        turn(60)
        koch(length / 3, depth-1)
        
def kochtriangle(length: int, depth: int):
    koch(length, depth)
    turn(-120)
    koch(length, depth)
    turn(-120)
    koch(length, depth)
    turn(-120)

def kochfoo(length: int, depth: int):
    koch(length, depth)
    turn(-60)
    koch(length, depth)
    turn(-60)
    koch(length, depth)
    turn(-60)
    koch(length, depth)
    turn(-60)
    koch(length, depth)
    turn(-60)
    koch(length, depth)
    turn(-60)
    
kochtriangle(lengthA, rekDepth)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

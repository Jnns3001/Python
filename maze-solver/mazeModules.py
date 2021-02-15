import pygame
import random

tileSize = 1
def getParameters(n):
    tileSize = n


def printMap(mapList):
    for row in mapList:
        for tile in row:
            if tile:
                print('X', end='')
            else:
                print(' ', end='')
        print()


def loadTile(filename):
    return pygame.transform.scale(
        pygame.image.load(filename),
        (tileSize, tileSize))


def processEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()


def loadMap():
    global walls,  mapWidth, mapHeight, playerX, playerY, finishX, finishY, mapFile
    mapFile = open(mapFile).read().splitlines()
    # first line is map size, rest is the actual map
    (mapWidth, mapHeight), mapText = eval(mapFile[0]), mapFile[1:]

    # fill walls and set player, finish
    walls = emptyMap()
    for x in range(0, mapWidth):
        for y in range(0, mapHeight):
            if y >= len(mapText): continue
            if x >= len(mapText[y]): continue
            if mapText[y][x] == playerChar:
                playerX, playerY = x, y
            if mapText[y][x] == finishChar:
                finishX, finishY = x, y
            if mapText[y][x] == wallChar:
                walls[x][y] = True


def render():
    for x in range(mapWidth):
        for y in range(mapHeight):
            # wall or floor
            if walls[x][y]: drawTile(wallTile, x, y)
            else:           drawTile(floorTile, x, y)
            # trail
            if trail[x][y]:     drawTile(trailTile, x, y)
            elif visited[x][y]: drawTile(visitedTile, x, y)
    drawTile(finishTile, finishX, finishY)
    drawTile(playerTile, playerX, playerY)

    pygame.display.flip()


def emptyMap():
    return [[False for _ in range(mapHeight)] for _ in range(mapWidth)]


def drawTile(tile, x, y): screen.blit(tile, (x * tileSize, y * tileSize))


def demolisher(x,y) -> bool:
    global trail, visited, playerX, playerY, demoSteps

    demoSteps +=1
    
    if x < 0 or y < 0 or x >= mapWidth or y >= mapHeight:
        return False
    if walls[x][y]:
        return False
    if visited[x][y]:
        return False
        
    pygame.time.delay(stepTime)

    playerX, playerY = x, y
    trail[x][y] = visited[x][y] = True

    if doRender:
        render()
    
    # move
    z = [1, 2, 3, 4]
    random.shuffle(z)
    
    for i in range(0, 4):
        if z[i] == 1:
            if x+2 < mapWidth and trail[x+2][y] == False:
                walls[x+1][y] = False
                trail[x+1][y] = True
                demolisher(x+2, y)
        elif z[i] == 2:
            if y+2 < mapHeight and trail[x][y+2] == False:        
                walls[x][y+1] = False
                trail[x][y+1] = True
                demolisher(x, y+2)
        elif z[i] == 3:        
            if x-2 >= 0 and trail[x-2][y] == False:  
                walls[x-1][y] = False
                trail[x-1][y] = True
                demolisher(x-2, y)
        elif z[i] == 4:       
            if y-2 >= 0 and trail[x][y-2] == False:        
                walls[x][y-1] = False
                trail[x][y-1] = True
                demolisher(x, y-2)
           
        else:
            walls[x][y] = True
    return False


def generateMap():
    global walls,  mapWidth, mapHeight, playerX, playerY
    global finishX, finishY, mapFile, visited, trail
    walls = emptyMap()
    
    
    for x in range(0, mapWidth):
        for y in range(0, mapHeight):
            if x%2 == 0 and y%2 == 0:
                #walls[x][y] = False
                continue
            else:
                walls[x][y] = True
    finishX, finishY = mapWidth-2, mapHeight-2
    
    demolisher(playerX, playerY)
    
    trail = emptyMap()
    visited = emptyMap()
    render()


def step(x, y) -> bool:
    global trail, visited, playerX, playerY, walkSteps
    
    walkSteps += 1
    
    # check stuff
    
    if x < 0 or y < 0 or x >= mapWidth or y >= mapHeight:
        return False
    if walls[x][y]:
        return False
    if visited[x][y]:
        return False
    
    
    pygame.time.delay(stepTime)

    playerX, playerY = x, y
    trail[x][y] = visited[x][y] = True

    if doRender:
        render()
    
    if (x, y) == (finishX, finishY):
        return True
    
    # move
    if step(x+1, y):
        return True
        
    if step(x, y+1):
        return True

    if step(x-1, y):
        return True

    if step(x, y-1):
        return True

    trail[x][y] = False
    return False
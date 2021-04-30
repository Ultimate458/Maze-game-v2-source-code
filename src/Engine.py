"""

"""

#Made with Clear engine v3

try:
    import math
    import time
    import pygame
    import os
    import random
    from PIL import Image
    from pygame.locals import *
    from pygame import gfxdraw

except ImportError:
    print("Clear engine could not import necessary modules")
    raise ImportError

keys=[False]*324

Tex1=[
    [255,0,0],[255,0,0],[255,255,255],[255,0,0],
    [255,0,0],[255,0,0],[255,255,255],[255,0,0],
    [255,0,0],[255,0,0],[255,255,255],[255,0,0],
    [255,255,255],[255,255,255],[255,255,255],[255,255,255]
]

Map3 =  [
            [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
            [1, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
            [1, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
            [1, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]]

Map3f1 =  [
            [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]]

Maze1 =  [
            [4, 5, 4, 5, 4, 5, 3, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5],
            [5, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 4],
            [4, 0, 0, 2, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 5],
            [5, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 4],
            [4, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 5],
            [5, 0, 0, 1, 0, 1, 0, 1, 1, 0, 2, 1, 0, 2, 0, 1, 0, 1, 0, 4],
            [4, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 5],
            [5, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 2, 0, 1, 0, 1, 0, 4],
            [4, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 1, 0, 1, 0, 0, 0, 5],
            [5, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 0, 2, 0, 1, 2, 4],
            [4, 1, 0, 1, 1, 0, 1, 1, 0, 2, 0, 1, 0, 1, 0, 1, 0, 0, 0, 5],
            [5, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 2, 4],
            [4, 0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 0, 0, 5],
            [5, 1, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 0, 0, 1, 1, 0, 0, 1, 1, 2, 1, 1, 1, 0, 1, 1, 1, 1, 5],
            [5, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 5],
            [5, 1, 0, 1, 2, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 5],
            [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 3, 4, 5, 4, 5, 4]]

MazeWall =  [
            [4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4]]

Maze2 =  [
            [4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5],
            [5, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 4],
            [4, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 1, 0, 4],
            [4, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 5],
            [5, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 1, 0, 1, 0, 4],
            [4, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 2, 0, 2, 0, 5],
            [5, 1, 0, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 2, 0, 1, 0, 1, 0, 4],
            [4, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 2, 0, 0, 0, 5],
            [5, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 2, 0, 1, 0, 1, 2, 4],
            [4, 2, 0, 2, 1, 0, 1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 5],
            [5, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 2, 0, 2, 4],
            [4, 0, 0, 0, 0, 0, 1, 2, 1, 2, 1, 0, 1, 2, 0, 2, 0, 0, 0, 5],
            [5, 1, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 0, 0, 1, 2, 0, 0, 1, 2, 1, 2, 1, 2, 0, 2, 1, 2, 1, 5],
            [5, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 5],
            [5, 1, 0, 1, 2, 1, 0, 0, 2, 1, 2, 1, 0, 2, 0, 1, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 5],
            [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 3, 4, 5, 4, 5, 4]]

# A map over the world

def LoadTex(Path):
    P=Image.open(Path)
    PIMG=Wall1R.convert("RGB")
    Out=PIMG

def Lerp(a,b,x):
    return a + (b-a) * x

def LerpColor3(a,b,x):
    FinishColor = [0,0,0]
    FinishColor[0] = Lerp(a[0],b[0],0.5)
    FinishColor[1] = Lerp(a[1],b[1],0.5)
    FinishColor[2] = Lerp(a[2],b[2],0.5)
    FinishTuple=(int(FinishColor[0]),int(FinishColor[1]),int(FinishColor[2]))
    return FinishTuple

# Closes the program 
def close(): 
    pygame.display.quit()
    pygame.quit()

def main():
    pygame.init()

    # Head Up Display information (HUD)
    font = pygame.font.SysFont("Verdana",20)
    HUD = font.render("F1 / F2 - Screenshot JPEG/BMP   F5/F6 - Shadows on/off   F7/F8 - HUD Show/Hide", True, (0,0,0))

    Upscale=1

    WIDTH = 320
    HEIGHT = 180
    OutW = 1280
    OutH = 720

    # Creates window
    if Upscale == 1:
        screenR = pygame.display.set_mode((OutW, OutH))
        pygame.display.set_caption("Really cool maze game!")

        screen = pygame.Surface((WIDTH, HEIGHT))
    else:
        WIDTH=OutW
        HEIGHT=OutH
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Really cool maze game!")

    showShadow = True
    showHUD = True
    
    # Defines starting position and direction
    positionX = 1
    positionY = 6.5

    directionX = 1
    directionY = 0

    planeX = 0.0
    planeY = 0.5

    # Movement constants
    RotPF=1.024
    #MovePF=1.2
    MovePF=4.8
    ROTATIONSPEED = 0.008
    MOVESPEED = 0.03

    MoveForward=0
    MoveBack=0
    TurnLeft=0
    TurnRight=0

    Antialiasing=0

    LTime = time.time()
    frames=0
    fps=60

    CurrMap=1

    TexX=0
    TexXA=0
    LSide=0
    LType=0
    LXDec=0
    texXA=0
    LMapX=0
    LMapY=0

    BadMath=0

    BetterTex=1

    SecondFloorE=1

    FilterTextures=0

    worldMap = Maze1
    worldMapf1 = MazeWall
    worldMapb1 = None

    TSprite=Image.open('TestSprite.png')
    TSprite=TSprite.convert("RGB")

    Wall1R=Image.open('Wall1.png')
    Wall2R=Image.open('Wall2.png')
    Wall3R=Image.open('Wall3.png')
    Wall1=Wall1R.convert("RGB")
    Wall2=Wall2R.convert("RGB")
    Wall3=Wall3R.convert("RGB")

    if FilterTextures == 1:
        for j in range(Wall1.size[1]):
            for i in range(Wall1.size[0]):
                if i+1<Wall1.size[0]:
                    if j+1<Wall1.size[1]:
                        Wall1.putpixel((i,j),LerpColor3(Wall1.getpixel((i,j)),Wall1.getpixel((i+1,j+1)),0.5))
                    else:
                        Wall1.putpixel((i,j),LerpColor3(Wall1.getpixel((i,j)),Wall1.getpixel((i+1,j)),0.5))

    print(TSprite.getpixel((0,0)))

    # Trigeometric tuples + variables for index
    TGM = (math.cos(ROTATIONSPEED), math.sin(ROTATIONSPEED))
    ITGM = (math.cos(-ROTATIONSPEED), math.sin(-ROTATIONSPEED))
    COS, SIN = (0,1)

    Clock = pygame.time.Clock()
    
    while True:
        ROTATIONSPEED=RotPF*fps
        MOVESPEED=MovePF/fps
        # Catches user input
        # Sets keys[key] to True or False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    close()
                    return
                if event.key == K_LEFT:
                    TurnLeft=1
                if event.key == K_RIGHT:
                    TurnRight=1
                if event.key == K_UP:
                    MoveForward = 1
                if event.key == K_DOWN:
                    MoveBack = 1
                if event.key == K_F1:
                    try:
                        pygame.image.save(screen,('PyRay' + time.strftime('%Y%m%d%H%M%S')+ '.jpeg'))
                    except:
                        print("Couldn't save jpeg screenshot")
                if event.key == K_F2:
                    try:
                        pygame.image.save(screen,('PyRay' + time.strftime('%Y%m%d%H%M%S')+ '.bmp'))
                    except:
                        print("Couldn't save bmp screenshot")
                if event.key == K_F5:
                    showShadow = True
                if event.key == K_F6:
                    showShadow = False
                if event.key == K_F7:
                    showHUD = True
                if event.key == K_F8:
                    showHUD = False
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    TurnLeft=0
                if event.key == K_RIGHT:
                    TurnRight=0
                if event.key == K_UP:
                    MoveForward = 0
                if event.key == K_DOWN:
                    MoveBack = 0

        positionX=round(positionX,2)
        positionY=round(positionY,2)
        if MoveForward == 1:
            if not worldMap[int(positionX + directionX * MOVESPEED)][int(positionY)]:
                positionX += directionX * MOVESPEED
            if not worldMap[int(positionX)][int(positionY + directionY * MOVESPEED)]:
                positionY += directionY * MOVESPEED
        if MoveBack == 1:
            if not worldMap[int(positionX - directionX * MOVESPEED)][int(positionY)]:
                    positionX -= directionX * MOVESPEED
            if not worldMap[int(positionX)][int(positionY - directionY * MOVESPEED)]:
                positionY -= directionY * MOVESPEED
        if TurnRight == 1:
            oldDirectionX = directionX
            directionX = directionX * TGM[COS] - directionY * TGM[SIN]
            directionY = oldDirectionX * TGM[SIN] + directionY * TGM[COS]
            oldPlaneX = planeX
            planeX = planeX * TGM[COS] - planeY * TGM[SIN]
            planeY = oldPlaneX * TGM[SIN] + planeY * TGM[COS]
        if TurnLeft == 1:
            oldDirectionX = directionX
            directionX = directionX * ITGM[COS] - directionY * ITGM[SIN]
            directionY = oldDirectionX * ITGM[SIN] + directionY * ITGM[COS]
            oldPlaneX = planeX
            planeX = planeX * ITGM[COS] - planeY * ITGM[SIN]
            planeY = oldPlaneX * ITGM[SIN] + planeY * ITGM[COS]

        if BadMath == 1:
            directionX=round(directionX,2)
            directionY=round(directionY,2)
            positionX=round(positionX,1)
            positionY=round(positionY,1)
        # Checks with keys are pressed by the user
        # Uses if so that more than one button at a time can be pressed.   

        # showShadows - On / Off

        # showHUD - Show / Hide
            
        # Draws roof and floor
        screen.fill((25,25,25))
        pygame.draw.rect(screen, (50,50,50), (0, HEIGHT/2, WIDTH, HEIGHT/2)) 
                
        # Starts drawing level from 0 to < WIDTH

        #Draw second floor
        if SecondFloorE == 1:
            column = 0        
            while column < WIDTH and worldMapf1 != None:
                cameraX = 2.0 * column / WIDTH - 1.0
                rayPositionX = positionX
                rayPositionY = positionY
                rayDirectionX = directionX + planeX * cameraX
                rayDirectionY = directionY + planeY * cameraX + .000000000000001 # avoiding ZDE 

                # In what square is the ray?
                mapX = int(rayPositionX)
                mapY = int(rayPositionY)

                # Delta distance calculation
                # Delta = square ( raydir * raydir) / (raydir * raydir)
                try:
                    deltaDistanceX = math.sqrt(1.0 + (rayDirectionY * rayDirectionY) / (rayDirectionX * rayDirectionX))
                    deltaDistanceY = math.sqrt(1.0 + (rayDirectionX * rayDirectionX) / (rayDirectionY * rayDirectionY))
                except:
                    deltaDistanceX = 64
                    deltaDistanceY = 64
                    print("Bad")

                # We need sideDistanceX and Y for distance calculation. Checks quadrant
                if (rayDirectionX < 0):
                    stepX = -1
                    sideDistanceX = (rayPositionX - mapX) * deltaDistanceX

                else:
                    stepX = 1
                    sideDistanceX = (mapX + 1.0 - rayPositionX) * deltaDistanceX

                if (rayDirectionY < 0):
                    stepY = -1
                    sideDistanceY = (rayPositionY - mapY) * deltaDistanceY

                else:
                    stepY = 1
                    sideDistanceY = (mapY + 1.0 - rayPositionY) * deltaDistanceY

                # Finding distance to a wall
                hit = 0
                while  (hit == 0):
                    if (sideDistanceX < sideDistanceY):
                        sideDistanceX += deltaDistanceX
                        mapX += stepX
                        side = 0
                        
                    else:
                        sideDistanceY += deltaDistanceY
                        mapY += stepY
                        side = 1
                        
                    if (worldMapf1[mapX][mapY] > 0):
                        hit = 1

                # Correction against fish eye effect
                try:
                    if (side == 0):
                        perpWallDistance = abs((mapX - rayPositionX + ( 1.0 - stepX ) / 2.0) / rayDirectionX)
                    else:
                        perpWallDistance = abs((mapY - rayPositionY + ( 1.0 - stepY ) / 2.0) / rayDirectionY)
                except:
                    perpWallDistance = 64

                # Calculating HEIGHT of the line to draw
                lineHEIGHT = abs(int(HEIGHT / (perpWallDistance+.0000001)))

                if worldMapf1[mapX][mapY] == 4 or worldMapf1[mapX][mapY] == 5 or worldMapf1[mapX][mapY] == 6:
                    drawStart = -lineHEIGHT / 2.0 + HEIGHT / 2.0
                    drawStart = 0
                else:
                    drawStart = -lineHEIGHT / 2.0 + HEIGHT / 2.0
                    drawStart = drawStart-(lineHEIGHT)

                # if drawStat < 0 it would draw outside the screen
                if (drawStart < 0):
                    drawStart = 0

                drawEnd = -lineHEIGHT / 2.0 + HEIGHT / 2.0

                if (drawEnd >= HEIGHT):
                    drawEnd = HEIGHT - 1

                # Wall colors 0 to 3
                wallcolors = [ [], [255,255,255], [204,204,204], [38,38,38], [255,255,255], [204,204,204], [38,38,38] ]
                color = wallcolors[ worldMapf1[mapX][mapY] ]

                # If side == 1 then ton the color down. Gives a "showShadow" an the wall.
                # Draws showShadow if showShadow is True
                if showShadow:
                    if side == 1:
                        for i,v in enumerate(color):
                            color[i] = int(v / 1.2)                    

                # Drawing the graphics
                if Antialiasing == 0:
                    #if worldMap[mapX][mapY] == 4:
                    #pygame.draw.line(screen, color, (column,0+((drawStart/4))), (column, drawEnd), 2)
                    #else:
                    pygame.draw.line(screen, color, (column,drawStart), (column, drawEnd), 2)
                else:
                    color[0]=int(color[0])
                    color[1]=int(color[1])
                    color[2]=int(color[2])
                    column=int(column)
                    drawStart=int(drawStart)
                    drawEnd=int(drawEnd)
                    #color[3]=round(color[3],0)
                    pygame.gfxdraw.line(screen,(column,drawStart),(column,drawEnd),color)
                column += 2
            while column < WIDTH and worldMapb1 != None:
                cameraX = 2.0 * column / WIDTH - 1.0
                rayPositionX = positionX
                rayPositionY = positionY
                rayDirectionX = directionX + planeX * cameraX
                rayDirectionY = directionY + planeY * cameraX + .000000000000001 # avoiding ZDE 

                # In what square is the ray?
                mapX = int(rayPositionX)
                mapY = int(rayPositionY)

                # Delta distance calculation
                # Delta = square ( raydir * raydir) / (raydir * raydir)
                deltaDistanceX = math.sqrt(1.0 + (rayDirectionY * rayDirectionY) / (rayDirectionX * rayDirectionX))
                deltaDistanceY = math.sqrt(1.0 + (rayDirectionX * rayDirectionX) / (rayDirectionY * rayDirectionY))

                # We need sideDistanceX and Y for distance calculation. Checks quadrant
                if (rayDirectionX < 0):
                    stepX = -1
                    sideDistanceX = (rayPositionX - mapX) * deltaDistanceX

                else:
                    stepX = 1
                    sideDistanceX = (mapX + 1.0 - rayPositionX) * deltaDistanceX

                if (rayDirectionY < 0):
                    stepY = -1
                    sideDistanceY = (rayPositionY - mapY) * deltaDistanceY

                else:
                    stepY = 1
                    sideDistanceY = (mapY + 1.0 - rayPositionY) * deltaDistanceY

                # Finding distance to a wall
                hit = 0
                while  (hit == 0):
                    if (sideDistanceX < sideDistanceY):
                        sideDistanceX += deltaDistanceX
                        mapX += stepX
                        side = 0
                        
                    else:
                        sideDistanceY += deltaDistanceY
                        mapY += stepY
                        side = 1
                        
                    if (worldMapb1[mapX][mapY] > 0):
                        hit = 1

                # Correction against fish eye effect
                try:
                    if (side == 0):
                        perpWallDistance = abs((mapX - rayPositionX + ( 1.0 - stepX ) / 2.0) / rayDirectionX)
                    else:
                        perpWallDistance = abs((mapY - rayPositionY + ( 1.0 - stepY ) / 2.0) / rayDirectionY)
                except:
                    perpWallDistance = 64

                # Calculating HEIGHT of the line to draw
                lineHEIGHT = abs(int(HEIGHT / (perpWallDistance+.0000001)))

                drawEnd = lineHEIGHT / 2.0 + HEIGHT / 2.0
                if worldMapb1[mapX][mapY] == 4 or worldMapb1[mapX][mapY] == 5 or worldMapb1[mapX][mapY] == 6:
                    drawStart = -lineHEIGHT / 2.0 + HEIGHT / 2.0
                    drawStart = 0
                else:
                    drawStart = -lineHEIGHT / 2.0 + HEIGHT / 2.0
                    drawStart = drawEnd+(lineHEIGHT)

                # if drawStat < 0 it would draw outside the screen
                if (drawStart < 0):
                    drawStart = 0

                if (drawEnd >= HEIGHT):
                    drawEnd = HEIGHT - 1

                # Wall colors 0 to 3
                wallcolors = [ [], [255,255,255], [204,204,204], [38,38,38], [255,255,255], [204,204,204], [38,38,38] ]
                color = wallcolors[ worldMapb1[mapX][mapY] ]

                # If side == 1 then ton the color down. Gives a "showShadow" an the wall.
                # Draws showShadow if showShadow is True
                if showShadow:
                    if side == 1:
                        for i,v in enumerate(color):
                            color[i] = int(v / 1.2)                    

                # Drawing the graphics
                if Antialiasing == 0:
                    #if worldMap[mapX][mapY] == 4:
                    #pygame.draw.line(screen, color, (column,0+((drawStart/4))), (column, drawEnd), 2)
                    #else:
                    pygame.draw.line(screen, color, (column,drawStart), (column, drawEnd), 2)
                else:
                    color[0]=int(color[0])
                    color[1]=int(color[1])
                    color[2]=int(color[2])
                    column=int(column)
                    drawStart=int(drawStart)
                    drawEnd=int(drawEnd)
                    #color[3]=round(color[3],0)
                    pygame.gfxdraw.line(screen,(column,drawStart),(column,drawEnd),color)
                column += 2
        
        column = 0
        while column < WIDTH:
            cameraX = 2.0 * column / WIDTH - 1.0
            rayPositionX = positionX
            rayPositionY = positionY
            rayDirectionX = directionX + planeX * cameraX
            rayDirectionY = directionY + planeY * cameraX + .000000000000001 # avoiding ZDE 

            # In what square is the ray?
            mapX = int(rayPositionX)
            mapY = int(rayPositionY)

            # Delta distance calculation
            # Delta = square ( raydir * raydir) / (raydir * raydir)
            try:
                deltaDistanceX = math.sqrt(1.0 + (rayDirectionY * rayDirectionY) / (rayDirectionX * rayDirectionX))
                deltaDistanceY = math.sqrt(1.0 + (rayDirectionX * rayDirectionX) / (rayDirectionY * rayDirectionY))
            except:
                deltaDistanceX = 64
                deltaDistanceY = 64
                print("Bad")

            if BadMath == 1:
                    deltaDistanceX=int(deltaDistanceX)
                    deltaDistanceY=int(deltaDistanceY)
                    rayPositionX=round(rayPositionX,4)
                    rayPositionY=round(rayPositionY,4)
                    rayDirectionX=round(rayDirectionX,4)
                    rayDirectionY=round(rayDirectionY,4)

            # We need sideDistanceX and Y for distance calculation. Checks quadrant
            if (rayDirectionX < 0):
                stepX = -1
                sideDistanceX = (rayPositionX - mapX) * deltaDistanceX

            else:
                stepX = 1
                sideDistanceX = (mapX + 1.0 - rayPositionX) * deltaDistanceX

            if (rayDirectionY < 0):
                stepY = -1
                sideDistanceY = (rayPositionY - mapY) * deltaDistanceY

            else:
                stepY = 1
                sideDistanceY = (mapY + 1.0 - rayPositionY) * deltaDistanceY

            # Finding distance to a wall
            hit = 0
            while  (hit == 0):
                if (sideDistanceX < sideDistanceY):
                    sideDistanceX += deltaDistanceX
                    mapX += stepX
                    side = 0
                    
                else:
                    sideDistanceY += deltaDistanceY
                    mapY += stepY
                    side = 1
                    
                if (worldMap[mapX][mapY] > 0):
                    hit = 1

            # Correction against fish eye effect
            try:
                if (side == 0):
                    perpWallDistance = abs((mapX - rayPositionX + ( 1.0 - stepX ) / 2.0) / rayDirectionX)
                else:
                    perpWallDistance = abs((mapY - rayPositionY + ( 1.0 - stepY ) / 2.0) / rayDirectionY)
            except:
                perpWallDistance = 64

            if BadMath == 1:
                    perpWallDistance=round(perpWallDistance,1)

            # Calculating HEIGHT of the line to draw
            if BadMath == 1:
                lineHEIGHT = round(abs(int(HEIGHT / (perpWallDistance+.0000001))),0)
            else:
                lineHEIGHT = abs(int(HEIGHT / (perpWallDistance+.0000001)))
            if worldMap[mapX][mapY] == 4 or worldMap[mapX][mapY] == 5 or worldMap[mapX][mapY] == 6:
                drawStart = -lineHEIGHT / 2.0 + HEIGHT / 2.0
                drawStart = 0
            else:
                drawStart = -lineHEIGHT / 2.0 + HEIGHT / 2.0

            # if drawStat < 0 it would draw outside the screen
            if (drawStart < 0):
                drawStart = 0

            drawEnd = lineHEIGHT / 2.0 + HEIGHT / 2.0

            if (drawEnd >= HEIGHT):
                drawEnd = HEIGHT - 1

            # Wall colors 0 to 3
            wallcolors = [ [], [255,255,255], [204,204,204], [38,38,38], [255,255,255], [204,204,204], [38,38,38] ]
            color = wallcolors[ worldMap[mapX][mapY] ]

            # If side == 1 then ton the color down. Gives a "showShadow" an the wall.
            # Draws showShadow if showShadow is True
            if showShadow:
                if side == 1:
                    for i,v in enumerate(color):
                        color[i] = int(v / 1.2)                    

            # Drawing the graphics
            if Antialiasing == 0:
                #if worldMap[mapX][mapY] == 4:
                #pygame.draw.line(screen, color, (column,0+((drawStart/4))), (column, drawEnd), 2)
                #else:
                if BadMath == 1:
                    pygame.draw.line(screen, color, (column,drawStart), (round(column,0), drawEnd), 2)
                else:
                    pygame.draw.line(screen, color, (column,drawStart), (column, drawEnd), 2)
            else:
                color[0]=int(color[0])
                color[1]=int(color[1])
                color[2]=int(color[2])
                column=int(column)
                drawStart=int(drawStart)
                drawEnd=int(drawEnd)
                #color[3]=round(color[3],0)
                if BadMath == 1:
                    pygame.gfxdraw.line(screen,(column,drawStart),(column,drawEnd),color)
                else:
                    pygame.gfxdraw.line(screen,(column,drawStart),(column,drawEnd),color)

            PosXDec=0
            
            #TSLoad
            if worldMap[mapX][mapY] == 1 or worldMap[mapX][mapY] == 2 or worldMap[mapX][mapY] == 3:

                if worldMap[mapX][mapY] == 1:
                    TSprite = Wall1
                elif worldMap[mapX][mapY] == 2:
                    TSprite = Wall2
                elif worldMap[mapX][mapY] == 3:
                    TSprite = Wall3

                if LSide != side:
                    TexXA=0

                PixDec=LXDec-PosXDec
                if side == 0:
                    WallXHit=positionY + perpWallDistance * rayDirectionY
                else:
                    WallXHit=positionX + perpWallDistance * rayDirectionX
                #rayPositionX
                #WallXDec = float(str(rayPositionX-int(rayPositionX)).split('.')[1])
                WallXDec = float(str(WallXHit)[:str(WallXHit).find(".")])-WallXHit
                #print(WallXDec)
                
                #texXA=WallXHit * 15
                #if side == 0 and rayDirectionX > 0:
                #    texXA=15 - texXA - 1
                #if side == 1 and rayDirectionY < 0:
                #    texXA=15 - texXA - 1
                #if TexXA > 15:
                #    TexXA=0

                #if LMapX != mapX:
                #    TexXA=0

                #if LMapY != mapY:
                #    TexXA=0

                if BetterTex == 0:
                    if BadMath == 1:
                        TexXA=TexXA+((round(WallXHit,0)/WIDTH)/(round(lineHEIGHT,0)/HEIGHT))*3
                    else:
                        TexXA=TexXA+((WallXHit/WIDTH)/(lineHEIGHT/HEIGHT))*3.25
                else:
                    if BadMath == 1:
                        TexXA=round(((WallXDec)/0.0625),0)
                    else:
                        TexXA=round(((WallXDec)/0.0625),0)
                    #print(TexXA)
                if TexXA>15:
                    TexXA=0
                TexX=TexXA
                    #print(PosXDec)
                #for i in range(0,15,1):
                #    pygame.draw.line(screen, TSprite.getpixel((0,i)),(column,drawStart), (column, (drawStart+(lineHEIGHT/16)*(i+1))), 2)
                if BadMath == 1:
                    pygame.draw.line(screen, TSprite.getpixel((TexX,15)), (column,round(drawStart,0)), (column, (round(drawStart+(lineHEIGHT/16)*16,0))), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,14)), (column,round(drawStart,0)), (column, (round(drawStart+(lineHEIGHT/16)*15,0))), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,13)), (column,round(drawStart,0)), (column, (round(drawStart+(lineHEIGHT/16)*14,0))), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,12)), (column,round(drawStart,0)), (column, (round(drawStart+(lineHEIGHT/16)*13,0))), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,11)), (column,round(drawStart,0)), (column, (round(drawStart+(lineHEIGHT/16)*12,0))), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,10)), (column,round(drawStart,0)), (column, (round(drawStart+(lineHEIGHT/16)*11,0))), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,9)), (column,round(drawStart,0)), (column, (round(drawStart+(lineHEIGHT/16)*10,0))), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,8)), (column,round(drawStart,0)), (column, (round(drawStart+(lineHEIGHT/16)*9,0))), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,7)), (column,round(drawStart,0)), (column, (round(drawStart+(lineHEIGHT/16)*8,0))), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,6)), (column,round(drawStart,0)), (column, (round(drawStart+(lineHEIGHT/16)*7,0))), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,5)), (column,round(drawStart,0)), (column, (round(drawStart+(lineHEIGHT/16)*6,0))), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,4)), (column,round(drawStart,0)), (column, (round(drawStart+(lineHEIGHT/16)*5,0))), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,3)), (column,round(drawStart,0)), (column, (round(drawStart+(lineHEIGHT/16)*4,0))), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,2)), (column,round(drawStart,0)), (column, (round(drawStart+(lineHEIGHT/16)*3,0))), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,1)), (column,round(drawStart,0)), (column, (round(drawStart+(lineHEIGHT/16)*2,0))), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,0)), (column,round(drawStart,0)), (column, (round(drawStart+(lineHEIGHT/16)*1,0))), 2)
                else:
                    pygame.draw.line(screen, TSprite.getpixel((TexX,15)), (column,drawStart), (column, (drawStart+(lineHEIGHT/16)*16)), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,14)), (column,drawStart), (column, (drawStart+(lineHEIGHT/16)*15)), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,13)), (column,drawStart), (column, (drawStart+(lineHEIGHT/16)*14)), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,12)), (column,drawStart), (column, (drawStart+(lineHEIGHT/16)*13)), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,11)), (column,drawStart), (column, (drawStart+(lineHEIGHT/16)*12)), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,10)), (column,drawStart), (column, (drawStart+(lineHEIGHT/16)*11)), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,9)), (column,drawStart), (column, (drawStart+(lineHEIGHT/16)*10)), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,8)), (column,drawStart), (column, (drawStart+(lineHEIGHT/16)*9)), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,7)), (column,drawStart), (column, (drawStart+(lineHEIGHT/16)*8)), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,6)), (column,drawStart), (column, (drawStart+(lineHEIGHT/16)*7)), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,5)), (column,drawStart), (column, (drawStart+(lineHEIGHT/16)*6)), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,4)), (column,drawStart), (column, (drawStart+(lineHEIGHT/16)*5)), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,3)), (column,drawStart), (column, (drawStart+(lineHEIGHT/16)*4)), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,2)), (column,drawStart), (column, (drawStart+(lineHEIGHT/16)*3)), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,1)), (column,drawStart), (column, (drawStart+(lineHEIGHT/16)*2)), 2)
                    pygame.draw.line(screen, TSprite.getpixel((TexX,0)), (column,drawStart), (column, (drawStart+(lineHEIGHT/16)*1)), 2)
            else:
                TexX=0
                TexXA=0
            LSide=side
            LXDec=PosXDec
            LMapX=mapX
            LMapY=mapY
            LType=worldMap[mapX][mapY]
            column += 2
        #DrawSecondFloor

        # Drawing HUD if showHUD is True

        # Updating display
        if Upscale == 1:
            BScreen=pygame.transform.scale(screen, (OutW,OutH))

            screenR.blit(BScreen, (0, 0))

            if showHUD:
                pygame.draw.rect(screenR, (100,100,200), (0, OutH-40, OutW, 40))
                screenR.blit(HUD, (20,OutH-30))
            pygame.event.pump()
            pygame.display.flip()
        else:
            if showHUD:
                pygame.draw.rect(screen, (100,100,200), (0, HEIGHT-40, WIDTH, 40))
                screen.blit(HUD, (20,HEIGHT-30))
            
            pygame.event.pump()
            pygame.display.flip()

        if not time.time()-LTime>0.99:
            frames=frames+1
        else:
            HUD = font.render("FPS:"+str(fps)+" F1 / F2 - Screenshot JPEG/BMP   F5/F6 - Shadows on/off   F7/F8 - HUD Show/Hide "+str(round(positionX,1))+","+str(round(positionY,1)), True, (0,0,0))
            fps=frames
            LTime=time.time()
            frames=0
        #Clock.tick(24)
       
main()

import pygame 

#assigning colors
darkmode = "n"
if "y" in darkmode:
    BLACK = (255, 255, 255)
    WHITE = (0, 0, 0)
    GREEN = (255, 0, 255)
    RED = (0, 255, 255)
    BLUE = (255,255,0)
else:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0,255,0)

#column and row size for grid
amtrow =9
amtcol =9

HEIGHT = 75
WIDTH = 75
MARGIN = 5

#colour  for player's turn
playcolour = [25, 250, 100]

#creating grid
grid = []
TotalGrid = []

#creating total grid size
totxsize = ((WIDTH + MARGIN) * amtrow)+5*MARGIN
totysize = ((HEIGHT + MARGIN) * amtcol)+5*MARGIN

#formatting **********************************
def ResizePlayBox(playrect,allowedx,allowedy):
    if allowedx == -1 and allowedy == -1:
        playrect[0] = MARGIN
        playrect[1] = MARGIN
        playrect[2] = (3*WIDTH + 4*MARGIN)*3
        playrect[3] = (3*HEIGHT + 4*MARGIN)*3
    else:

        playrect[1]=allowedy*(MARGIN+HEIGHT) + 2*MARGIN + ((allowedy//3 -1)*MARGIN)
        playrect[0]=allowedx*(MARGIN+WIDTH) + 2*MARGIN + ((allowedx//3 -1) *MARGIN)
        playrect[2]=(MARGIN+WIDTH)*3 + MARGIN
        playrect[3]=(MARGIN+HEIGHT)*3 + MARGIN

#determining next box in game play
def NextBox(Ccords,TotalGrid):
    boxFull = False
    if TotalGrid[Ccords[0]%3][Ccords[1]%3] != 0:
        return (-1,-1)
    else:
        return((Ccords[0]%3)*3,(Ccords[1]%3)*3)

#Determineinga winner        
def SetWin(Grid,Team,TotalGrid):
    #for three in a row
    for x in range(amtrow):
        for y in range(amtcol):
            Grid[x][y] = Team
    #for three matching "x" or "y"
    for x in TotalGrid:
        for y in x:
            y = Team
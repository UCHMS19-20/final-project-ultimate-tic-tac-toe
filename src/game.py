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

#formatting to create the major box
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
    #ccords are the individual small squares
    #here they are divided up
    if TotalGrid[Ccords[0]%3][Ccords[1]%3] != 0:
        return (-1,-1)
    else:
        return((Ccords[0]%3)*3,(Ccords[1]%3)*3)

#Determining a winner        
def SetWin(Grid,Team,TotalGrid):
    #for three in a row
    for x in range(amtrow):
        for y in range(amtcol):
            Grid[x][y] = Team
    #for three matching "x" or "y"
    for x in TotalGrid:
        for y in x:
            y = Team

#Winner of a set
def winSetter(OC,Team,Grid,TotalGrid):
    TotalGrid[OC[0]//3][OC[1]//3] = Team
    for x in range((OC[0]//3) * 3,(OC[0]//3) *3 + 3):
        for y in range((OC[1]//3) * 3,(OC[1]//3) *3 + 3):
            grid[x][y] = Team
    #when win is detected in individual box set for x team
    for x in range(0,3):
        if TotalGrid[x][0] == Team and TotalGrid[x][1] == Team and TotalGrid[x][2] == Team:
            print("Win detected on",x)
            if Team == 1:
                SetWin(Grid,1,TotalGrid)
            else:
                SetWin(Grid,2,TotalGrid)
    #when win is detected in individual box set for y team
    for y in range(0,3):
        if TotalGrid[0][y] == Team and TotalGrid[1][y] == Team and TotalGrid[2][y] == Team:
            print("Win detected on ",y)
            if Team == 1:
                SetWin(Grid,1,TotalGrid)
            else:
                SetWin(Grid,2,TotalGrid)
    #when a winner is detected in the entire grid
    if (TotalGrid[0][0] ==Team and TotalGrid[1][1] == Team and TotalGrid[2][2] == Team) or (TotalGrid[2][0] == Team and TotalGrid[1][1] == Team and TotalGrid[0][2] == Team ):
        print("Win here detected")
        if Team == 1:
            SetWin(Grid,1,TotalGrid)
        else:
            SetWin(Grid,2,TotalGrid)
    print(TotalGrid)

def winCalc(OuterCords,Grid,TotalGrid):
    #the major outside boxes
    OC = OuterCords
    #the small inner boxes
    IC = (OC[0]%3,OC[1]%3)
    thisTileTeam = Grid[OC[0]][OC[1]]
    Team = thisTileTeam
    if thisTileTeam == 0:
        return "Invaild Team"
    if IC == (0,0):
        #determines if the win is made in one of the major outside boxes
        #it will execute the defined winSetter above
        if Grid[OC[0]+1][OC[1]] == thisTileTeam and Grid[OC[0]+2][OC[1]] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
        elif Grid[OC[0]][OC[1]+1] == thisTileTeam and Grid[OC[0]][OC[1]+2] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
        elif Grid[OC[0]+1][OC[1]+1] == thisTileTeam and Grid[OC[0]+2][OC[1]+2] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
    elif IC == (1,0):
        #similar to what's above except this is in reference to the small boxes
        if Grid[OC[0]+1][OC[1]] == thisTileTeam and Grid[OC[0]-1][OC[1]] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
        elif Grid[OC[0]][OC[1]+1] == thisTileTeam and Grid[OC[0]][OC[1]+2] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
    elif IC == (2,0):
        if Grid[OC[0]-1][OC[1]] == thisTileTeam and Grid[OC[0]-2][OC[1]] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
        elif Grid[OC[0]][OC[1]+1] == thisTileTeam and Grid[OC[0]][OC[1]+2] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
        elif Grid[OC[0]-1][OC[1]+1] == thisTileTeam and Grid[OC[0]-2][OC[1]+2] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
    elif IC == (0,1):
        if Grid[OC[0]][OC[1]+1] == thisTileTeam and Grid[OC[0]][OC[1]-1] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
        elif Grid[OC[0]+1][OC[1]] == thisTileTeam and Grid[OC[0]+2][OC[1]] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
    elif IC == (1,1):
        if Grid[OC[0]][OC[1]+1] == thisTileTeam and Grid[OC[0]][OC[1]-1] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
        elif Grid[OC[0]+1][OC[1]] == thisTileTeam and Grid[OC[0]-1][OC[1]] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
        elif Grid[OC[0]-1][OC[1]-1] == thisTileTeam and Grid[OC[0]+1][OC[1]+1] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
        elif Grid[OC[0]-1][OC[1]+1] == thisTileTeam and Grid[OC[0]+1][OC[1]-1] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)

    elif IC == (2,1):
        if Grid[OC[0]][OC[1]+1] == thisTileTeam and Grid[OC[0]][OC[1]-1] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
        elif Grid[OC[0]-1][OC[1]] == thisTileTeam and Grid[OC[0]-2][OC[1]] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)

    elif IC == (0,2):
        if Grid[OC[0]+1][OC[1]] == thisTileTeam and Grid[OC[0]+2][OC[1]] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
        elif Grid[OC[0]][OC[1]-1] == thisTileTeam and Grid[OC[0]][OC[1]-2] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
        elif Grid[OC[0]+1][OC[1]-1] == thisTileTeam and Grid[OC[0]+2][OC[1]-2] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
    elif IC == (1,2):
        if Grid[OC[0]+1][OC[1]] == thisTileTeam and Grid[OC[0]-1][OC[1]] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
        elif Grid[OC[0]][OC[1]-1] == thisTileTeam and Grid[OC[0]][OC[1]-2] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)

    elif IC == (2,2):
        if (Grid[OC[0]][OC[1]-1] == thisTileTeam and Grid[OC[0]][OC[1]-2] == thisTileTeam) :
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
        elif (Grid[OC[0]-1][OC[1]] == thisTileTeam and Grid[OC[0]-2][OC[1]] == thisTileTeam):
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
        elif Grid[OC[0]-1][OC[1]-1] == thisTileTeam and Grid[OC[0]-2][OC[1]-2] == thisTileTeam:
            winSetter(OC,thisTileTeam,Grid,TotalGrid)
    amtused = 0
    #print(OC[0],IC[0],OC[1],IC[1])
    for x in range(OC[0]-IC[0],OC[0]-IC[0]+3):
        for y in range(OC[1]-IC[1],OC[1]-IC[1]+3):
            if Grid[x][y] != 0:
                amtused = amtused + 1
    if amtused == 9:
        if TotalGrid[OC[0]//3][OC[1]//3] == 0:
            TotalGrid[OC[0]//3][OC[1]//3] = -1
            print("Box tied!!")
    #print(TiedBox)
for row in range(3):

    TotalGrid.append([])
    for column in range(3):
        TotalGrid[row].append(0)
for row in range(amtrow):

    grid.append([])
    for column in range(amtcol):
        grid[row].append(0)

#prints game
print(grid)
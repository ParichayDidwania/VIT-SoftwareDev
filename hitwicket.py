
Characters=['P1','P2','P3','P4','P5','H1','H2','H3']
selected=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

alive=[5,5]

Moveset = {
    'A-PL':[0,-1],
    'A-PR':[0,1],
    'A-PF':[-1,0],
    'A-PB':[1,0],

    'B-PL':[0,1],
    'B-PR':[0,-1],
    'B-PF':[1,0],
    'B-PB':[-1,0],

    'A-H1L':[0,-2],
    'A-H1R':[0,2],
    'A-H1F':[-2,0],
    'A-H1B':[2,0],

    'B-H1L':[0,2],
    'B-H1R':[0,-2],
    'B-H1F':[2,0],
    'B-H1B':[-2,0],

    'A-H2FL':[-2,-2],
    'A-H2FR':[-2,2],
    'A-H2BL':[2,-2],
    'A-H2BR':[2,2],

    'B-H2FL':[2,2],
    'B-H2FR':[2,-2],
    'B-H2BL':[-2,2],
    'B-H2BR':[-2,-2],

    'A-H3FL':[-2,-1],
    'A-H3FR':[-2,1],
    'A-H3BL':[2,-1],
    'A-H3BR':[2,-1],

    'A-H3LF':[1,-2],
    'A-H3LB':[-1,-2],
    'A-H3RF':[1,2],
    'A-H3RB':[-1,2],

    'B-H3FL':[2,1],
    'B-H3FR':[2,-1],
    'B-H3BL':[-2,1],
    'B-H3BR':[-2,1],

    'B-H3LF':[-1,2],
    'B-H3LB':[1,2],
    'B-H3RF':[-1,-2],
    'B-H3RB':[1,-2],
    
}

CharToIndex = {
    'P1':0,
    'P2':1,
    'P3':2,
    'P4':3,
    'P5':4,
    'H1':5,
    'H2':6,
    'H3':7
}


characterselectionCompleted_1=0
characterselectionCompleted_2=0

pawn = ['L','R','F','B']
H2=['FL','FR','BL','BR']
H3=['FL','FR','BL','BR','RF','RB','LF','LB']
turn=0
board=[]
n=5
for i in range(5):
    m=[]
    for j in range(5):
        m.append(0)
    board.append(m)

def getAtPos(i,j,x,y,name,character):

    if(character=='P'):
        z = board[x][y]
        z=str(z)
        name = name.split("-")[0]
        z = z.split("-")[0]
        if(z=='0'):
            return [0]
        elif(name==z):
            return [-1]
        elif(name!=z):
            return [1]
    elif(character=="H1"):
        midx = (i+x)//2
        midy = (j+y)//2

        result=[0,0]

        z = board[midx][midy]
        z=str(z)
        name = name.split("-")[0]
        z = z.split("-")[0]

        if(z=='0'):
            result[0] = 0
        elif(name==z):
            result[0] = -1
        elif(name!=z):
            result[0] = 1

        z = board[x][y]
        z=str(z)
        name = name.split("-")[0]
        z = z.split("-")[0]

        if(z=='0'):
            result[1] = 0
        elif(name==z):
            result[1] = -1
        elif(name!=z):
            result[1] = 1
        return result
    return []
        
    

def getCharacterPos(x):
    for i in range(n):
        for j in range(n):
            if(board[i][j]==x):
                return i,j
    return -1,-1

def display():
    print("\n")
    for i in range(n):
        for j in range(n):
            if(board[i][j]==0):
                print('-',end="\t")
            else:
                print(board[i][j],end="\t")
        print("\n")

def characterSelection(x,y):
    x = x.split(",")
    if(len(x)>5):
        return False,"You can only select 5 Characters"
    for i in x:
        try:
            z = Characters.index(i)
            if(selected[y][z]==0):
                selected[y][z]+=1
            else:
                return False,"Cannot reselect the characters"
        except:
            return False,"Character does not exist"
    return True,"Ok"

def checkMove(x,y,name):
    x = x.split(':')
    if(x[0] not in Characters):
        return False,"Character is Invalid"
    if(selected[y][CharToIndex[x[0]]]==0):
        return False,"Character is Dead"
    if(x[0][0]=='P' or x[0]=='H1'):
        if(x[1] not in pawn):
            return False,"Invalid Move"
    if(x[0]=='H2'):
        if(x[1] not in H2):
            return False,"Invalid Move"
    if(x[0]=='H3'):
        if(x[1] not in H3):
            return False,"Invalid Move"

    searchStr = name+x[0]
    i,j = getCharacterPos(searchStr)
    if(x[0][0]=='P'):
        z = Moveset[name+x[0][0]+x[1]]
    elif(x[0]=='H1' or x[0]=='H2' or x[0]=='H3'):
        z = Moveset[name+x[0]+x[1]]        

    newcord_x = i+z[0]
    newcord_y = j+z[1]

    if(newcord_x>=n or newcord_x<0 or newcord_y>=n or newcord_y<0):
        return False,"Invalid Move"
    if(x[0][0]=='P' or x[0]=='H3'):
        result = getAtPos(i,j,newcord_x,newcord_y,name,'P')
    elif(x[0]=='H1' or x[0]=='H2'):
        result = getAtPos(i,j,newcord_x,newcord_y,name,'H1')

    if(len(result)==1):
        if(result[0]==-1):
            return False,"Own Character at the position"
        elif(result[0]==1):
            opponent_char = board[newcord_x][newcord_y]
            opponent_char = str(opponent_char)
            opponent_char = opponent_char.split("-")[1]
            selected[(y+1)%2][CharToIndex[opponent_char]]=0
            alive[(y+1)%2]+=-1
            board[newcord_x][newcord_y] = searchStr
            board[i][j]=0
            return True,"Killed opponent"
        elif(result[0]==0):
            board[i][j]=0
            board[newcord_x][newcord_y] = searchStr
            return True,"Moved"
    else:
        print(result)
        print("***********")
        midx = (i+newcord_x)//2
        midy = (j+newcord_y)//2
        if(result[0]==-1 or result[1]==-1):
            return False,"Own Character at the position"
        elif(result[0]==1 and result[1]==1):
            
            board[i][j]=0

            opponent_char = board[midx][midy]
            opponent_char = str(opponent_char)
            opponent_char = opponent_char.split("-")[1]
            selected[(y+1)%2][CharToIndex[opponent_char]]=0
            alive[(y+1)%2]+=-1
            board[midx][midy]=0

            opponent_char = board[newcord_x][newcord_y]
            opponent_char = str(opponent_char)
            opponent_char = opponent_char.split("-")[1]
            selected[(y+1)%2][CharToIndex[opponent_char]]=0
            alive[(y+1)%2]+=-1

            board[newcord_x][newcord_y] = searchStr

            return True,"Killed opponent"

        elif(result[0]==1 and result[1]==0):

            board[i][j]=0

            opponent_char = board[midx][midy]
            opponent_char = str(opponent_char)
            opponent_char = opponent_char.split("-")[1]
            selected[(y+1)%2][CharToIndex[opponent_char]]=0
            alive[(y+1)%2]+=-1
            board[midx][midy] = 0

            board[newcord_x][newcord_y] = searchStr
            return True,"Killed opponent"


        elif(result[0]==0 and result[1]==1):
            board[i][j]=0
            opponent_char = board[newcord_x][newcord_y]
            opponent_char = str(opponent_char)
            opponent_char = opponent_char.split("-")[1]
            selected[(y+1)%2][CharToIndex[opponent_char]]=0
            alive[(y+1)%2]+=-1

            board[newcord_x][newcord_y] = searchStr 
            return True,"Killed opponent"
        else:
            board[i][j]=0
            board[newcord_x][newcord_y] = searchStr
            return True,"Moved"

            

while(characterselectionCompleted_1==0):
    print("Player 1 Enter the order : \n")
    x = input()
    result,msg = characterSelection(x,0)
    if(result==False):
        print("Try Again\n")
    else:
        x = x.split(',')
        for i in range(0,5):
            board[n-1][i]='A-'+x[i]
        display()
        characterselectionCompleted_1=1

while(characterselectionCompleted_2==0):
    print("\nPlayer 2 Enter the order : \n")
    x = input()
    result,msg = characterSelection(x,1)
    if(result==False):
        print("Try Again\n")
    else:
        x = x.split(',')
        for i in range(0,5):
            board[0][i]='B-'+x[i]
        display()
        characterselectionCompleted_2=1


if(characterselectionCompleted_1==1 and characterselectionCompleted_2==1):
    while(alive[0]!=0 or alive[1]!=0):
        if(turn==0):
            print("Player 1 Move : ")
            x = input()
            result,msg = checkMove(x,0,'A-')
            if(result==False):
                print(msg)
                print("\nTry Again\n")
            else:
                display()
                turn=(turn+1)%2
        else:
            print("Player 2 Move : ")
            x = input()
            result,msg = checkMove(x,1,'B-')
            if(result==False):
                print(msg)
                print("\nTry Again\n")
            else:
                display()
                turn=(turn+1)%2
if(alive[0]==0):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
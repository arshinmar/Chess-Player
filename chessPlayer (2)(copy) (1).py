from timeit import default_timer as timer

class Tree:
        def __init__(self,root):
                self.store=[root,[]]
        def AddSuccessor(self,root):
                self.store[1]+=[root]
                return True
        def GetLevelOrder(self):
                accum=[]
                x=Queue()
                x.push(self.store)
                while x.empty()==False:
                        y=x.dequeue()
                        accum+=[y[0]]
                        for i in y:
                                x.enqueue(i)
                return accum
        def GetSuccessor(self):
                return self.store[1]

class Queue:
        def __init__(self):
                self.store=[]
        def push(self,root):
                self.store+=[root]
                return True
        def empty(self):
                if self.store==[]:
                        return True
        def pop(self):
                if self.store!=[]:
                        val=self.store[0]
                        self.store=self.store[1:len(self.store)]
                else:
                        return False
    
def max(a,b):
        if a>b:
                return a
        else:
                return b

def min(a,b):
        if a<b:
                return a
        else:
                return b

def ChessPlayer(board,player):
        y=GetPlayerMoves(board,player)
        if GameOver(board,10)==True or GameOver(board,20)==True or y==[]:
                return [False,[],[],None]
        else:
                B=FindBestMove(board,player,5)
                blah=MainEval(board,player)
                blah2=MainSort(blah)
                x=Tree(board)
                for i in blah2:
                        x.AddSuccessor(i)
                x.GetLevelOrder()
                return [True,B,blah,x]

def MainEval(board,player):
        y=GetPlayerMoves(board,player)
        blah=[]
        x=[]
        for d in y:
                board2=list(board)
                Move(board2,d[0],d[1],player)
                temp=[d]+[float(EvaluateBoard(board2))]
                blah+=[temp]
        return blah

def MainSort(blah):
        accum=[]
        for i in blah:
                accum+=[i[1]]
        accum=BubbleSort(accum)
        x=list(blah)
        temp=[]
        counter=0
        while len(temp)!=len(accum):
                for i in x:
                        if i[1]==accum[counter]:
                                temp+=[i]
                                counter+=1
        return temp
    
def BubbleSort(x):
        y=list(x)
        a=len(y)
        for i in range(0,a,1):
                for j in range(0,a-i-1,1):
                        if y[j]>y[j+1]:
                                y[j],y[j+1]=y[j+1],y[j]
        return y

def initialization():
        chessboard=[]
        for i in range(0,4,1):
                chessboard+=[0,0,0,0,0,0,0,0]
                chessboard+=[0,0,0,0,0,0,0,0]
        print(chessboard)
        original=list(chessboard)
        chessboard[0:8]=[13,11,12,15,14,12,11,13]
        chessboard[8:16]=[10,10,10,10,10,10,10,10]
        chessboard[48:56]=[20,20,20,20,20,20,20,20]
        chessboard[56:64]=[23,21,22,25,24,22,21,23]
        emptyboard=0
        return chessboard

def PrintIndexes():
        board=['00','01','02','03','04','05','06','07','08','09']
        for i in range(10,64,1):
                board+=[i]
        return PrintBoard(board)
def PrintBoard(main):
        board=list(main)
        for i in range(0,len(board),1):
                if board[i]==0:
                        board[i]="OO"
        row7="  "+str(board[63])+"  "+"|"+"  "+str(board[62])+"  "+"|"+"  "+str(board[61])+"  "+"|"+"  "+str(board[60])+"  "+"|"+"  "+str(board[59])+"  "+"|"+"  "+str(board[58])+"  "+"|"+"  "+str(board[57])+"  "+"|"+"  "+str(board[56])+"  "+"|"+"  "
        row6="  "+str(board[55])+"  "+"|"+"  "+str(board[54])+"  "+"|"+"  "+str(board[53])+"  "+"|"+"  "+str(board[52])+"  "+"|"+"  "+str(board[51])+"  "+"|"+"  "+str(board[50])+"  "+"|"+"  "+str(board[49])+"  "+"|"+"  "+str(board[48])+"  "+"|"+"  "
        row5="  "+str(board[47])+"  "+"|"+"  "+str(board[46])+"  "+"|"+"  "+str(board[45])+"  "+"|"+"  "+str(board[44])+"  "+"|"+"  "+str(board[43])+"  "+"|"+"  "+str(board[42])+"  "+"|"+"  "+str(board[41])+"  "+"|"+"  "+str(board[40])+"  "+"|"+"  "
        row4="  "+str(board[39])+"  "+"|"+"  "+str(board[38])+"  "+"|"+"  "+str(board[37])+"  "+"|"+"  "+str(board[36])+"  "+"|"+"  "+str(board[35])+"  "+"|"+"  "+str(board[34])+"  "+"|"+"  "+str(board[33])+"  "+"|"+"  "+str(board[32])+"  "+"|"+"  "
        row3="  "+str(board[31])+"  "+"|"+"  "+str(board[30])+"  "+"|"+"  "+str(board[29])+"  "+"|"+"  "+str(board[28])+"  "+"|"+"  "+str(board[27])+"  "+"|"+"  "+str(board[26])+"  "+"|"+"  "+str(board[25])+"  "+"|"+"  "+str(board[24])+"  "+"|"+"  "
        row2="  "+str(board[23])+"  "+"|"+"  "+str(board[22])+"  "+"|"+"  "+str(board[21])+"  "+"|"+"  "+str(board[20])+"  "+"|"+"  "+str(board[19])+"  "+"|"+"  "+str(board[18])+"  "+"|"+"  "+str(board[17])+"  "+"|"+"  "+str(board[16])+"  "+"|"+"  "
        row1="  "+str(board[15])+"  "+"|"+"  "+str(board[14])+"  "+"|"+"  "+str(board[13])+"  "+"|"+"  "+str(board[12])+"  "+"|"+"  "+str(board[11])+"  "+"|"+"  "+str(board[10])+"  "+"|"+"  "+str(board[9])+"  "+"|"+"  "+str(board[8])+"  "+"|"+"  "
        row0="  "+str(board[7])+"  "+"|"+"  "+str(board[6])+"  "+"|"+"  "+str(board[5])+"  "+"|"+"  "+str(board[4])+"  "+"|"+"  "+str(board[3])+"  "+"|"+"  "+str(board[2])+"  "+"|"+"  "+str(board[1])+"  "+"|"+"  "+str(board[0])+"  "+"|"+"  "
        linechange="------|------|------|------|------|------|------|------|"
        print(row7)
        print(linechange)
        print(row6)
        print(linechange)
        print(row5)
        print(linechange)
        print(row4)
        print(linechange)
        print(row3)
        print(linechange)
        print(row2)
        print(linechange)
        print(row1)
        print(linechange)
        print(row0)
        print(linechange)
        return True

def Edge(position):
        for i in [56,57,58,59,60,61,62,63]+[0,1,2,3,4,5,6,7]+[0,8,16,24,32,40,48,56]+[7,15,23,31,39,47,55,63]:
                if i==position:
                        return True
        return False

def TopEdge(position):
        for i in [56,57,58,59,60,61,62,63]:
                if i==position:
                        return True
        return False

def BottomEdge(position):
        for i in [0,1,2,3,4,5,6,7]:
                if i==position:
                        return True
        return False

def RightEdge(position):
        for i in [0,8,16,24,32,40,48,56]:
                if i==position:
                        return True
        return False

def LeftEdge(position):
        for i in [7,15,23,31,39,47,55,63]:
                if i==position:
                        return True
        return False

def UnOccupied(board,position):
        if (board[position]==0):
                return True
        else:
                return False

def Occupied(board,position):
        if position<0 or position>63:
                return True
        if (board[position]!=0):
                return True
        else:
                return False

def IsPositionUnderThreat(board,position,player):
        blacks=[20,21,22,23,24]
        whites=[10,11,12,13,14]
        if player==10:
                for i in range(0,64,1):
                    if type(board[i])==int:
                        if board[i]>=20 and board[i]<=24:
                                for k in GetPieceLegalMoves(board,i):
                                        if position==k:
                                                return True
        if player==20:
                for i in range(0,64,1):
                    if type(board[i])==int:
                        if board[i]>=10 and board[i]<=14:
                                for k in GetPieceLegalMoves(board,i):
                                        if position==k:
                                                return True
        return False

def ValidPosition(board,position,player):
        if (position>=0 and position<=63):
                if Occupied(board,position)==True:
                        if player==10:
                                if board[position]>=20 and board[position]<=25:
                                        return True
                                else:
                                        return False
                        if player==20:
                                if board[position]>=10 and board[position]<=15:
                                        return True
                                else:
                                        return False
                else:
                        return True
        else:
                return False

def PawnLegalMoves(board,position,player):
        accum=[]
        if player==10:
                if (ValidPosition(board,position+8,player)==True and Occupied(board,position+8)==False):
                        accum+=[position+8]
                if (ValidPosition(board,position+9,player)==True and LeftEdge(position)==False):
                    if type(board[position+9])==int:
                        if board[position+9]>=20 and board[position+9]<=25:
                                accum+=[position+9]
                if (ValidPosition(board,position+7,player)==True and RightEdge(position)==False):
                    if type(board[position+7])==int:        
                        if board[position+7]>=20 and board[position+7]<=25:
                                accum+=[position+7]
        if player==20:
                if (ValidPosition(board,position-8,player)==True and Occupied(board,position-8)==False):
                        accum+=[position-8]
                if (ValidPosition(board,position-7,player)==True and LeftEdge(position)==False):
                    if type(board[position-7])==int:
                        if board[position-7]>=10 and board[position-7]<=15:
                                accum+=[position-7]
                if (ValidPosition(board,position-9,player)==True and RightEdge(position)==False):
                    if type(board[position-9])==int:
                        if board[position-9]>=20 and board[position-9]<=25:
                                accum+=[position-9] 
        return accum

def KnightLegalMoves(board,position,player):
    accum=[]
    if (Edge(position)==False):
            if ValidPosition(board,position-17,player)==True:
                    accum+=[position-17]
            if ValidPosition(board,position-15,player)==True:
                    accum+=[position-15]
            if ValidPosition(board,position-6,player)==True:
                    if RightEdge(position-6)!=True:
                            accum+=[position-6]
            if ValidPosition(board,position-10,player)==True:
                    if LeftEdge(position-10)!=True:
                            accum+=[position-10]
            if ValidPosition(board,position+10,player)==True:
                    if RightEdge(position+10)!=True:
                            accum+=[position+10]
            if ValidPosition(board,position+6,player)==True:
                    if LeftEdge(position+6)!=True:
                            accum+=[position+6]
            if ValidPosition(board,position+15,player)==True:
                    accum+=[position+15]
            if ValidPosition(board,position+17,player)==True:
                    accum+=[position+17]
    else:
            if BottomEdge(position)==True:
                    if BottomEdge(position+6)!=True and ValidPosition(board,position+6,player)==True:
                            accum+=[position+6]
                    if RightEdge(position+17)!=True and ValidPosition(board,position+17,player)==True:
                            accum+=[position+17]
                    if LeftEdge(position+15)!=True and ValidPosition(board,position+15,player)==True:
                            accum+=[position+15]
                    if ValidPosition(board,position+10,player)==True and (position!=6 and position!=7):
                            accum+=[position+10]
            if TopEdge(position)==True:
                    if TopEdge(position-6)!=True and ValidPosition(board,position-6,player)==True:
                            accum+=[position-6]
                    if LeftEdge(position-17)!=True and ValidPosition(board,position-17,player)==True:
                            accum+=[position-17]
                    if RightEdge(position-15)!=True and ValidPosition(board,position-15,player)==True:
                            accum+=[position-15]
                    if ValidPosition(board,position-10,player)==True and (position!=56 and position!=57):
                            accum+=[position-10]
            if RightEdge(position)==True:
                    if ValidPosition(board,position-6,player)==True:
                            accum+=[position-6]
                    if ValidPosition(board,position-15,player)==True:
                            accum+=[position-15]
                    if ValidPosition(board,position+10,player)==True:
                            accum+=[position+10]
                    if ValidPosition(board,position+17,player)==True:
                            accum+=[position+17]
            if LeftEdge(position)==True:
                    if ValidPosition(board,position+6,player)==True:
                            accum+=[position+6]
                    if ValidPosition(board,position+15,player)==True:
                            accum+=[position+15]
                    if ValidPosition(board,position-10,player)==True:
                            accum+=[position-10]
                    if ValidPosition(board,position-17,player)==True:
                            accum+=[position-17]
    return accum

def BishopLegalMoves(board,position,player):
        accum=[]
        if (Edge(position)==False):
                i=position+9
                j=position-9
                counter=0
                while ValidPosition(board,i,player)==True and counter==0:
                        accum+=[i]
                        i+=9
                        if Occupied(board,i-9)==True or Edge(i-9)==True:
                                counter+=1
                counter=0
                while ValidPosition(board,j,player)==True and counter==0:
                        accum+=[j]
                        j-=9
                        if Occupied(board,j+9)==True or Edge(j+9)==True:
                                counter+=1
                i=position+7
                j=position-7
                counter=0
                while ValidPosition(board,i,player)==True and counter==0:
                        accum+=[i]
                        i+=7
                        if Occupied(board,i-7)==True or Edge(i-7)==True:
                                counter+=1
                counter=0
                while ValidPosition(board,j,player)==True and counter==0:
                        accum+=[j]
                        j-=7
                        if Occupied(board,j+7)==True or Edge(j+7)==True:
                                counter+=1
        else:
                if (RightEdge(position)==True):
                        i=position+9
                        counter=0
                        while (ValidPosition(board,i,player)==True and counter==0):
                                accum+=[i]
                                i+=9
                                if Occupied(board,i-9)==True or Edge(i-9)==True:
                                        counter+=1
                        i=position-7
                        counter=0
                        while (ValidPosition(board,i,player)==True and counter==0):
                                accum+=[i]
                                i-=7
                                if Occupied(board,i+7)==True or Edge(i+7)==True:
                                        counter+=1
                if (LeftEdge(position)==True):
                    i=position+7
                    counter=0
                    while (ValidPosition(board,i,player)==True and counter==0):
                            accum+=[i]
                            i+=7
                            if Occupied(board,i-7)==True or Edge(i-7)==True:
                                    counter+=1
                    i=position-9
                    counter=0
                    while (ValidPosition(board,i,player)==True and counter==0):
                            accum+=[i]
                            i-=9
                            if Occupied(board,i+9)==True or Edge(i+9)==True:
                                    counter+=1
                if (TopEdge(position)==True):
                        i=position-7
                        j=position-9
                        counter=0
                        while ValidPosition(board,i,player)==True and counter==0:
                                accum+=[i]
                                i-=7
                                if Occupied(board,i+7)==True or Edge(i+7)==True:
                                        counter+=1
                        counter=0
                        while ValidPosition(board,j,player)==True and counter==0:
                                accum+=[j]
                                j-=9
                                if Occupied(board,j+9)==True or Edge(j+9)==True:
                                        counter+=1
                if (BottomEdge(position)==True):
                        i=position+7
                        j=position+9
                        counter=0
                        while (ValidPosition(board,i,player)==True and counter==0):
                                accum+=[i]
                                i+=7
                                if Occupied(board,i-7)==True or Edge(i-7)==True:
                                        counter+=1
                        counter=0
                        while ValidPosition(board,j,player)==True and counter==0:
                                accum+=[j]
                                j+=9
                                if Occupied(board,j-9)==True or Edge(j-9)==True:
                                        counter+=1
        return accum

def RookLegalMoves(board,position,player):
        accum=[]
        i=position+1
        j=position-1
        counter=0
        while (ValidPosition(board,i,player)==True and i%8!=0 and counter==0):
                accum+=[i]
                i+=1
                if Occupied(board,i-1)==True:
                        counter+=1
        counter=0
        while (ValidPosition(board,j,player)==True and j%8!=7 and counter==0):
                accum+=[j]
                j-=1
                if Occupied(board,j+1)==True:
                        counter+=1
        i=position+8
        j=position-8
        counter=0
        while (ValidPosition(board,i,player)==True and counter==0):
                accum+=[i]
                i+=8
                if Occupied(board,i-8)==True:
                        counter+=1
        counter=0
        while (ValidPosition(board,j,player)==True and counter==0):
                accum+=[j]
                j-=8   
                if Occupied(board,j+8)==True:
                        counter+=1
        return accum

def QueenLegalMoves(board,position,player):
        accum1=BishopLegalMoves(board,position,player)
        accum2=RookLegalMoves(board,position,player)
        return accum1+accum2

def KingLegalMoves(board,position,player):
        accum=[]
        if Edge(position)==False:
                for i in [-9,-8,-7,-1,1,7,8,9]:
                        if ValidPosition(board,position+i,player)==True:
                                if player==10:
                                        if IsPositionUnderThreat(board,position+i,10)==False:
                                                accum+=[position+i]
                                if player==20:
                                        if IsPositionUnderThreat(board,position+i,20)==False:
                                                accum+=[position+i]
                return accum
        if RightEdge(position)==True:                                        
                for i in [-8,-7,1,8,9]:
                        if ValidPosition(board,position+i,player)==True:
                                if player==10:
                                        if IsPositionUnderThreat(board,position+i,10)==False:
                                                accum+=[position+i]
                                if player==20:
                                        if IsPositionUnderThreat(board,position+i,20)==False:
                                                accum+=[position+i]
                return accum
        if LeftEdge(position)==True:
                for i in [-9,-8,-1,7,8]:
                        if ValidPosition(board,position+i,player)==True:
                                if player==10:
                                        if IsPositionUnderThreat(board,position+i,10)==False:
                                                accum+=[position+i]
                                if player==20:
                                        if IsPositionUnderThreat(board,position+i,20)==False:
                                                accum+=[position+i]
        if TopEdge(position)==True:
                for i in [-9,-8,-7,-1,1]:
                        if ValidPosition(board,position+i,player)==True:
                                if player==10:
                                        if IsPositionUnderThreat(board,position+i,10)==False:
                                                accum+=[position+i]
                                if player==20:
                                        if IsPositionUnderThreat(board,position+i,20)==False:
                                                accum+=[position+i]
                return accum
        else:
                for i in [-1,1,7,8,9]:
                        if ValidPosition(board,position+i,player)==True:
                                if player==10:
                                        if IsPositionUnderThreat(board,position+i,10)==False:
                                                accum+=[position+i]
                                if player==20:
                                        if IsPositionUnderThreat(board,position+i,20)==False:
                                                accum+=[position+i]
                return accum
                                    
def GetPieceLegalMoves(board,position):
        if (board[position]==10):
                return PawnLegalMoves(board,position,10)
        if (board[position]==11):
                return KnightLegalMoves(board,position,10)
        if (board[position]==12):
                return BishopLegalMoves(board,position,10)
        if (board[position]==13):
                return RookLegalMoves(board,position,10)
        if (board[position]==14):
                return QueenLegalMoves(board,position,10)
        if (board[position]==15):
                return KingLegalMoves(board,position,10)
        if (board[position]==20):
                return PawnLegalMoves(board,position,20)
        if (board[position]==21): 
                return KnightLegalMoves(board,position,20)
        if (board[position]==22):
                return BishopLegalMoves(board,position,20)
        if (board[position]==23):
                return RookLegalMoves(board,position,20)
        if (board[position]==24):
                return QueenLegalMoves(board,position,20)
        if (board[position]==25):
                return KingLegalMoves(board,position,20)
        return []
                 
'''def EvaluateBoard(board):
        whitevalue=0
        blackvalue=0
        accum=[]
        for i in board:
                if type(i)==int:
                        accum+=[i]
        for i in accum:
            if i>=10 and i<=14:
                    whitevalue+=i
            if i>=20 and i<=24:
                    blackvalue+=i
            if i==15:
                    whitevalue+=1000
            if i==25:
                    blackvalue+=1000
        return whitevalue-blackvalue'''

def EvaluateBoard(board):
        whitepieces=[10,11,12,13,14,15]
        blackpieces=[20,21,22,23,24,25]
        whitevalue=0
        blackvalue=0
        accum=[]
        for i in board:
            if type(i)==int:
                if i>=10 and i<=15:
                        if i==10:
                            whitevalue+=1
                        if i==11:
                            whitevalue+=3
                        if i==12:
                            whitevalue+=3.25
                        if i==13:
                            whitevalue+=5
                        if i==14:
                            whitevalue+=9
                        if i==15:
                            whitevalue+=1000
                if i>=20 and i<=25:
                        if i==20:
                            blackvalue+=1
                        if i==21:
                            blackvalue+=3
                        if i==22:
                            blackvalue+=3.25
                        if i==23:   
                            blackvalue+=5
                        if i==24:
                            blackvalue+=9
                        if i==25:
                            blackvalue+=1000
        return whitevalue-blackvalue
      
def Move(board,OldPosition,NewPosition,player):
        oldboard=[]
        for i in range(0,4,1):
                oldboard+=[0,0,0,0,0,0,0,0]
                oldboard+=[0,0,0,0,0,0,0,0]
        y=board[OldPosition]
        board[NewPosition]=y
        board[OldPosition]=oldboard[OldPosition]
        if player==10 and NewPosition>=56:
                board[NewPosition]=14
        if player==20 and NewPosition<=7:
                board[NewPosition]=24
        return board
        

def GetPlayerPositions(board,player):
        accum=[]
        if player==10:
                for i in range(0,64,1):
                    if type(board[i])==int:
                        if board[i]>=10 and board[i]<=15:
                                accum+=[i]
        if player==20:
                for i in range(0,64,1):
                    if type(board[i])==int:
                        if board[i]>=20 and board[i]<=25:
                                accum+=[i]
        return accum
    
def GameOver(board,player):
        if player==10:
                for i in board:
                        if i==15:
                                return False
        if player==20:
                for i in board:
                        if i==25:
                                return False
        return True

def PotentialBoards(board,player):
        accum=[]
        for i in GetPlayerMoves(board,player):
                board2=list(board)
                board2=Move(board2,i[0],i[1],player)
                if GameOver(board2,player)==False:
                        accum+=[board2]
        return accum

def Minimax(board,depth,alpha,beta,player):
    if depth==0 or GameOver(board,player)==True:
        return EvaluateBoard(board)
    if player==10:
        maxEval=-1000
        for i in PotentialBoards(board,player):
                eval1=Minimax(i,depth-1,alpha,beta,20)
                maxEval=max(maxEval,eval1)
                alpha=max(alpha,eval1)
                if beta<=alpha:
                        break
        return maxEval
    else:
        minEval=1000
        for i in PotentialBoards(board,player):
                eval2=Minimax(i,depth-1,alpha,beta,10)
                minEval=min(minEval,eval2)
                beta=min(beta,eval2)
                if beta<=alpha:
                        break
        return minEval

def GetPlayerMoves(board,player):
        blah=[]
        x=[]
        accum=[]
        counter=0
        for a in GetPlayerPositions(board,player):
                y=GetPieceLegalMoves(board,a)
                for b in range(0,len(y),1):
                        x+=[[a]]
                for c in range(0,len(y),1):
                        x[c]+=[y[c]]
                blah+=x
                x=[]
        return blah
        for i in blah:
                board2=list(board)
                Move(board2,i[0],i[1],player)
                for i in board2:
                        if i==player+5:
                                if IsPositionUnderThreat(board2,i,player)!=True:
                                        accum+=[i]
        return accum

def FindBestMove(board,player,depth):
        start=timer()
        x=Minimax(board,depth,-1e8,+1e8,player)
        end=timer()
        print(end-start,'ye',depth)
        if (end-start)>3.8:
                return FindBestMove(board,player,depth-1)
        for i in GetPlayerMoves(board,player):
                board2=list(board)
                board2=Move(board2,i[0],i[1],player)
                if player==10:
                        y=Minimax(board2,depth-1,-1e8,+1e8,20)
                        if y==x:
                                return i
                if player==20:
                        y=Minimax(board2,depth-1,-1e8,+1e8,10)
                        if y==x:
                                return i

def AutoPlayGame():
        blah=initialization()
        while GameOver(blah,10)!=True or GameOver(blah,20)!=True:
                oldpos=int(input("Old Pos"+"\n"))
                newpos=int(input("New Pos"+"\n"))
                blah=Move(blah,oldpos,newpos,10)
                PrintBoard(blah)
                start=timer()
                H=ChessPlayer(blah,20)
                end=timer()
                print(end-start,'b')
                print(H)
                blah=Move(blah,H[1][0],H[1][1],20)
                PrintBoard(blah)
                print(EvaluateBoard(blah))
                #blue=input("Continue?")
                #if blue!='ye':
                       # break
                #print(ChessPlayer(blah,10))
                '''huh=str(input("Do you wanna end game?"+"\n"))
                print("Player White, it is your turn.")
                H=FindBestMove(blah,10)
                print(H)
                blah=Move(blah,H[0],H[1],10)
                if GameOver(blah,10)==True:
                      14ver(blah,20)==True:
                        print ("Game Over")
                        return True
                else:
                        print (False)
                PrintBoard(blah)
                L=FindBestMove(blah,20)
                print(L)
                blah=Move(blah,L[0],L[1],20)
                if GameOver(blah,10)==True:
                        print ("Game Over")
                        return True
                if GameOver(blah,20)==True:
                        print("Game Over")
                        return True
                else:
                        print(False)
                print(EvaluateBoard(blah))
                counter+=1
        return True'''

PrintIndexes()
print("\n"+"\n")
AutoPlayGame()
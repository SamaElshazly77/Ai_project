#Tic-Tac-Toe using Mini-Max Algorithm

#This function is used to draw the board's current state every time the user turn arrives. 
def ConstBoard(board):
    print("Current State Of Board : \n\n");
    for i in range (0,9):
        if((i>0) and (i%3)==0):  # to print new line after 3 index 
            print("\n");
        if(board[i]==0):
            print("- ",end=" ");  # if it is empty replace it with  - 
        if (board[i]==1):
           print("O ",end=" "); # if it is empty replace it with  O
        if(board[i]==-1):    
            print("X ",end=" ");  # if it is empty replace it with  X
    print("\n\n");

#This function takes the user move as input and make the required changes on the board.
def User1Turn(board):
    pos=input("Enter X's position from [1...9]: ");
    pos=int(pos);
    if(board[pos-1]!=0):  # there is plaing symbol here 
        print("Wrong Move!!!");
        exit(0) ;
    board[pos-1]=-1;   # O player = -1

def User2Turn(board):
    pos=input("Enter O's position from [1...9]: ");
    pos=int(pos);
    if(board[pos-1]!=0):
        print("Wrong Move!!!");
        exit(0);
    board[pos-1]=1;    # X player = 1

#MinMax function.
def minimax(board,player):
    x=analyzeboard(board);
    if(x!=0):
        return (x*player);
    pos=-1;
    value=-2;
    for i in range(0,9):
        if(board[i]==0):
            board[i]=player;
            score=-minimax(board,(player*-1));
            if(score>value):
                value=score;
                pos=i;
            board[i]=0;

    if(pos==-1):
        return 0;
    return value;
    
#This function makes the computer's move using minmax algorithm.
def CompTurn(board):
    pos=-1;
    value=-2;
    for i in range(0,9):
        if(board[i]==0):
            board[i]=1;
            score=-minimax(board, -1);
            board[i]=0;
            if(score>value):
                value=score;
                pos=i;
 
    board[pos]=1;


#This function is used to analyze a game.
def analyzeboard(board):
    cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];

    for i in range(0,8):
        if(board[cb[i][0]] != 0 and  
           board[cb[i][0]] == board[cb[i][1]] and
           board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][2]];   # return the number of player 
    return 0;  # no player is win yet 

#Main Function.
def main():
    choice=input("Enter 1 for single player, 2 for multiplayer: ");
    choice=int(choice);
    #The broad is considered in the form of a single dimentional array.
    #One player moves 1 and other move -1.
    board=[0,0,0,0,0,0,0,0,0];


    if(choice==1):    # if the player choose one player vs computer
        print("Computer : O Vs. You : X");
        player= input("Enter to play 1(st) or 2(nd) :");  # choose be the first player or second player 
        player = int(player);



        for i in range (0,9):
            if(analyzeboard(board)!=0):   # it mean the game is end with -1 or 1
                break;
            if((i+player)%2==0):   #  if i choose 1 it will be odd result will go to else if i choose 2 it will begin the game with computer 
                CompTurn(board);   # computer turn 
            else:
                ConstBoard(board);    # fill the board 
                User1Turn(board);     # my turn 



    else:   # if the player choose one player vs player 
        for i in range (0,9):
            if(analyzeboard(board)!=0):
                break;
            if((i)%2==0):
                ConstBoard(board);
                User1Turn(board);
            else:
                ConstBoard(board);
                User2Turn(board);
         

    x=analyzeboard(board);      # analisys the board to display result 
    if(x==0):
         ConstBoard(board);  #bulid the board by x and y to display it 
         print("Draw!!!")
    if(x==-1):
         ConstBoard(board);
         print("X Wins!!! Y Loose !!!")
    if(x==1):
         ConstBoard(board);
         print("X Loose!!! O Wins !!!!")
       
#---------------#
main()
#---------------#



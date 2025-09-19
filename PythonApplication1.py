# tic tac toe game

def print_board(li):
    print("-"*12)
    for i in range(len(li)) :
        if (i+1) % 3==0 :
            print(f"{li[i]}\n")
            print("-"*12)
        else :
            print(li[i],end="  | ")

def player_move(player,board):
    if player == "X" :
        Place = int(input(f"Player {player} turn, enter a number from 1 to 9 : ")) 
        if Place not in board or Place=="X" or Place=="O":
            print("Place already taken, choose another place")
            Place = int(input(f"Player {player} turn, enter a number from 1 to 9 : "))
        idx=int(board.index(Place))
        board.remove(Place)
        board.insert(idx,player)
        print(f"Player {player} placed on {Place}")
        
    else: 
        Place = int(input(f"Player {player} turn, enter a number from 1 to 9 : "))
        if Place not in board or Place=="X" or Place=="O":
            print("Place already taken, choose another place")
            Place = int(input(f"Player {player} turn, enter a number from 1 to 9 : "))
        idx=int(board.index(Place))
        board.remove(Place)
        board.insert(idx,player)
        print(f"Player {player} placed on {Place}")
#check if player wins
def check_winner(player,board):
    if  (board[0]==board[1]==board[2]==player) or \
        (board[3]==board[4]==board[5]==player) or \
        (board[6]==board[7]==board[8]==player) or \
        (board[0]==board[3]==board[6]==player) or \
        (board[1]==board[4]==board[7]==player) or \
        (board[2]==board[5]==board[8]==player) or \
        (board[0]==board[4]==board[8]==player) or \
        (board[2]==board[4]==board[6]==player):
        print(f"Congratulations! Player {player} wins!")
        return 1
    return 0


def play_game():
    print("Welcome to Tic Tac Toe!")
    print("--------------------------------")
    print("Starting a new game...")
    print("--------------------------------")
    print("Player X always goes first")
    board = [1,2,3,4,5,6,7,8,9]
    print_board(board)
    # make moves =0 , if moves even x playes if odd o player
    moves=0
    flag=0
    while moves < 9 and flag==0:
        player = "X" if moves % 2 == 0 else "O"
        player_move(player, board)
        print_board(board)
        moves += 1
        flag=check_winner(player,board)
        if flag==1:
            break

    if flag == 0:
        print("It's a draw!")
        print("Thanks for playing Tic Tac Toe! ")

while True:
    play_game()
    replay = input("Do you want to play again? (yes/no): ")
    if replay.lower() != 'yes':
        print("Thanks for playing!")
        break
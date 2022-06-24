def main():
    board = []
    player = " "
    board  = fill_board() 
    while not (winner(board) or cat(board)):
        player = next_player(player)
        print_board (board)
        play_board (board, player)
        
    print_board(board)
    if winner(board):
        print(f"The winner is {player}!!!")
    else:
        print("The Cat is the winner!!!")


def fill_board ():
    board = []
    for i in range (9):
        board.append(i+1)
    return board

def print_board(board):
    print (f"{board[0]}|{board[1]}|{board[2]}")
    print ("-+-+-")
    print (f"{board[3]}|{board[4]}|{board[5]}")
    print ("-+-+-")
    print (f"{board[6]}|{board[7]}|{board[8]}")

def play_board (board, player):
    answer = int(input(f"{player} choose a number between (1-9):"))
    board [answer-1]= player
   
def next_player(player):
    if player == 'x':
        player = 'o'
    else:
        player = 'x'
    return player

def winner (board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def cat(board):
    for i in range(9):
        if board[i]!='x' and board[i]!='o':
            return False      
    return True
    

if __name__ == "__main__":
    main()
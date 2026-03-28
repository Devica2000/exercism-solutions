def gamestate(board):
    
    count_x = 0
    count_o = 0
    
    for state in board:
        for s in state:
            if s == "O":
                count_o +=1 
            if s == "X":
                count_x += 1

    if count_o > count_x: 
        raise ValueError("Wrong turn order: O started")

    if count_x > count_o + 1:
        raise ValueError("Wrong turn order: X went twice")

    def has_won(player):
        for row in board: 
            if row[0] == row[1] == row[2] == player:
                return True
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] == player:
                return True
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[2][0] == board[1][1] == board[0][2] == player:
            return True
        return False

    x_win = has_won("X")
    o_win = has_won("O")

    if x_win and o_win:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if x_win and count_x == count_o:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if o_win and count_x > count_o:
        raise ValueError("Impossible board: game should have ended after the game was won")

    if x_win or o_win:
        return "win"
    if count_o + count_x == 9:
        return "draw"
    else:
        return "ongoing"
            

    
        

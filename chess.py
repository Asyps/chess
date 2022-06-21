board = {
    # black
    (1, 1): {
        "type": "rook",
        "color": "black"
    },
    (2, 1): {
        "type": "knight",
        "color": "black"
    },
    (3, 1): {
        "type": "bishop",
        "color": "black"
    },
    (4, 1): {
        "type": "queen",
        "color": "black"
    },
    (5, 1): {
        "type": "king",
        "color": "black"
    },
    (6, 1): {
        "type": "bishop",
        "color": "black"
    },
    (7, 1): {
        "type": "knight",
        "color": "black"
    },
    (8, 1): {
        "type": "rook",
        "color": "black"
    },
    
    # white
    (1, 8): {
        "type": "rook",
        "color": "white"
    },
    (2, 8): {
        "type": "knight",
        "color": "white"
    },
    (3, 8): {
        "type": "bishop",
        "color": "white"
    },
    (4, 8): {
        "type": "queen",
        "color": "white"
    },
    (5, 8): {
        "type": "king",
        "color": "white"
    },
    (6, 8): {
        "type": "bishop",
        "color": "white"
    },
    (7, 8): {
        "type": "knight",
        "color": "white"
    },
    (8, 8): {
        "type": "rook",
        "color": "white"
    }   
}

for i in range(1, 9):
    board[(i, 2)] = {
        "type": "pawn",
        "color": "black",
        "moved": False
    }
    board[(i, 7)] = {
        "type": "pawn",
        "color": "white",
        "moved": False
    }

for i in range(1, 9):
    for j in range(1, 9):
        coord = (j, i)
        if coord in board:
            print(board[coord]["type"][:2], end="")
        else:
            print("  ", end="")
    print()
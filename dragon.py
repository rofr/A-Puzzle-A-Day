import all_pieces

print(all_pieces.all_pieces())

def board():
   result = list([True] * 43)

# create a target board where target month and day are marked as occupied
# month is 1-12, day is 1-31
def target(month,day):
   board = board()
   board[month-1] = False
   board[day+11]

def valid_moves(board, pieces):
    pass

def apply_move(move, board):
   pass

def search(pieces, board, moves):
   for piece in pieces:
      remaining_pieces = pieces.remove(piece)
      for move in valid_moves(board, piece):
        moves.push(move)
        apply_move(move,board)
        search(remaining_pieces, board, moves)

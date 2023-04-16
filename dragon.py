from all_pieces import all_pieces
from datetime import datetime
import sys

#print(all_pieces())

def board():
   return list([0] * 43)

# create a target board where target month and day are marked as occupied
# month is 1-12, day is 1-31
def puzzle(month,day):
   b = board()
   b[month-1] = 'X'
   b[day+11] = 'X'
   return b

def valid_placements(board, placements):
   result = []
   for placement in placements:
      is_valid = True
      for square in placement:
         if board[square] != 0:
            is_valid = False
            break
      if is_valid:
         result.append(placement)
   return result

# Put the number of the piece into each square the piece occupies
def place_piece(piece_number, squares, board):
   for square in squares:
      board[square] = piece_number

# set the squares which the piece had occupied back to zero
def remove_piece(squares, board):
   for square in squares:
      board[square] = 0

def solve(pieces, board, solutions):
   # no pieces left means we have placed all of them on the board
   # and found a solution
   if (len(pieces) == 0):
      if (board.count(0) == 0):
         solutions.append(board.copy())
         pretty_print(board)
      return

   #pieces are numbered from 1 to 8
   piece_number = 9 - len(pieces)
   piece = pieces.pop()
   for placement in valid_placements(board, piece):
      place_piece(piece_number,placement,board)
      solve(pieces, board, solutions)
      remove_piece(placement,board)
   pieces.append(piece)

def pretty_print(board):
   b = board
   s = ' '
   print(b[0], b[1],b[2], b[3], b[4], b[5], sep=s)
   print(b[6], b[7],b[8], b[9], b[10],b[11], sep=s)
   print(b[12], b[13],b[14], b[15], b[16],b[17],b[18], sep=s)
   print(b[19], b[20],b[21], b[22], b[23],b[24],b[25], sep=s)
   print(b[26], b[27],b[28], b[29], b[30],b[31],b[32], sep=s)
   print(b[33], b[34],b[35], b[36], b[37],b[38],b[39], sep=s)
   print(b[40], b[41], b[42], sep=s)



if __name__ == "__main__":
   if len(sys.argv) == 3:
      month = int(sys.argv[1])
      day = int(sys.argv[2])
   else:
      now = datetime.now()
      month = now.month
      day = now.day
   print(month, day)

   p = puzzle(month,day)
   pretty_print(p)
   solutions = []
   solve(all_pieces(),p,solutions)
   for solution in solutions:
      print("Solution")
      pretty_print(solution)
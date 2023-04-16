from all_pieces import all_pieces
from datetime import datetime
import sys

# the board is represented as a one-dimensional array of size 43
# An empty board is all zeros
def board():
   return list([0] * 43)

# create a target board where target month and day are marked as occupied
# month is 1-12, day is 1-31
def puzzle(month,day):
   b = board()
   b[month-1] = 'X'
   b[day+11] = 'X'
   return b

# A piece is represnted as an array of all possible 
# placements on the board. Each placement is an array
# array of indicies on the board
def valid_placements(board, piece):
   result = []
   for placement in piece:
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

# Depth first exhaustive search using recursion
def solve(pieces, board, solutions):

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
   print(b[0], b[1],b[2], b[3], b[4], b[5])
   print(b[6], b[7],b[8], b[9], b[10],b[11])
   print(b[12], b[13],b[14], b[15], b[16],b[17],b[18])
   print(b[19], b[20],b[21], b[22], b[23],b[24],b[25])
   print(b[26], b[27],b[28], b[29], b[30],b[31],b[32])
   print(b[33], b[34],b[35], b[36], b[37],b[38],b[39])
   print(b[40], b[41], b[42])
   print()



if __name__ == "__main__":

   # get the month and day from the command line
   # or use todays date when not specified
   if len(sys.argv) == 3:
      month = int(sys.argv[1])
      day = int(sys.argv[2])
   else:
      now = datetime.now()
      month = now.month
      day = now.day

   p = puzzle(month,day)
   solutions = []
   pieces = all_pieces()
   solve(pieces, p, solutions)
   print("number of solutions:", len(solutions))
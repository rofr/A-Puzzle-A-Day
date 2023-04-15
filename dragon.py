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
      solutions.append(board.copy())
      return

   #pieces are numbered from 1 to 8
   piece_number = 9 - len(pieces)
   piece = pieces.pop()
   for placement in valid_placements(board, piece):
      place_piece(piece_number,placement,board)
      solve(pieces, board, solutions)
      remove_piece(placement,board)

def pretty_print(board):
   print(board)

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
   solutions = []
   solve(all_pieces(),p,solutions)
   for solution in solutions:
      print("\nSolution")
      pretty_print(solution)
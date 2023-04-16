import dragon
from all_pieces import all_pieces

def test_board_size():
    b = dragon.board()
    assert(len(b) == 43)

def test_all_placements_on_empty_board_should_be_valid():
    b = dragon.board()
    all_placements = all_pieces()
    for piece in all_placements:
        valid = dragon.valid_placements(b, piece)
        assert(len(piece) == len(valid))
            
def test_placement_followed_by_removal_yields_original_board():
    b = dragon.board()
    expected = dragon.board()
    all_placements = all_pieces()
    for piece in all_placements:
        valid = dragon.valid_placements(b, piece)
        for placement in valid:
            dragon.place_piece(1, placement,b)
            dragon.remove_piece(placement, b)
            assert(b == expected)

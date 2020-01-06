# Class Dictionary Validator

board = {'1a': 'brook',
        '1b': 'bknight',
        '1c': 'bbishop',
        '1d': 'bqueen',
        '1e': 'bking',
        '1f': 'bbishop',
        '1g': 'bknight',
        '1h': 'brook',
        '2a': 'bpawn',
        '2b': 'bpawn',
        '2c': 'bpawn',
        '2d': 'bpawn',
        '2e': 'bpawn',
        '2f': 'bpawn',
        '2g': 'bpawn',
        '2h': 'bpawn',
        '8a': 'wrook',
        '8b': 'wknight',
        '8c': 'wbishop',
        '8d': 'wqueen',
        '8e': 'wking',
        '8f': 'wbishop',
        '8g': 'wknight',
        '8h': 'wrook',
        '7a': 'wpawn',
        '7b': 'wpawn',
        '7c': 'wpawn',
        '7d': 'wpawn',
        '7e': 'wpawn',
        '7f': 'wpawn',
        '7g': 'wpawn',
        '7h': 'wpawn'}

pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
for piece in pieces:
    piece in board.values()

#def isValidChessBoard(board):
    #pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    #keys_first = [1, 2, 3, 4, 5, 6, 7, 8]
    #keys_second = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    #board = input()

# dict values contain ('pawn', 'knight', 'bishop', 'rook', 'queen', 'king')
# count of dict values <= 16
# count of 'bking' and 'wking' == 1
# count of dict values containing 'pawn' <= 8
# first character of dict keys must range from 1 to 8
# second character of dict keys must range from 'a' to 'h'
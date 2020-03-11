# Class Dictionary Validator

sample_board = {'1a': 'brook', '1b': 'bknight', '1c': 'bbishop', '1d': 'bqueen', '1e': 'bking', '1f': 'bbishop', '1g': 'bknight', '1h': 'brook', '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn', '8a': 'wrook', '8b': 'wknight', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wking', '8f': 'wbishop', '8g': 'wknight', '8h': 'wrook', '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn'}

def isValidChessBoard(board):
    value_list = list(sample_board.values())
    key_list = list(sample_board.keys())
    value_count = {}
    #key_count = {}
    for value in value_list:
        value_count.setdefault(value, 0)
        value_count[value] += 1
    #for key in key_list:
        #key_count.setdefault(key, 0)
        #key_count[key] += 1
    if value_count['bking'] != 1:
        return('False.')
        return('Incorrect count of black king pieces.')
    if value_count['wking'] != 1:
        return('False.')
        return('Incorrect count of wlack king pieces.')
    
# Create value_count as global variable for testing
value_count = {}
for value in value_list:
    value_count.setdefault(value, 0)
    value_count[value] += 1

# Create key_count as global variable for testing
key_list = list(sample_board.keys())
key_count = {}
for key in key_list:
    key_count.setdefault(key, 0)
    key_count[key] += 1

# Check if 'pawn' in values
for value in value_list:
    'pawn' in value
    
# Check first character of values
for value in value_list:
    print(value[0])
    
#1 count of 'bking' and 'wking' == 1
#2 count of dict values (pieces) <= 16
#3 count of dict values containing 'pawn' <= 8
#4 first character of dict keys must range from 1 to 8
#5 second character of dict keys must range from 'a' to 'h'
#6 dict values begin with 'w' or 'b'
#7 dict values must contain ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
# Return True or False
# Give error message when 'bug has resulted in an improper chess board'

# use for k in board.items() to parse keys and check first and second characters (may need to convert to strings)
# use for v in board.items() to parse keys and check first and remaining characters characters (may need to convert to strings)
# evaluate in final if statement?
# how to account for error message?

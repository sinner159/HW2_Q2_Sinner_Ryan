#!/usr/bin/env python
#coding:utf-8

"""
Each sudoku board is represented as a dictionary with string keys and
int values.
e.g. my_board['A1'] = 8
"""

import time
from ac3 import AC3
from backtracking import BackTrackingSearch
from csp import CSP


ROW = "ABCDEFGHI"
COL = "123456789"


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionary to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)


def backtracking(board):
    """Takes a board and returns solved board."""
    # TODO: implement this
    
    #Need to implement
    #constraint satisfaction
    #Backtracking
    #Minimum remaining value heuristic
    #forward checking
    bts = BackTrackingSearch()
    ac3 = AC3()
    csp = CSP(board)
    assignment = {k:v for k,v in board.items() if v != 0}
    solvable = ac3.ac3(csp)
    solved_board = bts.backtrack(csp,assignment)
    return solved_board


if __name__ == '__main__':
    #  Read boards from source.
    src_filename = 'sudokus_start.txt'
    try:
        srcfile = open(src_filename, "r")
        sudoku_list = srcfile.read()
    except:
        print("Error reading the sudoku file %s" % src_filename)
        exit()

    # Setup output file
    out_filename = 'output.txt'
    outfile = open(out_filename, "w")

    # Solve each board using backtracking
    then = time.time()
    sum = float(0)
    for line in sudoku_list.split("\n"):

        if len(line) < 9:
            continue

        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(line[9*r+c])
                  for r in range(9) for c in range(9)}

        # Print starting board. TODO: Comment this out when timing runs.
        print_board(board)

        # Solve with backtracking
        then_bts = time.time()
        solved_board = backtracking(board)
        t = time.time() - then_bts
        print(f"Took {t} seconds")
        sum += t
        
        # Print solved board. TODO: Comment this out when timing runs.
        print_board(solved_board)

        # Write board to file
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')

    avg = sum/400
    avg_time = avg/60
    total_time = time.time() - then
    mins = total_time / 60
    print(f"Average time per board: {avg_time} Total Time: {mins}")
    print("Finishing all boards in file.")
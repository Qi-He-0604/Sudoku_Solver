#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:06:59 2020

@author: heqi
"""

#construct the 9x9 sudoku
board = [[0,7,0,0,0,5,0,0,0],
         [1,0,0,0,3,0,5,0,8],
         [0,0,0,2,0,9,0,6,0],
         [9,1,0,5,0,0,4,2,0],
         [6,8,0,3,0,0,0,1,0],
         [2,5,4,0,9,0,0,0,3],
         [7,0,6,8,0,1,0,4,0],
         [3,4,5,0,0,6,0,7,1],
         [0,0,1,0,7,0,2,0,6]
         ]
         
#print sudoku as 9 3x3 boxes
def print_sudoku(board):
    #iterate rows
    for i in range(len(board)):
        if i % 3 == 0 :
            print("-------------------------")
        #iterate columns
        for j in range(len(board[0])):
            if j % 3 == 0 :
                print("| ", end="")
            if j == 8:
                print(str(board[i][j]) + " |")
            else:
                print(str(board[i][j]) + " ", end="")
        if i == 8:
            print("-------------------------")

print_sudoku(board)

#define a function to find empty spot in sudoku, in this case find 0s
def find_empty(board):
    #iterate rows
    for i in range(len(board)):
        #iterate columns
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) #index of an empty spot
    return None #when there's no empty spot

#define a function to check if numbers we filled in is valid
def valid(board, num, spot):
    #iterate rows - check if there's a same number exsiting in the same columns
    for i in range(len(board)):
        if board[i][spot[1]] == num and i != spot[0]:
            return False
    #iterate columns - check if there's a same number exsiting in the same row
    for j in range(len(board[0])):
        if board[spot[0]][j] == num and j != spot[1]:
            return False
    #check if there's a same number exsiting in the same 3x3 box
    #use floor division to decide which box a spot belongs to
    box_x = spot[0] // 3
    box_y = spot[1] // 3
    #iterate spots in the designated box
    for i in range(box_x*3, box_x*3 + 3):
        for j in range(box_y * 3, box_y*3 + 3):
            if board[i][j] == num and (i,j) != spot:
                return False
    return True

#define a function to solve sudoku
def solve(board):
    spot_find = find_empty(board)
    if not spot_find:
        return True #the whole sudoku is solved if there's no empty spot
    else:
         row,col = spot_find
    #iterate possible anwers - 1 to 9
    for i in range(1,10):
        #if a possible answer is valid, fill in and keep trying to find next empty and solve
        if valid(board, i, (row,col)):
            board[row][col] = i
            if solve(board):
                return True #the whole sudoku is solved
            board[row][col] = 0 #the sudoku is not solved with this answer - change spot back to 0
    return False #sudoku not solved

print(" ------ Solution ------ ")
solve(board)
print_sudoku(board)
def sudokuSolver(board): 
  '''
  The isValid() checks if a number is valid to be added at a cell. 
  '''
  def isValid(board, row, column, num): 
    for x in range(9): 
      '''
      Column Check
      '''
      if board[row][x] == num: 
        return False
      '''
      Row Check
      '''
      if board[x][column] == num: 
        return False
      r = 3 * (row // 3) + x // 3 
      c  = 3 * (column // 3) + x % 3 
      if board[r][c] == num:
        return False
    return True
  ''' 
  The recurFunc() is the recursive function to be used to solve the sudoku puzzlw
  '''
  def recurFunc(board):
    for row in range(9):
      for col in range(9):
        '''
        Monitoring for empty cells, and add a number within 1 through 9 within that cell
        '''
        if board[row][col] == '.':
          for num in '123456789':
            ''' 
            Before adding the number, check if that number is a valid for that cell. 
            '''
            if isValid(board,row, col, num):
              board[row][col] = num
              if recurFunc(board): return True # checks if the board is filled up completely.
              board[row][col] == '.' #backtracking step
          return False
    return True
            
  '''
  The function is called lastly because the puzzle will be solved in place.
  '''
  recurFunc(board)
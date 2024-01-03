y_pos = [-1, -1, -1,  0, 0,  1, 1, 1]
x_pos = [-1,  0,  1, -1, 1, -1, 0, 1]

class MatrixNumber:
  def __init__(self, number_string, row, end):
    self.number_string = number_string
    self.row = row
    self.end = end
    self.len = len(number_string)
    self.start = end - self.len

  def has_symbol_nearby(self, symbols):
    has_symbol = False
    for i in range(self.start, self.end):
      for k in range(len(y_pos)):
        new_row = self.row + y_pos[k]
        new_col = i + x_pos[k]
        for symbol in symbols:
          if symbol.row == new_row and symbol.col == new_col:
            has_symbol = True
            break
      if has_symbol:
        break
    return has_symbol

class Symbol:
  def __init__(self, row, col):
    self.row = row
    self.col = col

matrix = []

m = 0

with open("engine-schematic.txt") as file:
  for line in file:
    line = line.strip()
    row = list(line)
    matrix.append(row)

    m += 1

n = len(matrix)

print(n, m)

numbers = []
symbols = []

for i in range(n):
  cur_number = ''
  for j in range(m):
    char = matrix[i][j]
    is_number = char.isdigit()
    is_symbol = (not char.isdigit()) and char != '.'

    if is_number:
      cur_number += char
    elif cur_number:
      numbers.append(MatrixNumber(cur_number, i, j))
      cur_number = ''
    
    if is_symbol:
        symbols.append(Symbol(i, j))
  
  if cur_number:
    numbers.append(MatrixNumber(cur_number, i, j))
    cur_number = ''

part_numbers_sum = 0
for number in numbers:
  if number.has_symbol_nearby(symbols):
    part_numbers_sum += int(number.number_string)
    print("found symbol near", number.number_string)

print("Part numbers sum total:", part_numbers_sum)

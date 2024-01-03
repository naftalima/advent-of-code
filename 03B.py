y_pos = [-1, -1, -1,  0, 0,  1, 1, 1]
x_pos = [-1,  0,  1, -1, 1, -1, 0, 1]

class MatrixNumber:
  def __init__(self, number_string, row, end):
    self.number_string = number_string
    self.row = row
    self.end = end
    self.len = len(number_string)
    self.start = end - self.len

  def get_nearby_symbol(self, symbols):
    for i in range(self.start, self.end):
      for k in range(len(y_pos)):
        new_row = self.row + y_pos[k]
        new_col = i + x_pos[k]
        for symbol in symbols:
          if symbol.row == new_row and symbol.col == new_col:
            return symbol
    return None

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
    is_symbol = char == '*'

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

gear_ratios = {}
# part_numbers_sum = 0
for number in numbers:
  symbol_pos = number.get_nearby_symbol(symbols)
  if symbol_pos != None:
    symbol_key = f'{symbol_pos.row},{symbol_pos.col}'
    if symbol_key not in gear_ratios:
      gear_ratios[symbol_key] = (1, 0)
    
    number_value = int(number.number_string)

    current_ratio = gear_ratios[symbol_key]
    gear_ratios[symbol_key] = (current_ratio[0] * number_value, current_ratio[1] + 1)

total_sum = 0

for ratio_key in gear_ratios:
  ratio, count = gear_ratios[ratio_key]
  if count > 1:
    total_sum += ratio

print(total_sum)

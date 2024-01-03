file_name='puzzle-input/'+'calibration-doc.txt'

process_line_digits = lambda lines: (
    (lines[0], lines[0]) if len(lines) == 1 else
    (lines[0], lines[-1]) if len(lines) > 1 else None
)

tupla_to_int = lambda digts: int(digts[0])*10 + int(digts[1])

calibration_digits = []
with open(file_name) as file:
  for line in file:
    digits_per_line = [i for i in line if i.isdigit()]
    calibration_digits.append(process_line_digits(digits_per_line))

calibration_values = [ tupla_to_int(j) for j in calibration_digits]
print('calibration values:' ,calibration_values)

print('Adding these together produces', sum(calibration_values))
import regex as re

dict_digit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

pattern = r"(zero|one|two|three|four|five|six|seven|eight|nine|[0-9])"

process_line_digits = lambda lines: (
    (lines[0], lines[0]) if len(lines) == 1 else
    (lines[0], lines[-1]) if len(lines) > 1 else None
)

tupla_to_int = lambda digts: int(digts[0])*10 + int(digts[1])

calibration_digits = []
with open("calibration-doc.txt") as file:
  for line in file:
    line = line.strip()
    numbers = re.findall(pattern, line, overlapped=True)
    numbers_digit =  []
    for number in numbers:
        if not number.isdigit():
            numbers_digit.append(dict_digit[number])
        else:
            numbers_digit.append(number)
    # print(numbers_digit)

    calibration_digits.append(process_line_digits(numbers_digit))

    # values = tupla_to_int(process_line_digits(numbers_digit))
    # print(line, values)

calibration_values = [ tupla_to_int(j) for j in calibration_digits]

print('calibration values:' ,calibration_values)

print('Adding these together produces', sum(calibration_values))
print(len(calibration_values))
def convert(numbers, map):
  source_map = [] # [tupla] : (source_start,source_end,diff) 
  for i in map:
    destination_start, source_start, range_len = i 
    source_start = int(source_start)
    source_end = source_start+int(range_len) 
    destination_start = int(destination_start) 
    diff =  destination_start - source_start 
    source_map.append((source_start,source_end,diff)) 
    diff = 0
  
  correspond_numbers = []
  for number in numbers:
    number = int(number)
    for source_start,source_end,diff in source_map:
      if (number >= source_start) and (number <= source_end):
        correspond_number =  number + diff
        break
      else:
        correspond_number =  number
    correspond_numbers.append(str(correspond_number))

  return(correspond_numbers)


def get_locations(seeds, maps):
  relations = ['seed-to-soil map:',
               'soil-to-fertilizer map:',
               'fertilizer-to-water map:',
               'water-to-light map:',
               'light-to-temperature map:',
               'temperature-to-humidity map:',
               'humidity-to-location map:'
              ]

  print('seeds', seeds)
  correspond_numbers = seeds
  for relation in relations:
    print(relation)
    map = maps[relation]
    correspond_numbers = convert(correspond_numbers, map)
    print(correspond_numbers)
  locations = correspond_numbers
  locations = [int(location) for location in locations]
  return(locations)


with open("puzzle-input/Almanac.txt") as f:
  lines = f.read().split('\n')

_, seeds = lines[0].split(':')
lines = lines[2:] 
seeds = seeds.split()

# maps = {'smt_to_smt': [(destination range start, source range start, range length)]}
maps = {}
cur_key = ''
for line in lines:
  if line == '':
    cur_key = ''
  elif 'to' in line:
    cur_key = line
    maps[cur_key] = [] 
  else:
    dest_start, source_star, range_len = line.split(' ')
    maps[cur_key].append((dest_start, source_star, range_len))


locations = get_locations(seeds, maps)
min_location = min(locations)
print(min_location) 
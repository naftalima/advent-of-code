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


# def get_locations(seeds, maps):
#   relations = ['seed-to-soil map:',
#                'soil-to-fertilizer map:',
#                'fertilizer-to-water map:',
#                'water-to-light map:',
#                'light-to-temperature map:',
#                'temperature-to-humidity map:',
#                'humidity-to-location map:'
#               ]

#   print('seeds', seeds)
#   correspond_numbers = seeds
#   for relation in relations:
#     print(relation)
#     map = maps[relation]
#     correspond_numbers = convert(correspond_numbers, map)
#     print(correspond_numbers)
#   locations = correspond_numbers
#   locations = [int(location) for location in locations]
#   return(locations)


with open("puzzle-input/almanac.txt") as f:
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

best_answer = None

map_names = [
              'seed-to-soil map:',
               'soil-to-fertilizer map:',
               'fertilizer-to-water map:',
               'water-to-light map:',
               'light-to-temperature map:',
               'temperature-to-humidity map:',
               'humidity-to-location map:'
]

def get_next_map(map_index):
  return maps[map_names[map_index]]

def find_overlaps(seed_interval, puzzle_map):
  seed_interval_start, seed_interval_end = seed_interval
  overlaps = []
  for mapping in puzzle_map:
    target_map_start, source_map_start, map_len = mapping

    target_map_start = int(target_map_start)
    source_map_start = int(source_map_start)
    map_len = int(map_len)

    map_offset = target_map_start - source_map_start

    source_interval = (source_map_start, source_map_start + map_len - 1)
    source_interval_start, source_interval_end = source_interval

    if source_interval_start > seed_interval_end: continue
    if seed_interval_start > source_interval_end: continue

    overlap_start = max(seed_interval_start, source_interval_start)
    overlap_end = min(seed_interval_end, source_interval_end)

    range_outside = None

    if seed_interval_start < overlap_start:
      range_outside = (seed_interval_start, overlap_start - 1)
    elif seed_interval_end > overlap_end:
      range_outside = (overlap_end + 1, seed_interval_end)

    mapped_overlap_start = overlap_start + map_offset
    mapped_overlap_end = overlap_end + map_offset
    mapped_overlap_interval = (mapped_overlap_start, mapped_overlap_end)

    overlaps.append((mapped_overlap_interval, range_outside))

  return overlaps


def proceed(seed_interval, map_index):
  # (0, 1438146)
  global best_answer
  
  if map_index >= len(map_names):
    return
  if map_index == len(map_names) - 1  :
    if best_answer == None:
      best_answer = seed_interval[0]
    else:
      best_answer = min(best_answer, seed_interval[0])
    return

  print("Interval", seed_interval)
  next_map = get_next_map(map_index)
  overlapping_intervals = find_overlaps(seed_interval, next_map)
  if len(overlapping_intervals) == 0:
    proceed(seed_interval, map_index + 1)
    return
  
  for overlap in overlapping_intervals:
    overlap_interval, range_outside = overlap
    proceed(overlap_interval, map_index + 1)
    if range_outside != None:
      proceed(range_outside, map_index + 1)


i = 0
while i < len(seeds):
  seed_interval_start = int(seeds[i])
  seed_interval_size = int(seeds[i + 1])

  seed_interval_end = seed_interval_start + seed_interval_size - 1


  starting_interval = (seed_interval_start, seed_interval_end)
  print("Executing interval", starting_interval)
  proceed(starting_interval, 0)
  print("Best answer is", best_answer)

  i += 2

# locations = get_locations(seeds, maps)
# candidate_locations = []

# seed interval
# si1: [79..92]
# si2: [55..67]

# seed-to-soil
# sts1: [50..97] -> [52..99] +2 
# sts2: [98..99] -> [50..51] -48

# soil-to-fertilizer
# stf3: [00..14] -> [39..53]
# stf1: [15..51] -> [00..36] 
# stf2: [52..53] -> [37..38]

# fertilizer-to-water
# ftw3: [0..6]
# ftw4: [7..10]
# ftw2: [11..52]
# ftw1: [53..60]

# water-to-light
# wtl1: [18..24] -> [88.94]  +80
# wtl2: [25..94] -> [18..87] -7

# light-to-temperature
# ltt2: [45..63] -> [81..99] +36
# ltt3: [64..76] -> [68..80] +4
# ltt1: [77..99] -> [45..67] -32

# temperature-to-humidity
# tth2: [00..68] -> [1..69]   +1
# tth1: [69..69] -> [00..00]  -69

# humidity-to-location
# htl1: [56..92] -> [60..96]  +4
# htl2: [93..96] -> [56..59]  -37

# PATHS
  # si1 -> sts1 (overlap: [79..92]) -> [81..94]
    # sts1 -> NO MATCHES with stf
    # sts1 -> stf [81..94] (SAME)
      # stf -> NO MATCHES with ftw
      # stf -> ftw [81..94] (SAME)
        # ftw -> wtl2 (overlap: [81..94]) -> [74..87]
          # wtl2 -> ltt3 (overlap: [74..76]) -> [78..80]
              # SHOULD ALSO HAVE A FLOW FOR [77..77]
            # ltt3 -> NO MATCHES with tth
            # ltt3 -> tth [78..80] (SAME)
              # tth -> htl1 (overlap: [78..80]) -> [82..84]]
          # wtl2 -> ltt1 (overlap: [77..87]) -> [45..55]
            # ltt1 -> tth2 (overlap: [45..55]) -> [46..66]
            
              # tth2 -> htl1 (overlap: [56..66]) -> [60..70]
                # BEST keep 46 than use overlap of 60
                # whenever doing a transition,
                # should also consider smallest number outside overlap
                # so [46..46], [60..70]
              
  # si2 -> sts1 (overlap: [55..67])

'''
  # seed_interval is [x..y]
  def proceed(seed_interval, next_map):
  if not next_map:
    minimize lowest value found with smallest value in interval
    return

  overlapping_interval, smallest_outside = find_overlap(seed_interval, next_map)
  if empty overlapping_interval:
    # initial interval
    proceed(seed_interval)
  else:
    proceed(overlapping_interval)
    lowest_number_outside_interval = find_lowest_outside_interval()
    proceed(lowest_number_outside_interval)

'''

# min_location = min(locations)
# print(min_location) 
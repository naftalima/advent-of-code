def convert(numbers, map):
  number_map = []
  for i in map:
    dest_start, source_star, range_len = i
    destination = [j + int(dest_start) for j in range(int(range_len))]
    source =  [k + int(source_star) for k in range(int(range_len))]
    dst_src = list(zip(source, destination))
    for j in dst_src: number_map.append(j)
  number_map_sorted = sorted(number_map, key=lambda x: x[0])
  hash_table = {}
  for i,j in number_map_sorted: hash_table[str(i)]= str(j)

  correspond_numbers = []
  for i in range(len(numbers)):
    number= numbers[i]
    correspond_number = 0
    if not number in hash_table:
      correspond_number = number
    else:
      correspond_number = hash_table[number]
    correspond_numbers.append(correspond_number)
  
  return(correspond_numbers)


def get_locations(seeds, maps):
  print('seeds', seeds)
  soils = convert(seeds,maps['seed-to-soil map:'])
  print('soils', soils)
  fertilizers = convert(soils,maps['soil-to-fertilizer map:']) 
  print('fertilizers', fertilizers)
  waters = convert(fertilizers,maps['fertilizer-to-water map:']) 
  print('waters', waters)
  lights = convert(waters,maps['water-to-light map:'])
  print('lights', lights)
  temperatures = convert(lights,maps['light-to-temperature map:']) 
  print('temperatures', temperatures)
  humiditys = convert(temperatures,maps['temperature-to-humidity map:']) 
  print('humiditys', humiditys)
  locations = convert(humiditys,maps['humidity-to-location map:']) 
  print('locations', locations)
  return(locations)


with open("puzzle-input/almanac.txt") as f:
  lines = f.read().split('\n')

_, seeds = lines[0].split(':')
del lines[0]
del lines[0]
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
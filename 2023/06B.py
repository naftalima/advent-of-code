import numpy

def count_winnable_races(race_tuple):
    time, distance = race_tuple
    count = 0
    for i in range(time):
        hold_bt = i
        velocity = hold_bt
        travel_time = time - hold_bt
        travelled_distance = velocity * travel_time
        if travelled_distance > distance:
            count+=1
    return count


race = {}
with open("puzzle-input/races.txt") as file:
    for line in file:
        key, values = line.split(':')
        values = int(''.join(values.split()))
        race[key] = values

time = race['Time']
distance = race['Distance']

print(count_winnable_races((time, distance)))

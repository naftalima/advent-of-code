import numpy

def count_winnable_races(race_tuple):
    print(race_tuple)
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


races = {}
with open("puzzle-input/races.txt") as file:
    for line in file:
        key, values = line.split(':')
        values = values.split()
        values = [int(value) for value in values]
        races[key] = values

time = races['Time']
distance = races['Distance']

races_tuple = zip(time, distance)

races_won =  [count_winnable_races(race_tuple) for race_tuple in races_tuple]
print(races_won)

result = numpy.prod(races_won)
print(result)
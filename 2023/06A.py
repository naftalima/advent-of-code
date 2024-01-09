from termcolor import colored
import numpy

def count_winnable_races(race_tuple):
    print(race_tuple)
    time, distance = race_tuple
    print('time:', time)
    print('distance:', distance)
    count = 0
    for i in range(time):
        hold_bt = i
        velocity = hold_bt
        travel_time = time - hold_bt
        travelled_distance = velocity * travel_time
        print('hold_bt:', hold_bt)
        print('velocity:', velocity)
        print('travel_time:', travel_time)
        print('travelled_distance:', travelled_distance)
        if travelled_distance > distance:
            debugger = str(travelled_distance) + ' >= ' + str(distance)
            print(colored(debugger, 'red'))
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
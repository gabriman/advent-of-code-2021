import pathlib
import sys
from collections import Counter

def parse(puzzle_input):
    return [line for line in puzzle_input.splitlines()]

def rotate(table):
    return list(zip(*table[::-1]))

def calculateGammaEpsilon(line):
        c = Counter(line)
        zeros = c['0']
        ones = c['1']
        common = c.most_common()
        mostCommon = common[0];
        leastCommon = common[-1];
        return mostCommon[0], leastCommon[0], mostCommon[1] == leastCommon[1]

def part1(lines):
    tableRotated = rotate(lines)
    gamma = ''
    epsilon = ''

    for line in tableRotated:
        result = calculateGammaEpsilon(line)
        gamma += result[0]
        epsilon += result[1]
            
    gammaRate = int(gamma, 2)
    epsilonRate = int(epsilon, 2)

    return gammaRate * epsilonRate

def part2(lines):
    tableRotated = rotate(lines)
    oxygen = findLifeSupportRating(True, tableRotated[0], lines, 0)
    CO2 = findLifeSupportRating(False, tableRotated[0], lines, 0)

    oxygenRate = int(oxygen, 2)
    CO2Rate = int(CO2, 2)

    return oxygenRate * CO2Rate


# returns True if line has value in position
def check_value_in_position(line, pos, val):
    if line[pos] == val:
          return True  
    return False
    
# ox = True if oxygen, false if co2
# controlLine = column to check max/min
# values = filtered lines (not rotated)
# post = position checking
def findLifeSupportRating(ox, controlLine, values, pos):
    most, least, equals = calculateGammaEpsilon(controlLine)
    if (ox):
        controlValue = '1' if equals else most
    else:
        controlValue = '0' if equals else least
        
    newValues = list(filter(lambda x: check_value_in_position(x, pos, controlValue), values))

    if len(newValues) == 1:
        return newValues[0]
    # newValues = list(filter(lambda x: len(x) > 4, values))
    
    pos = pos + 1
    controlLine = rotate(newValues)[pos]
    return findLifeSupportRating(ox, controlLine, newValues, pos)






def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    path = "Input.txt"
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
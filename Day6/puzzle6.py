import pathlib
import sys
from collections import Counter
from operator import methodcaller

maxDaysOfLife = 7
initialAge = maxDaysOfLife - 1

class Fish:
    def __init__(self, age = initialAge, isParent = False):
        self.age = age
        self.isParent = isParent
    def reproduce(self):
        self.age = initialAge
        self.isParent = True
        child = Fish(initialAge + 2)
        return child
    def getOlder(self):
        self.age -=1

def parse(puzzle_input):
    line = puzzle_input.splitlines()[0]
    fishes = [int(fishValue) for fishValue in line.split(',')]
    return fishes

def part1(fishesData, days):
    fishes = [Fish(age) for age in fishesData]
    for day in range(days):
        newFishes = []
        for idx, fish in enumerate(fishes):
            if fish.age == 0:
                newFish = fish.reproduce()
                newFishes.append(newFish)
            else:
                fish.getOlder()
        fishes.extend(newFishes)
        del newFishes
    number = len(fishes)
    del fishes
    return number

# Instead of follow the lifeflow for every fish, when a fish has a children it follows a recurrent lifeflow (create a fish every 7 days)
# We will count the fishes by age, incrementing the age each day (decreasing the days to reproduce) and adding the one extra fish by fish at 0 
#   and reseting this fish to 6 (adding it to all the ones with age 6)
def part1_optimized(fishes, days):
    fishesByAges = {i:0 for i in range(maxDaysOfLife + 2)}
    for f in fishes:
        fishesByAges[f] += 1

    for day in range(days):
        inZero = fishesByAges[0]
        for i in range(len(fishesByAges)-1):
            fishesByAges[i] = fishesByAges[i+1]
        fishesByAges[6] += inZero
        fishesByAges[8] = inZero
    number = sum(fishesByAges.values())
    return number

def part2(fishes, days):
    return part1_optimized(fishes, days)

# 5934
def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    data1 = data[:]
    data2 = data[:]
    solution1 = part1(data1, 80)
    solution2 = part2(data2, 256)

    return solution1, solution2

if __name__ == "__main__":
    path = "Input.txt"
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
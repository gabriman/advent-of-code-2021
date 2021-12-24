import pathlib
import sys

def parse(puzzle_input):
    line = puzzle_input.splitlines()[0]
    positions = [int(val) for val in line.split(',')]
    return positions

def calculateFuel(positions, target):
    total = 0
    for p in positions:
        total += abs(p - target)
    return total

def calculateFuel_part2(positions, target):
    total = 0
    for p in positions:
        positionsToMove = abs(p - target)
        #formula = (n(n+1))/2
        total += int((positionsToMove * (positionsToMove + 1)) / 2)
    return total

def core(positions, calculateFunction):
    candidateFuel = 9999999999999999999
    candidateTarget = 0

    possible = range(min(positions),max(positions))
    for t in possible:
        targetFuel = calculateFunction(positions, t)
        if (targetFuel < candidateFuel):
            candidateFuel = targetFuel
            candidateTarget = t

    fuel = candidateFuel
    return fuel

def part1(positions):
    return core(positions, calculateFuel)

def part2(positions):
    return core(positions, calculateFuel_part2)

# 5934
def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    data1 = data[:]
    data2 = data[:]
    solution1 = part1(data1)
    solution2 = part2(data2)

    return solution1, solution2

if __name__ == "__main__":
    path = "Input.txt"
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
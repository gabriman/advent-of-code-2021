import pathlib
import sys
from collections import Counter
from operator import methodcaller

def parse(puzzle_input):
    lines = puzzle_input.splitlines()
    draw = [int(i) for i in lines[0].split(',')]

    bingos = []
    startLine = 2
    while (startLine + 5) <= len(lines):
        bingosplitted = [ [int(i) for i in x.split()]  for x in lines[startLine : startLine + 5]]
        bingos.append(Bingo(bingosplitted))
        startLine += 6

    return draw, bingos

def markDraw(draw, bingo):
    for idx, row in enumerate(bingo.data):
        row = [-1 if i == draw else i for i in row]
        bingo.data[idx] = row
    return bingo

def checkBingo(bingo):
    bingodata = bingo.data
    for idx, row in enumerate(bingodata):
        if bingodata[idx][idx] == -1:
            if sumRow(bingodata, idx) == -5:
                return True
            if sumColumn(bingodata, idx) == -5:
                return True
    return False

def sumColumn(m, idx):
    return sum([row[idx] for row in m])
    
def sumRow(m, idx):
    return sum(m[idx])
    
def sumBingo(bingo):
    total = 0
    for row in bingo.data:
        for val in row:
            if val != -1:
                total += val
    return total

def part1(draw, bingos):
    for number in draw:
        for idx, bingo in enumerate(bingos):
            bingos[idx] = markDraw(number, bingo)
            check = checkBingo(bingos[idx])
            if check:
                sum = sumBingo(bingos[idx])
                return sum * number
    return 0

def part2(draw, bingos):
    bingosRemaining = len(bingos)
    for number in draw:
        for idx, bingo in enumerate(bingos):
            if bingo.won:
                continue
            bingos[idx] = markDraw(number, bingo)
            check = checkBingo(bingos[idx])
            if check:
                bingos[idx].won = True
                bingosRemaining -= 1
                if bingosRemaining == 0:
                    sum = sumBingo(bingos[idx])
                    return sum * number
    return 0

class Bingo:
  def __init__(self, data):
    self.won = False
    self.data = data


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data[0],data[1])
    solution2 = part2(data[0],data[1])

    return solution1, solution2

if __name__ == "__main__":
    path = "Input.txt"
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
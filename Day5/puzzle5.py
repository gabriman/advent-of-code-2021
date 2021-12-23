import pathlib
import sys
from collections import Counter
from operator import methodcaller


class Line:
    def __init__(self, line):
        coordenates = list(map(lambda x : x.strip(),  line.split('->')))
        c1 = coordenates[0].split(',')
        c2 = coordenates[1].split(',')
        self.x1 = int(c1[0])
        self.y1 = int(c1[1])
        self.x2 = int(c2[0])
        self.y2 = int(c2[1])
        self.setHorizontalVertical()
    def setHorizontalVertical(self):
        self.horizontal = self.y1 == self.y2
        self.vertical = self.x1 == self.x2


def parse(puzzle_input):
    lines = puzzle_input.splitlines()
    lines = [Line(line) for line in lines]
    return lines

def total(matrix):
    total = 0
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            if matrix[i][j] > 1:
                total += 1
    return total

def part1(lines,includeDiagonals):
    matrix = [ [ 0 for i in range(1000) ] for j in range(1000) ]

    for line in lines:
        if line.horizontal:
            ma = max(line.x1, line.x2)
            mi = min(line.x1, line.x2)
            for x in list(range(mi, ma+1)):
                matrix[line.y1][x] += 1
        elif line.vertical:
            ma = max(line.y1, line.y2)
            mi = min(line.y1, line.y2)
            for y in list(range(mi, ma+1)):
                matrix[y][line.x1] += 1
        elif includeDiagonals:
            x_direction = 1 if line.x1 < line.x2 else -1
            y_direction = 1 if line.y1 < line.y2  else -1
            xrange = list(range(line.x1, line.x2 + x_direction, x_direction))
            yrange = list(range(line.y1, line.y2 + y_direction, y_direction))

            for i in range(len(xrange)):
                matrix[yrange[i]][xrange[i]] += 1


    return total(matrix)


def part2(lines):
    return 0


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data, False)
    solution2 = part1(data, True)

    return solution1, solution2

if __name__ == "__main__":
    path = "Input.txt"
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
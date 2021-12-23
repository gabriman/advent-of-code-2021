import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.splitlines()]

def part1(lines):
    h = 0
    depth = 0
    aim = 0
    for line in lines:
        lineList = line.split()
        if (lineList[0] == "forward"):
            h = h + int(lineList[1])
        elif lineList[0] == "down":
            depth = depth + int(lineList[1])
        elif lineList[0] == "up":
            depth = depth - int(lineList[1])

    return h * depth

def part2(lines):
    h = 0
    depth = 0
    aim = 0
    for line in lines:
        cmd, val = line.split()
        if (cmd == "forward"):
            h = h + int(val)
            depth = depth + (int(val) * aim)
        elif cmd == "down":
            aim = aim + int(val)
        elif cmd == "up":
            aim = aim - int(val)

    return h * depth

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
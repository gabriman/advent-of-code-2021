def sumPreviousValues(lines, index, count):
    return sum(lines[index-count+1:index+1])


print("Puzzle 2")

filename = "Input.txt";
with open(filename) as file:
    lines = file.readlines()
    lines = [int(line) for line in lines]

increaseCount = 0
startIndex = 2;

lastWindows = 999999999999999999999
for idx, val in enumerate(lines):
    if (idx < startIndex):
        continue
    currentWindow = sumPreviousValues(lines,idx, 3)

    isBigger = False
    if(currentWindow > lastWindows):
        isBigger = True
        increaseCount+=1;
    print(currentWindow,">",lastWindows,"?", isBigger)
    lastWindows = currentWindow

# for idx, val in enumerate(lines[startLine:]):
#     realIndex = idx + startLine;
#     if(lines[realIndex] > lines[realIndex-1]):
#         increaseCount+=1;

print(increaseCount)
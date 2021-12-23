print("Hello World")

filename = "Input.txt";
with open(filename) as file:
    lines = file.readlines()
    lines = [int(line) for line in lines]

increaseCount = 0
startLine = 1;
for idx, val in enumerate(lines[startLine:]):
    realIndex = idx + startLine;
    if(lines[realIndex] > lines[realIndex-1]):
        increaseCount+=1;

print(increaseCount)

with open("teleport.in", "r") as fin:
    line = fin.readline().strip().split(" ")
    a = int(line[0])
    b = int(line[1])
    x = int(line[2])
    y = int(line[3])
    print(a, b, x, y)
    
    answer = abs(a-b)
    
    answer = min(answer, abs(a-x) + abs(b-y), abs(a-y) + abs(b-x))

with open("teleport.out", "w") as fout:
    fout.write(str(answer))
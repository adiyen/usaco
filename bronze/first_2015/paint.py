with open("paint.in", "r") as fin:
    line1 = fin.readline().strip().split(" ")
    line2 = fin.readline().strip().split(" ")
    a = int(line1[0]); b = int(line1[1])
    c = int(line2[0]); d = int(line2[1])
    
answer = 0

for i in range(100):
    if i > a-1 and i < b:
        answer+=1
    elif i > c-1 and i < d:
        answer+=1

with open("paint.out", "w") as fout:
    fout.write(str(answer))
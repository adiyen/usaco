ids = []
entries = {}
counter = 0
with open("crossroad.in") as fin:
    numb_of_entries = int(fin.readline().strip())
    
    for i in range(numb_of_entries):
        line = fin.readline().strip().split(" ")
        if int(line[0]) not in ids:
            ids.append(int(line[0]))
            entries[int(line[0])] = int(line[1])
        elif int(line[0]) in ids and int(line[1]) != entries[int(line[0])]:
            entries[int(line[0])] = int(line[1])
            counter+=1

with open("crossroad.out", "w") as fout:
    fout.write(str(counter))
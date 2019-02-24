numbs = []
with open("sleepy.in", "r") as fin:
    n = int(fin.readline().strip())
    line = fin.readline().strip().split(" ")
    for i in range(n):
        numbs.append(int(line[i]))
        
for k in range(len(numbs)-1):
    if numbs[k] > numbs[k+1]:
        sorted = False
        break
    else:
        sorted = True
wrote = False       
if sorted == True:
    with open("sleepy.out", "w") as fout:
        fout.write("0")
        wrote = True
        
counter = 0
maximum = numbs[0]
max_idx = 0
for i in range(len(numbs)):
     if numbs[i] > maximum:
            maximum = numbs[i]
            max_idx = i
        
min_done = False
if numbs[0] == min(numbs):
    insert_numb = numbs.pop(0)
    numbs.insert(max_idx, insert_numb)
    counter+=1
    min_done = True
    print(numbs, counter)


done = False
while sorted == False:
    for i in range(len(numbs)):
        if numbs[0] == maximum and done == False:
            idx = len(numbs)
            done = True
            break
                 
        elif numbs[0] == min(numbs) and min_done == False:
            for l in range(len(numbs)):
                if numbs[l] == numbs[0] + 1:
                    idx = l-1
            break
        
        elif numbs[0] - numbs[i] == 1:
            idx = i

    insert_numb = numbs.pop(0)
    numbs.insert(idx, insert_numb)
    counter+=1
    print(numbs, counter)

    sorted = all(numbs[i] < numbs[i+1] for i in range(len(numbs)-1))

if wrote == False:
    with open("sleepy.out", "w") as fout:
        fout.write(str(counter))
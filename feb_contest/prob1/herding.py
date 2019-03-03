numbs = []
numbs1 = []

def is_consecutive(a, b, c):
    if a+1==b and b+1==c:
        return True
    elif a-1==b and b-1==c:
        return True
    return False

with open("herding.in", "r") as fin:
    line = fin.readline().strip().split(" ")
    bessie = int(line[0]); elsie = int(line[1]); mildred = int(line[2])
    #print(bessie, elsie, mildred)
    
    for i in range(3):
        numbs.append(int(line[i]))
        numbs1.append(int(line[i]))
    
    
#     for i in range(2):
#         if abs(numbs[i] - numbs[i+1]) == 2:\
# vals = []
# vals.append(abs(numbs[0]-numbs[1]))
# vals.append(abs(numbs[1]-numbs[2]))
# min_answer = min(vals)-1

# if min_answer == 0 and is_consecutive(numbs[0], numbs[1], numbs[2]) == False:
#     min_answer = 1

# print(min_answer)

# vals = []
# vals.append(abs(numbs[0]-numbs[1]))
# vals.append(abs(numbs[1]-numbs[2]))
# min_answer = min(vals)-1

# if min_answer == 0 and is_consecutive(numbs[0], numbs[1], numbs[2]) == False:
#     min_answer = 1

# print(min_answer)
counter = 0
if abs(numbs[1]-numbs[2]) == 2:
    counter+=1

else:
    while not is_consecutive(numbs[0], numbs[1], numbs[2]):
        if counter % 2 == 0:
            numbs.pop(0)
            numbs.insert(1, numbs[0]+2)
        else:
            numbs.pop()
            numbs.insert(1, numbs[0]+1)
        counter+=1
        
min_answer = counter
print(counter)

# while not is_consecutive(numbs[0], numbs[1], numbs[2]):
#     if counter % 2 == 0:
#         numbs.pop(0)
#         numbs.insert(1, numbs[0]+2)
#     else:
#         numbs.pop()
#         numbs.insert(1, numbs[0]+1)
#     counter+=1
# with open("herding.out", "w") as fout:
#     fout.write(str(find_min(numbs)))
#     fout.write('\n')
#     fout.write(str(find_max(numbs1)))

vals = []
vals.append(abs(numbs[0]-numbs[1]))
vals.append(abs(numbs[1]-numbs[2]))
answer = max(vals)-1

with open("herding.out", "w") as fout:
    fout.write(str(min_answer))
    fout.write('\n')
    fout.write(str(answer))
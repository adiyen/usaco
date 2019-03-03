def runner(N, arr, hoof, paper, scissors):
#     print(hoof, paper, scissors)
    counter = 0
    idx = 0
    while idx < N*2:
#         print("actions[idx]:", actions[idx])
#         print("actions[idx+1]", actions[idx+1])
        if arr[idx] == hoof and arr[idx+1] == scissors:
            counter=+1
        elif arr[idx] == paper and arr[idx+1] == hoof:
            counter+=1
        elif arr[idx] == scissors and arr[idx+1] == paper:
            counter+=1
        idx+=2
    return counter

vals = []
actions = []
# options = ["hoof", ""]        
with open("hps.in", "r") as fin:
    line = fin.readline().strip()
    N = int(line)
    #print(N)
    
    for i in range(N):
        line = fin.readline().strip().split(" ")
        actions.append(int(line[0])); actions.append(int(line[1]))

vals.append(runner(N, actions, 1, 2, 3))
vals.append(runner(N, actions, 1, 3, 2))
vals.append(runner(N, actions, 2, 1, 3))
vals.append(runner(N, actions, 2, 3, 1))
vals.append(runner(N, actions, 3, 1, 2))
vals.append(runner(N, actions, 3, 2, 1))

#print(vals)

with open("hps.out", "w") as fout:
    fout.write(str(max(vals)))
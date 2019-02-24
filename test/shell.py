shells = [False, False, False]

with open("shell.in", "r") as fin:
    n = int(fin.readline().strip())
    
answers = []
    
for j in range(3):
    correct = 0
    shells[0] = False; shells[1] = False; shells[2] = False
    
    shells[j] = True

    fin = open("shell.in", 'r')
    n = int(fin.readline().strip())
    for i in range(n):
        
        line = fin.readline().strip().split(" ")
        a = int(line[0]); b = int(line[1]); g = int(line[2])
        
        storage = shells[a-1]
        shells[abs(a-1)] = shells[abs(b-1)]
        shells[abs(b-1)] = storage
        
        if shells[abs(g-1)] == True:
            correct+=1

    fin.close()
    answers.append(correct)
    
with open("shell.out", "w") as fout:
    fout.write(str(max(answers)))
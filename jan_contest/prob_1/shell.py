answers = []
    
def runner(shells, a, b, g, points):
    fin = open("shell.in", "r")
    numb = int(fin.readline())
    
    for j in range(numb):
        line = fin.readline().strip().split(" ")
        a = int(line[0]); b = int(line[1]); g = int(line[2])

        storage = shells[a-1]
        shells[a-1] = shells[b-1]
        shells[b-1] = storage

        if shells[g-1] == True:
            points+=1
            
    fin.close() 
    return points

for i in range(3):
    points = 0
    
    shells[0] = False; shells[1] = False; shells[2] = False
    shells[i] = True
    
    points = runner(shells, a, b, g, points)
    answers.append(points)
    
with open("shell.out", "w") as fout:
    fout.write(str(max(answers)))
        
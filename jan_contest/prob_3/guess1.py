def same_checker(a1, a2):
    count = 0
    for f1 in a1:
        if f1 in a2:
            count+=1
    return count
    
entire_list = dict()
animals = []
 
with open("guess.in" , "r") as fin:
    numb_ani = int(fin.readline().strip())
    
    for i in range(numb_ani):
        list_arr = []
        
        line = fin.readline().strip().split(" ")
        numb_of_chars = int(line[1])
        
        for j in range(numb_of_chars):
            list_arr.append(line[2+j])
        entire_list[line[0]] = list_arr
        animals.append(line[0])
            
answers = []
for a1 in animals:
    numbs = []
    for a2 in animals:
        #print("a1:", a1, "a2:", a2)
        if a1 != a2:
            numb = same_checker(entire_list[a1], entire_list[a2])
            #print(a1, numb)
            numbs.append(numb)
    #print(numbs)
    answers.append(max(numbs))

with open("guess.out", "w") as fout:
    fout.write(str(max(answers)+1))
def same_checker(i, j, entire_list, animals):
    count = 0
    a1 = entire_list[animals[i]]
    a2 = entire_list[animals[j]]

    for k in range(len(a1)):
        if a1[k] in a2:
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
            
    largest = 0
    for i in range(numb_ani):
        for j in range(i+1, numb_ani):
            largest = max(largest, same_checker(i, j, entire_list, animals))
            
with open("guess.out", "w") as fout:
    fout.write(str(largest+1))
with open("guess.in", "r") as fin:
    phrases = []
    n = int(fin.readline().strip())
    for i in range(4):
        line = fin.readline().strip().split(" ")
        numb_of_phrases = int(line[1])
        for j in range(numb_of_phrases):
            phrases.append(line[2+j])
            
    # print(phrases)
    
common = []
for i in range(len(phrases)):
    for j in range(len(phrases)):
        if phrases[i] == phrases[j] and i != j and phrases[i] not in common:
            common.append(phrases[i])
# print(common)

with open("guess.out", "w") as fout:
    fout.write(str(len(common)+1))
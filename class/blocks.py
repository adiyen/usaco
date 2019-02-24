with open("blocks.in", "r") as fin:
    words = []
    n = int(fin.readline().strip())
    for i in range(n):
        line = fin.readline().strip().split(" ")
        words.append(line[0]); words.append(line[1])
    
letters = []
for i in range(n*2):
    for j in range(len(words[i])):
        if i == 0 or i % 2 == 0:
            letters.append(words[i][j])
        elif words[i][j] not in words[i-1]:
            letters.append(words[i][j])     

letter_numbs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(letters)):
    counter = 0
    for j in range(len(letters)):
        if ord(letters[i]) == ord(letters[j]):
            counter+=1

    letter_numbs[ord(letters[i])-97] = counter

with open("blocks.out", "w") as fout:
    for i in range(26):
        fout.write(str(letter_numbs[i]))
        fout.write('\n')
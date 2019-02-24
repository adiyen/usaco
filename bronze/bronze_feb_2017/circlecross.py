with open("circlecross.in", "r") as fin:
    string = fin.readline().strip()
crossed = []
counter = 0
# for i in range(1, 51):
#     if string[i]!= string[i-1] and string[i] != string[i+1]:
#         if string[i] not in crossed:
#             crossed.append(string[i])
# # answer = int(len(crossed)/2)

# for j in range(len(crossed)):
#     if j % 2 == 0:
#         if ord(crossed[j]) > ord(crossed[j+1]):
#             counter+=1
#     else:
#         if ord(crossed[j]) < ord(crossed[j-1]):
#             counter+=1
# answer = int(counter/2)

# with open("circlecross.out", "w") as fout:
#     fout.write(str(answer))

list = {}
for i in range(26):
    list[i+65] = 0
    
for i in range(1, 52):
    for j in range(i, 51):
        if string[j] != string[j+1] and j % 2 == 0:
            list[ord(string[i])]+=1
        if string[j] == string[i]:
            break
            
maximum = list[65]
for k in range(1, 26):
    if list[k+65] > maximum:
        maximum = list[k+65]
    
    

with open("circlecross.out", "w") as fout:
    fout.write(str(maximum))
persons, milks, times = [], [], []
sick_people, sick_times = [], []
possible_bad_milks = []

with open("badmilk.in", "r") as fin:
    line = fin.readline().strip().split(" ")
    N = int(line[0]); M = int(line[1]); D = int(line[2]); S = int(line[3])
    print(N, M, D, S)
    
    for i in range(D):
        line = fin.readline().strip().split(" ")
        persons.append(int(line[0]))
        milks.append(int(line[1]))
        times.append(int(line[2]))
    
    print(persons, milks, times)
    
    for j in range(S):
        line = fin.readline().strip().split(" ")
        sick_people.append(int(line[0]))
        sick_times.append(int(line[1]))
        
    print(sick_people, sick_times)

for i in range(M):
    if milks[i] not in possible_bad_milks:
        possible_bad_milks.append(milks[i])
        
for i in range(len(sick_people)):
    sick_person = sick_people[i]
    sick_time = sick_times[i]
    for j in range(len(times)):
        if times[j] > sick_time and persons[j] == sick_person:
            possible_bad_milks.remove(milks[j])
            
numbs = []
for j in range(N):
    counter = 0
    for i in range(len(milks)):
        if j == milks[i]:
            counter+=1
    numbs.append(counter)

with open("badmilk.out", "w") as fout:
    fout.write(str(max(numbs)))
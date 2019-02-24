allowed_segment, allowed_speed = [], []
bessie_segment, bessie_speed = [], []

with open("speeding.in", "r") as fin:
    line1 = fin.readline().strip().split(" ")
    N = int(line1[0]); M = int(line1[1])
    
    for i in range(N):
        line = fin.readline().strip().split(" ")
        allowed_segment.append(int(line[0]))
        allowed_speed.append(int(line[1]) )
    for j in range(M):
        line = fin.readline().strip().split(" ")
        bessie_segment.append(int(line[0]))
        bessie_speed.append(int(line[1]))

maximum = 0
counter = 0
for i in range(len(allowed_segment)):
    allowed_segment[i] = counter+allowed_segment[i]
    counter = allowed_segment[i]
    
counter = 0
for i in range(len(bessie_segment)):
    bessie_segment[i] = counter+bessie_segment[i]
    counter = bessie_segment[i]
    
allowed_numbs, bessie_numbs = [], []
i = 0; j = 0
while i < N or j < M:
    if allowed_segment[i] < bessie_segment[j]:
        allowed_numbs.append(allowed_speed[i])
        bessie_numbs.append(bessie_speed[j])
        i+=1
    elif allowed_segment[i] <= bessie_segment[j]:
        allowed_numbs.append(allowed_speed[i])
        bessie_numbs.append(bessie_speed[j])
        i+=1; j+=1
    else:
        allowed_numbs.append(allowed_speed[i])
        bessie_numbs.append(bessie_speed[j])
        j+=1
      
for i in range(len(allowed_numbs)):
    if bessie_numbs[i] > allowed_numbs[i]:
        maximum = max(maximum, bessie_numbs[i]-allowed_numbs[i])
            
with open("speeding.out", "w") as fout:
    fout.write(str(maximum))
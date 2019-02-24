with open("lostcow.in", "r") as fin:
    line = fin.readline().strip().split(" ")
    x = int(line[0]); y = int(line[1])

#     print(x, y)

farm_pos = x
counter = 1
steps = 0
prev_farm_pos = 0
if farm_pos < y:
    while farm_pos < y:
        prev_farm_pos = farm_pos
        farm_pos = x+counter
        print("prev:", prev_farm_pos, "pos:", farm_pos)
        steps+=abs(farm_pos-prev_farm_pos)
        #print("steps:", steps)

        counter*=-2
        
elif farm_pos > y:
    while farm_pos > y:
        prev_farm_pos = farm_pos
        farm_pos = x+counter
        print("prev:", prev_farm_pos, "pos:", farm_pos)
        steps+=abs(farm_pos-prev_farm_pos)
        #print("steps:", steps)

        counter*=-2
#print(farm_pos)

steps-=abs(farm_pos-y)
#print(steps)
with open("lostcow.out", "w") as fout:
    fout.write(str(steps))
#     print(steps)


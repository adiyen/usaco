cow_coming_time, amount_of_time = [], []

with open("cowqueue.in", "r") as fin:
    numb_of_cows = int(fin.readline().strip())
    
    for i in range(numb_of_cows):
        line = fin.readline().strip().split(" ")
        cow_coming_time.append(int(line[0]))
        amount_of_time.append(int(line[1]))
        
for i in range(numb_of_cows):
    for j in range(numb_of_cows):
        if cow_coming_time[i] < cow_coming_time[j]:
            storage_1 = cow_coming_time[i]
            storage_2 = amount_of_time[i]
            cow_coming_time[i] = cow_coming_time[j]
            amount_of_time[i] = amount_of_time[j]
            cow_coming_time[j] = storage_1
            amount_of_time[j] = storage_2

# maximum = cow_coming_time[0] + amount_of_time[0]     
max2_needed = True
maximum = 0
start_time = cow_coming_time[0]
for i in range(numb_of_cows-1):

    maximum = start_time+amount_of_time[i]

    if maximum >= cow_coming_time[i+1]:
        start_time = maximum
    else:
        start_time = cow_coming_time[i+1]
    #print(i, maximum)
# if maximum >= cow_coming_time[-1]:
#     maximum+=amount_of_time[-1]
maximum = start_time+amount_of_time[-1]

    
with open("cowqueue.out", "w") as fout:
    fout.write(str(maximum))
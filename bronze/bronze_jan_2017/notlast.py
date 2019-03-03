cows_names = []
cow_milk_numbs = []

cows = {
    "Bessie": 0,
    "Elsie": 0,
    "Daisy": 0,
    "Gertie": 0,
    "Annabelle": 0,
    "Maggie": 0,
    "Henrietta": 0
}

cows_arr = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]

with open("notlast.in", "r") as fin:
    line = fin.readline().strip()
    numb_of_entries = int(line)
    
    for i in range(numb_of_entries):
        line = fin.readline().strip().split(" ")
        cows_names.append(line[0]); cow_milk_numbs.append(int(line[1]))
    
for i in range(numb_of_entries):
    cows[cows_names[i]]+=cow_milk_numbs[i]
#print(cows)
    
tie = False
fmin, smin = 999999, 999999
fans, sans = "", ""
for name, val in cows.items():
    if val < fmin:
        smin, sans = fmin, fans
        fmin, fans = val, name
#     elif val < smin and val == fmin:
#         tie = True
    elif val < smin and val != fmin:
        smin, sans = val, name
    #print(fmin, fans, smin, sans)

# for i in range(len(cows_names)):
#     if cows[cows_names[i]] == smin and sans != cows_names[i]:
# #         print(smin, cows[cows_names[i]])
#         tie = True

new_cows = dict((y,x) for x,y in cows.items())
#print(cows)

for i in range(len(cows)):
#     print(cows[cows_arr[i]] == sans)
    if cows[cows_arr[i]] == smin and new_cows[smin] != cows_arr[i]:
        #print("true")
        tie = True

# used_numbs = []
# for i in range(len(cows)):
#     used_numbs.append(cows[cows_names[i]])

# print(used_numbs)


# for i in range(len(used_numbs)):
#     if 

# if numb_of_entries == 0:
#     tie = True
with open("notlast.out", "w") as fout:
    if not tie:
        fout.write(sans)
    else:
        fout.write("Tie")
    fout.write('\n')
"""
ID: krishna91
LANG: PYTHON3
TASK: friday
"""

def years(month_days, days, counter, day_numbs):
    day = days[counter]
    for j in range(12):
        day_numb = 1
        for i in range(month_days[j]):
            if day_numb == 13:
                day_numbs[day]+=1

            day_numb+=1
            if counter == 6:
                counter = 0
            else:  
                counter+=1

            day = days[counter]
    
    return day, counter

with open("friday.in", "r") as fin:
    N = int(fin.readline().strip())

day_numbs = {
    "Sat": 0,
    "Sun": 0,
    "Mon": 0,
    "Tues": 0,
    "Wed": 0,
    "Thurs": 0,
    "Fri": 0
}
days = ["Sat", "Sun", "Mon", "Tues", "Wed", "Thurs", "Fri"]
day = days[0]
counter = 2

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
number = 0

for i in range(N):
    if (1900+i) % 400 == 0:
        month_days[1] = 29
    
    elif (1900+i) % 4 == 0 and (1900+i) % 100 != 0:
        month_days[1] = 29
        
    else:
        month_days[1] = 28
        
    vals = years(month_days, days, counter, day_numbs)

    counter = int(vals[1])

res = ""
for day in days:
    res = res + f"{day_numbs[day]} "
res = res[:-1] + "\n"
print(res)
with open("friday.out", "w") as fout:
    fout.write(res)
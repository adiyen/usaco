"""
ID: krishna91
LANG: PYTHON3
TASK: ride
"""

fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
comet = fin.readline().strip()
group = fin.readline().strip()

comet_product = 1
group_product = 1
result = ''

for val in comet:
    ord_val = ord(val)-64
    comet_product*=ord_val
    
for val in group:
    ord_val = ord(val)-64
    group_product*=ord_val

comet_val = int(comet_product/47)
comet_mod = comet_product-(comet_val*47)

group_val = int(group_product/47)
group_mod = group_product-(group_val*47)

if group_mod == comet_mod:
    result = "GO"
    
else:
    result = "STAY"

fout.write(result + '\n')
fout.close()
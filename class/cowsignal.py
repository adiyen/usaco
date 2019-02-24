with open("cowsignal.in", "r") as fin:
    line1 = fin.readline().strip().split(" ")
    m = int(line1[0]); n = int(line1[1]); k = int(line1[2])
    string = []
    
    for i in range(m):
        line = fin.readline().strip()
        for j in range(n):
            string.append(line[j])

counter = 1


def writer(n, k, string_used):
    res = ""
    for j in range(k):
        res += str(string_used)
    return res
            
with open("cowsignal.out", "w") as fout:

    res = ""
    for ch in string:
        res += writer(n, k, ch)
        if counter % n*2 == 0:
            for i in range(k):
                fout.write(res)
                fout.write("\n")
                
            res = ""
        counter +=1
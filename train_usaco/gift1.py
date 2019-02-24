"""
ID: krishna91
LANG: PYTHON3
TASK: gift1
"""

persons = dict()
person_names = []

with open("gift1.in", "r") as fin:
    num_people = int(fin.readline().strip())
    print(num_people)
    for _ in range(num_people):
        name = fin.readline().strip()
        persons[name] = 0
        person_names.append(name)
    
    for j in range(num_people):
        person_name = fin.readline().strip()
        print(person_name)
        vals = fin.readline().strip().split(" ")
        give_amount = int(vals[0])
        num_receiver = int(vals[1])

        if num_receiver > 0:
            persons[person_name]-= give_amount - (give_amount % num_receiver)
            
            for i in range(num_receiver):
                name = fin.readline().strip()
                persons[name]+= int(give_amount/num_receiver)
                
with open("gift1.out", "w") as fout:
    for name in person_names:
#         print(name, persons[name])
        fout.write("{name} {val}\n".format(name=name, val=persons[name]))
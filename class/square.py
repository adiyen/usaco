with open("square.in", "r") as fin:
    rect_1 = []
    rect_2 = []
    line1 = fin.readline().strip().split(" ")
    line2 = fin.readline().strip().split(" ")
    
    for i in range(4):
        rect_1.append(int(line1[i]))
        rect_2.append(int(line2[i]))
            
r1_x1, r1_y1, r1_x2, r1_y2 = rect_1
r2_x1, r2_y1, r2_x2, r2_y2 = rect_2

x_min = min(r1_x1, r1_x2, r2_x1, r2_x2)
x_max = max(r1_x1, r1_x2, r2_x1, r2_x2)

y_min = min(r1_y1, r1_y2, r2_y1, r2_y2)
y_max = max(r1_y1, r1_y2, r2_y1, r2_y2)

x = x_max-x_min
y = y_max-y_min

numb = max(x, y)
answer = numb*numb

with open("square.out", "w") as fout:
    fout.write(str(answer))
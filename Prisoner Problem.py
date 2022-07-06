import random

count = 100
open_count = count//2

rs_count = 0
ls_count = 0
trials = 1000000

for trial in range(trials):
    boxes = list(range(count))
    #print(boxes)
    random.shuffle(boxes)

    #print(boxes)

    # random select strategy
    rs = True
    for p in range(count):
        if p not in random.sample(boxes, open_count):
            rs = False
            break

    # loop strategy
    ls = True
    for p in range(count):
        #print("prisoner:",p)
        i = boxes[p]
        opens = 1
        #print("   ",opens,"select box",0,"opens",i)
        while i != p and opens < open_count:
            i_old = i
            i = boxes[i]
            opens += 1
            #print("   ",opens,"select box",i_old,"opens",i)
        if i != p:
            ls = False
            break
    
    rs_count += rs
    ls_count += ls
    #print("trial:",trial)
    #print("    rand:","pass" if rs else "fail", "loop:","pass" if ls else "fail")

print("\n"+"*"*50)
print("rand success:",rs_count,"/",trials)
print("     ratio:  ",round(rs_count/trials, 3)*100,"%")
print("loop success:",ls_count,"/",trials)
print("     ratio:  ",round(ls_count/trials, 3)*100,"%")
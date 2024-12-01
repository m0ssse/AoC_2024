def part1(list1, list2):
    list1.sort()
    list2.sort()
    res = 0
    for x, y in zip(list1, list2):
        res+=abs(x-y)
    print(res)

def part2(list1, list2):
    list2_counts = {}
    for x in list2:
        if x not in list2_counts:
            list2_counts[x] = 0
        list2_counts[x]+=1
    res = 0
    for num in list1:
        if num in list2_counts:
            res+=num*list2_counts[num]
    print(res)


inputfile = "input1.txt"
list1, list2 = [], []
with open(inputfile) as myinput:
    for line in myinput:
        x, y = [int(x) for x in line.split()]
        list1.append(x)
        list2.append(y)
    
part1(list1, list2)
part2(list1, list2)
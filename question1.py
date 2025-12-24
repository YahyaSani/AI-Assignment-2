list =[1,[2,[3,4,],5],6]
def sum(list):
    total = 0
    for i in list:
        if(type(i) is list):
            for j in i:
                if(type(j) is list):
                    for k in j:
                        total = total + k
                else:
                    total = total + j
        else:
            total = total + i
    return sum
print(sum(list))

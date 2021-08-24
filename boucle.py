mat = [[1,2],[3,4],[5,6]]

i = 1;
j = 1;
for lig in mat:
    for cell in lig:
        print("{:>4d} {:>4d}".format(i,j))
        j+=1
        # print("{:>4}".format(cell),end="")
    i+=1
    j=1

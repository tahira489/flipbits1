def powerset(set, set_size):
    power_set_size = 2**set_size
    outer = 0
    inner = 0
    for outer in range(0, power_set_size):
        for inner in range(0,set_size):
            if (outer &(1<<inner)):
                print(set[inner],end="")
        print("")

set=[]
size = int(input("enter the total elements:"))
for i in range(0,size):
    n = int(input("enter the element:"))
    set.append(n)
powerset(set,size)
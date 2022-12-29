import random

# insert a value or array of values to split
A = [80, 88, 98, 98, 80, 80, 90, 98, 98, 80, 80, 98, 80, 80, 98, 98, 80, 98, 80, 98, 80, 80, 75, 80, 80, 98, 98, 80, 98, 75, 80, 80]

# function to split value to sum of Y random values
# change split array length to number of values you want to split to
# change Y in range(Y) to match with split array length
# change a,b in random.randint(a, b) to set the range (lowest-highest) of random values to be generated
def split_value(value):
    split = [0, 0, 0, 0, 0]
    while sum(split) != value:
        for i in range(5):
            split[i] = random.randint(1, 20)
    return split

# print sorted array of split values
for x in A:
    value = x
    split = split_value(value)
    sorted_array = sorted(split, reverse=True)
    print(sorted_array)
# Problem-4:  Get the total count of number list in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
#     (examples)
#     input: [1,2,8,9,12,46,76,82,15,20,30]
#     Output:
#         {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}


# solution 4:

inp = map(int, input("Enter a list of numbers: ").split())
d = {}
for i in inp:
    for multiple in [1,2,3,4,5,6,7,8,9]:
        if i%multiple == 0:
            if multiple in d:
                d[multiple] += 1
            else:
                d[multiple] = 1
print(d)
# WAP to sort the numbers in a list in assending order by loop.

ls = [7,5,8,3,4,2]  # expected output = [2,3,4,5,7,8]

for i in range(0, len(ls)):
    for j in range(i+1, len(ls)):
        if ls[i] > ls[j]:
            temp = ls[i]
            ls[i] = ls[j]
            ls[j] = temp

print(ls)
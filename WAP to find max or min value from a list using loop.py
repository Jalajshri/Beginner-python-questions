# WAP to find max or min value from a list using loop.

ls=[10,40,56,87,35,20,34,67,23,65,12]
max = 0 
min = ls[0]

for i in ls:
    if i > max:
        max = i
    if i < min:
        min = i

print(f"Maximum no from given list is {max} and Minimum value from the list is {min} ")



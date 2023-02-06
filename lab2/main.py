from euler import Euler

"""
Algorithm for computing the value of Euler’s function for natural numbers. For a given value
v and a given bound b, list all natural numbers less than b which have v as the value of Euler’s
function.
"""


value = int(input("Enter the value >>> "))
bound = int(input("Enter the bound >>> "))

result = []

for i in range(1, bound):
    if Euler.find_euler_value(i) == value:
        result.append(i)

print(f"The numbers that are less than {bound} and have the value of the Euler's function equal to {value} are: ")
print(result)



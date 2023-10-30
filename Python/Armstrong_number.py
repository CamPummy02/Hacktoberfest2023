"""

print armstrong number within a range without using 
import math and def in the code ,using only loop

"""
start = int(input("Enter the start range"))
end = int(input("Enter the end range"))
for num in range(start, end):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit**order
        temp //= 10
        if num == sum:
            print(num)
            break
        else:
            continue

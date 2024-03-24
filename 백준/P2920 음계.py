import sys

input_str=sys.stdin.readline().strip()
numbers = input_str.split()
numbers = list(map(int, numbers))
ascList = sorted(numbers)
desList = sorted(numbers, reverse=True)

if numbers == ascList :
    print("ascending")
elif numbers == desList :
    print("descending")
else :
    print("mixed")

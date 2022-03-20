#second level
print("Pleaze enter a number")
n = int(input())
print("enter list")
# arr_in = input()
arr = map(int, input().split())
arr2 = set(arr) #remove duplicate
arr2 = list(arr2) # list
m = max(arr2) # get max value
arr2.remove(m)
print(max(arr2))


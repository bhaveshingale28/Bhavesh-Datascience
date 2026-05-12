import statistics

nums = [10, 20, 30, 40, 50]

mid = statistics.median(nums)

a, b = map(int, input("Enter numbers: ").split())

def add(a, b):
    return a + b

total = add(a, b)

if total > mid:
    print(set(nums[:nums.index(mid)]))

elif total == mid:
    print({nums.index(mid): mid})

else:
    print(tuple(nums[nums.index(mid):]))
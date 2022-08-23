from re import T


while True:
    nums = input()
    if not int(nums):
        break
    ints = []
    for i in nums:
        ints.append(int(i))
    print(sum(ints))
nums = [x for x in input("enter desired numbers: ").split(",")]

oddNums = [x for x in nums if int(x) % 2 == 1]

print(", ".join(oddNums))
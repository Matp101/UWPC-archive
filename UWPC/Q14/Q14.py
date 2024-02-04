def findSublists(nums, target):
    target = int(target)
    nums = [int(num) for num in nums.split()]
    found_sublists = []

    for i in range(len(nums)):
        sum_so_far = 0
        for j in range(i, len(nums)):
            sum_so_far += nums[j]
            if sum_so_far == target:
                found_sublists.append(nums[i:j+1])

    return found_sublists

test_cases = [
    ["3 4 -7 1 3 3 1 -4", "7"],
    ["-1 0 1 2 3 4 5 6", "5"],
]
results = [findSublists(*case) for case in test_cases]
for case, result in zip(test_cases, results):
    print(f"findSublists({case}) = {result}")


## Generating test cases
#from TestCaseHandler import TestCaseHandler
#test_cases = [
#    ["1 1 1 2 2 2 3 3 3", "7"],
#    ["-2 0 2 4 6 8", "12"],
#    ["1 1 3 3 5 5 7 7", "11"],
#    ["1 1 1 1 1 1 1", "5"],
#]
#results = [findSublists(*case) for case in test_cases]
#handler = TestCaseHandler(14, test_cases, results)
#handler.write_to_files()
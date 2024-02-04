def input_to_array(input_list):
    input_str = input_list[0]
    array = input_str.split()
    return [int(num) for num in array]

def moveZeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
        if nums[slow] != 0:
            slow += 1
    return nums

# Testing with the provided samples
test_cases = [["0 1 0 3 12"], ["0"], ["0 0 1 0 2 0 3 2"]]
results = [moveZeroes(input_to_array(case)) for case in test_cases]
for case, result in zip(test_cases, results):
    print(f"moveZeroes({input_to_array(case)}) = {result}")

## Generating test cases
#from TestCaseHandler import TestCaseHandler
#test_cases = [["1 2 3 50 3 0"], ["1"], ["0 0 1 2 3 0 0 2 3 0"]]
#results = [moveZeroes(input_to_array(case)) for case in test_cases]
#handler = TestCaseHandler(2, test_cases, results)
#handler.write_to_files()
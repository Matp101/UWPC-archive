def jump(nums):
    max_reach, n = 0, len(nums)
    for i, jump_length in enumerate(nums):
        if i > max_reach:
            return "false"
        max_reach = max(max_reach, i + jump_length)
        if max_reach >= n - 1:
            return "true"
    return "false"


test_cases = [
    "2 3 1 1 4",
    "3 2 1 0 4"
]
results = [jump(list(map(int, case.split()))) for case in test_cases]
for case, result in zip(test_cases, results):
    print(f"jump({case}) = {result}")

# Generating test cases
from TestCaseHandler import TestCaseHandler
test_cases = [
    "1 2 3 2 1 1",
    "1 1 1 1 0 1",
    "2 2 3 2 1 0 1 2 3",
    "1 1 1 1 1 1 1 1 1",
    "2 2 3 1 2 3 4 2 1",
]
results = [jump(list(map(int, case.split()))) for case in test_cases]
handler = TestCaseHandler(19, test_cases, results)
handler.write_to_files()
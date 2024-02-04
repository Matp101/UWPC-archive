import math

def spiraldistance(pos):
    if pos == 1:
        return 0
    prev = int(math.sqrt(pos))
    if prev % 2 == 0:
        prev -= 1
    sidelength = prev + 1
    offset = (pos - (prev ** 2)) % sidelength
    middle = sidelength // 2
    return middle + abs(middle - offset)

# Testing with the provided samples
test_cases = [1, 12, 23]
results = [spiraldistance(case) for case in test_cases]
for case, result in zip(test_cases, results):
    print(f"spiraldistance({case}) = {result}")

## Generating test cases
#from TestCaseHandler import TestCaseHandler
#test_cases = [1, 2, 50, 25, 1024, 10, 3]
#results = [spiraldistance(case) for case in test_cases]
#handler = TestCaseHandler(15, test_cases, results)
#handler.write_to_files()
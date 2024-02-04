def readinput(s):
    return [[int(x) for x in row.split()] for row in s]

def twoCitySchedCost(costs):
    refund = []
    N = len(costs)//2
    minCost = 0
    for A, B in costs:
        refund.append(B - A)
        minCost += A
    refund.sort()
    for i in range(N):
        minCost += refund[i]
    return minCost

# Testing with the provided samples
test_cases = [
    ["10 20", "30 200", "400 50", "30 20"],
    ["259 770", "448 54", "926 667", "184 139", "840 118", "577 469"],
    ["515 563", "451 713", "537 709", "343 819", "855 779", "457 60", "650 359", "631 42"]
]
results = [twoCitySchedCost(readinput(case)) for case in test_cases]
for case, result in zip(test_cases, results):
    print(f"twoCitySchedCost({case}) = {result}")

# Generating test cases
from TestCaseHandler import TestCaseHandler
test_cases = [
    ["1 2", "3 4", "5 6", "7 8"],
    ["100 200", "300 400", "500 600", "700 800", "900 1000", "1100 1200"],
    ["231 742", "761 762", "627 830", "222 333"],
    ["20 40", "10 30", "11 31", "21 41", "22 42", "12 32"]
]
results = [twoCitySchedCost(readinput(case)) for case in test_cases]
handler = TestCaseHandler(6, test_cases, results)
handler.write_to_files()
def min_fishing_speed(s: str, h: str) -> int:
    def can_finish(speed):
        time_needed = 0
        for fish in nets:
            time_needed += -(-fish // speed)  # Equivalent to ceil(fish / speed)
        return time_needed <= hours

    nets = [int(fish) for fish in s.split()]
    hours = int(h)

    low, high = 1, max(nets)
    while low < high:
        mid = (low + high) // 2
        if can_finish(mid):
            high = mid
        else:
            low = mid + 1
    return low

test_cases = [
    ["3 6 7 11", "8"], 
    ["30 11 23 4 20", "5"], 
    ["30 11 23 4 20", "6"]
]
results = [min_fishing_speed(*case) for case in test_cases]
for case, result in zip(test_cases, results):
    print(f"min_fishing_speed({case}) = {result}")

# Generating test cases
from TestCaseHandler import TestCaseHandler
test_cases = [
    ["5 10 15", "3"],
    ["1 2 3 4 5", "5"],
    ["20 20 20", "2"],
    ["10", "1"],
    ["100 200 300", "10"],
    ["8 8 8 8 8", "4"],
    ["12 15 18 21", "7"]
]
results = [min_fishing_speed(*case) for case in test_cases]
handler = TestCaseHandler(17, test_cases, results)
handler.write_to_files()
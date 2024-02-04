def merge_and_sort_lists(list1_str, list2_str):
    list1 = list1_str.split()
    list2 = list2_str.split()
    merged_list = sorted(list1 + list2)
    return ' '.join(merged_list)

test_cases = [
    [["tomato", "apple", "banana"], ["rug", "shirt", "llama"]],
    [["a", "b", "c"], ["aa", "bb"]]
]
results = [merge_and_sort_lists(" ".join(case[0]), " ".join(case[1])) for case in test_cases]
for case, result in zip(test_cases, results):
    print(f"merge_and_sort_lists({case}) = {result}")


## Generating test cases
#from TestCaseHandler import TestCaseHandler
#test_cases = [
#    [["to", "pass", "tsin"], ["a", "cow"]],
#    [["hello", "world"], ["today", "is", "a", "good", "day"]],
#    [["dog", "cat", "horse"], ["sheep", "chicken", "cow"]],
#    [["u", "windsor", "school"], ["c", "ss", "uwpc"]]
#]
#results = [merge_and_sort_lists(" ".join(case[0]), " ".join(case[1])) for case in test_cases]
#handler = TestCaseHandler(13, test_cases, results)
#handler.write_to_files()
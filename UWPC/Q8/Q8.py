def correct_signal_error(messages):
    column_counts = [{} for _ in range(len(messages[0]))]
    for msg in messages:
        for i, char in enumerate(msg):
            column_counts[i][char] = column_counts[i].get(char, 0) + 1
    corrected_message = ''
    for column in column_counts:
        max_char = max(column, key=column.get)
        corrected_message += max_char

    return corrected_message

# Testing with the provided samples
test_cases = [
    [ "eedadn", "drvtee", "eandsr", "raavrd", "atevrs", "tsrnev", "sdttsa", "rasrtv", "nssdts", "ntnada", "svetve", "tesnvt", "vntsnd", "vrdear", "dvrsen", "enarar"],
    ["uqgc", "uwpc", "wwpc", "ugec"]
]
results = [correct_signal_error(case) for case in test_cases]
for case, result in zip(test_cases, results):
    print(f"correct_signal_error({case}) = {result}")

# Generating test cases
from TestCaseHandler import TestCaseHandler
test_cases = [
    ["mathew", "mathew", "mathew", "mathew", "mathew", "mathew"], 
    ["hepkp", "halna", "relgs", "pylrd", "hewlf", "hejuu", "ggglo", "kvklo"], 
    ["warcd", "abced", "wcbad", "boelw", "dlrow", "fffff", "horrr", "qpfld"],
    ["paaa", "pbbb", "cocc", "dodd", "eeoe", "ffof", "gggp", "gggp"],
]
results = [correct_signal_error(case) for case in test_cases]
handler = TestCaseHandler(8, test_cases, results)
handler.write_to_files()
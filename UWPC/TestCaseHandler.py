class TestCaseHandler:
    def __init__(self, question_number, test_cases, results):
        self.question_number = question_number
        self.test_cases = test_cases
        self.results = results

    def write_to_files(self):
        for i, (test_case, result) in enumerate(zip(self.test_cases, self.results)):
            # If test_case is a list, join the elements with spaces
            if isinstance(test_case, list):
                #test_case = "\n".join(map(str, test_case))
                test_case = " ".join(map(str, test_case))

            # If result is a list, convert each element to a string and then join them
            if isinstance(result, list):
                #result = "\n".join(map(str, result))
                result = " ".join(map(str, result))

            test_case_file = f"Q{self.question_number}.t{i+1}.in"
            result_file = f"Q{self.question_number}.t{i+1}.ans"

            with open(test_case_file, 'w') as f:
                f.write(str(test_case))

            with open(result_file, 'w') as f:
                f.write(str(result))
        self.cleanup()
    
    def cleanup(self):
        import shutil
        shutil.rmtree('__pycache__')


## Example usage:
# question_number = 1
# test_cases = ["input1", "input2", "input3"]
# results = ["output1", "output2", "output3"]
# 
# handler = TestCaseHandler(question_number, test_cases, results)
# handler.write_to_files()

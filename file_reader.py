import re

class FileReader:
    def __init__(self, filepath : str, encoding = 'utf-8'):
        self.filepath = filepath
        self.encoding = encoding

    def read_lines(self) -> list[str]:
        with open(self.filepath, 'r', encoding = self.encoding) as f:
            return f.readlines()

    def extract_data(self, number : int) -> list[list[int]]:
        lines = self.read_lines()
        list_of_numbers = []
        for line in lines:
            numbers_in_Line = [int(x) for x in re.findall(r'\d+', line)]
            list_of_numbers.append(numbers_in_Line)

        dataset_dict = {}
        for i in range(len(list_of_numbers)):
            if len(list_of_numbers[i]) == 1:
                dataset_number = list_of_numbers[i][0]
                dataset_dict[dataset_number] = [list_of_numbers[i+1], list_of_numbers[i+2]]

        return dataset_dict.get(number)


    def extract_length_and_capacity(self) -> list[int]:
        lines = self.read_lines()
        length_and_capacity = [int(x) for x in re.findall(r'\d+', lines[0])]
        return length_and_capacity
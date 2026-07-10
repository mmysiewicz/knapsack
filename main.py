import random
from file_reader import FileReader
from knapsack_service import KnapsackService


def main():
    file_reader = FileReader("knapsack.txt")
    data_set = file_reader.extract_data(random.randint(1, 15))
    knapsack_service = KnapsackService(file_reader.extract_length_and_capacity()[0], file_reader.extract_length_and_capacity()[1], data_set)

    list_of_knapsack = knapsack_service.greedy()
    for item in list_of_knapsack:
        print(item)

    print("\n")

    list_of_knapsack = knapsack_service.dynamic()
    for item in list_of_knapsack:
        print(item)

if __name__ == "__main__":
    main()
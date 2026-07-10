
class KnapsackService:
    def __init__(self, length: int, capacity: int, dataset : list[list[int]]):
        self.length = length
        self.capacity = capacity
        self.dataset = dataset

    def greedy(self):
        total_capacity = self.capacity
        total_value = 0
        list_of_items = []
        sizes = self.dataset[0]
        values = self.dataset[1]

        value_density = {}
        for i in range(self.length):
            value_density[i] = values[i] / sizes[i]

        value_density = dict(sorted(value_density.items(), key=lambda x: x[1], reverse=True))

        for index, density in value_density.items():
            if sizes[index] <= total_capacity:
                total_capacity -= sizes[index]
                total_value += values[index]
                list_of_items.append((index, sizes[index], values[index]))

        list_of_items.append(total_value)
        list_of_items.append(self.capacity - total_capacity)
        return list_of_items

    def dynamic(self):
        list_of_items = []
        sizes = self.dataset[0]
        values = self.dataset[1]

        rows = self.length + 1
        columns = self.capacity + 1
        array: list[list[int]] = [[0 if (row == 0 or col == 0) else -1 for col in range(columns)] for row in range(rows)]

        for row in range(1, rows):
            for column in range(1, columns):
                difference = column - sizes[row - 1]
                val = values[row - 1]
                if difference > 0:
                    difference_value = array[row - 1][difference]
                    val += difference_value
                elif difference < 0:
                    val = 0
                new_val = max(val, array[row-1][column])
                array[row][column] = new_val

        total_value = array[rows-1][columns-1]

        row = self.length
        column = self.capacity
        while row > 0 and column > 0:
            if array[row][column] != array[row-1][column]:
                list_of_items.append((row-1, sizes[row-1], values[row-1]))
                column -= sizes[row-1]
            row -= 1

        total_capacity = sum(size for i, size, value in list_of_items)
        list_of_items.append(total_value)
        list_of_items.append(total_capacity)
        return list_of_items


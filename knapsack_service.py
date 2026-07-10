
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






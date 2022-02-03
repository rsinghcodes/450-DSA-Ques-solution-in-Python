# Ques -> Find the maximum and minimum element in an array

# Implement using Function

def maxAndminInArray(arr):
    max = min = arr[0]
    for i in arr:
        if i > max:
            max = i
        elif i < min:
            min = i
    print("Max " + str(max))
    print("Min " + str(min))

# Implement using class (oop)

class MinMax:
    def __init__(self):
        self.max = 0
        self.min = 0

    def maxAndminInArray(self, arr):
        self.max = self.min = arr[0]

        for i in arr:
            if i > self.max:
                self.max = i
            elif i < self.min:
                self.min = i


array = [66, 87, 54, 52, 14, 10, 00, 56, 44, 55, 99]

test = MinMax()
test.maxAndminInArray(array)
print("Min value " + str(test.min))
print("Max value " + str(test.max))
import numpy as np


class Rug:
    def __init__(self, size):
        self.size = size

    def representation(self):
        if self.size % 2 == 0:
            print("The size of the Rug must be an Odd Integer.")
        else:
            matrix = np.zeros((self.size, self.size))
            for i in range(self.size):
                for j in range(self.size):
                    matrix[i][j] = max(abs(self.size // 2 - i), abs(self.size // 2 - j))
            print(matrix)


rug = Rug(size=9)
rug.representation()

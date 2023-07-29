from membar import MemBar
import numpy as np

def test_membar():
    ram = MemBar(total=10, total_ram=2)
    for i in range(10):
        size = np.random.randint(10000)
        a = np.random.rand(size, size)
        b = np.random.rand(size, size)
        c = np.dot(a, b)
        ram.update()


if __name__ == "__main__":
    test_membar()

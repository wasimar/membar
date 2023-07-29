# MemBar
A usage bar to the console that shows the current memory usage and the peak memory usage.

**Note:**  Mesuring the memory usage is not always accurate. The memory usage is measured using the `psutil` package. For more information, see [this](https://psutil.readthedocs.io/en/latest/#psutil.Process.memory_info) page.

## Known Issue
- The total available memory reported by `psutil` for [WSL](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) users is not same as actual system memory due to virtualization. Use the `total_ram` parameter to set the total available memory manually.

## Installation
```bash
pip install git+https://github.com/wasimar/membar.git
```

## Usage
See the [example.py](example.py) file.
Or you can use it like this:

```python
from membar import MemBar
ram = MemBar(total=10, total_ram=2)
sizes = np.random.randint(3000, 6000, 10)
for i in sizes:
    a = np.random.rand(i, i)
    c = np.dot(a, a)
    ram.update()
```
Here, the `total` parameter is the total number of iterations and `total_ram` is the total amount of memory permitted in GB (default: total system memory). The `update` method updates the bar and shows the current memory usage and the peak memory usage. The output will be something like this:

![demo](doc/demo-gif.gif)

The bars are colored based on the memory usage. The colors are: 
- Green: less than 50% of the total memory
- Yellow: between 50% and 80% of the total memory
- Red: more than 80% of the total memory
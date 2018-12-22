import numpy as np
from BubbleSort import BubbleSort

BS = BubbleSort.BubbleSort

# Shuffling a sorted list
test_arr = np.arange(50)
np.random.shuffle(test_arr)

# Sort the array 
test = BS(test_arr)
test.bubbleRun(show=True, scale=10, fps=100)

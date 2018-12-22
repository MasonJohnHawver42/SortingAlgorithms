import numpy as np
from BubbleSort import BubbleSort
import cv2

img = np.zeros((750, 750, 3), np.uint8)

font = cv2.FONT_HERSHEY_PLAIN
white = (255, 255, 255)

cv2.putText(img, 'Bubble Sort', (10, 40), font, 2, white, 2)
cv2.putText(img, 'By: Mason J. Hawver (@ https://github.com/MasonOfTheHawverFamily)', (10, 60), font, 1, white, 1)

# Display the image
while True:
    cv2.imshow("BubbleSort", img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        done = True
        break


BS = BubbleSort.BubbleSort

test_arr = np.arange(75)
np.random.shuffle(test_arr)
print(test_arr)

test = BS(test_arr)
test.bubbleRun(show=True, scale=10, fps=100)
print(test.unsortedList)

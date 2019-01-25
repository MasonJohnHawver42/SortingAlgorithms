import numpy as np
import CocktailShakerSort
import cv2

img = np.zeros((1200, 1200, 3), np.uint8)

font = cv2.FONT_HERSHEY_PLAIN
white = (255, 255, 255)

cv2.putText(img, 'Cocktail Sort', (10, 40), font, 2, white, 2)
cv2.putText(img, 'By: Mason J. Hawver (@ https://github.com/MasonJohnHawver42)', (10, 60), font, 1, white, 1)


cv2.imshow("CS", img)
cv2.waitKey(0)


CSS = CocktailShakerSort.CocktailShakerSort

test_arr = np.arange(0, 75, 1)
np.random.shuffle(test_arr)
print(test_arr)

test = CSS(test_arr)
test.CocktailShakerSorter(16, True)
print(test.unsortedArr)

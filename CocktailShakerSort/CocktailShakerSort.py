import numpy as np
import cv2


class CocktailShakerSort:
    def __init__(self, arr=np.array([])):
        self.unsortedArr = arr
        self.MAX = np.amax(self.unsortedArr)
        self.done = False

    def sortOnceForward(self, start, stop, scale, show):
        for i in range(start, stop):
            next_i = i + 1
            if not (next_i > (stop - 1)):
                if self.unsortedArr[i] > self.unsortedArr[next_i]:
                    val = self.unsortedArr[i]
                    self.unsortedArr[i] = self.unsortedArr[next_i]
                    self.unsortedArr[next_i] = val
                if show:
                    arr = self.toImg(scale)
                    cv2.imshow("CocktailShakerSort", arr)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        self.done = True

    def sortOnceBackwards(self, start, stop, scale, show):
        for i in range(start, stop, -1):
            next_i = i - 1
            if next_i > stop:
                if self.unsortedArr[i] < self.unsortedArr[next_i]:
                    val = self.unsortedArr[i]
                    self.unsortedArr[i] = self.unsortedArr[next_i]
                    self.unsortedArr[next_i] = val
                if show:
                    arr = self.toImg(scale)
                    cv2.imshow("CocktailShakerSort", arr)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        self.done = True

    def CocktailShakerSorter(self, scale, show):
        start = 0
        stop = self.unsortedArr.shape[0]

        i = 0
        while stop > start:
            if i%2 == 1:
                self.sortOnceForward(start, stop, scale, show)
                stop -= 1
            elif i%2 == 0:
                self.sortOnceBackwards(stop - 1, start - 1, scale, show)
                start += 1

            if self.done:
                break
            i += 1

    def toImg(self, scale=10):
        arr = np.zeros((self.unsortedArr.shape[0], self.MAX))
        for i in range(self.unsortedArr.shape[0]):
            val = self.unsortedArr[i]
            arr[i] = ((np.arange(self.MAX) < val) * 140) + ((np.arange(self.MAX) == val) * 0) + ((np.arange(self.MAX) > val) * 240)


        arr = arr.repeat(3).reshape((self.unsortedArr.shape[0], self.MAX, 3))
        arr = cv2.resize(arr, dsize=(int(arr.shape[1] * scale), int(arr.shape[0] * scale)), interpolation=0)
        arr = np.rot90(arr)

        return arr.astype(np.uint8)
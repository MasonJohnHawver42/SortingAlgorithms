import numpy as np
import cv2


class BubbleSort:
    def __init__(self, lst=np.zeros(0)):
        self.unsortedList = lst
        self.MAX = np.amax(self.unsortedList) + 1

    def bubbleOnce(self, end, show=False, scale=10, fps=1000):
        done = False

        for index in np.arange(end, self.unsortedList.shape[0])[::-1]:
            next_index = index - 1
            next_index = ((next_index >= end) * next_index) + ((next_index < end) * end)
            val = self.unsortedList[index]
            next_val = self.unsortedList[next_index]
            if val < next_val:
                self.unsortedList[index] = next_val
                self.unsortedList[next_index] = val

            if show:
                arr = self.toImg(scale)
                arr[:, next_index * scale: index * scale] = np.array([0, 0, 255])
                cv2.imshow("BubbleSort", arr)
                cv2.waitKey(int(1000/fps))


                if cv2.waitKey(10) & 0xFF == ord('q'):
                    done = True
                    break
        return done


    def bubbleRun(self, show=False, scale=10, fps=1000):
        done = False
        sorted_index = 0

        while sorted_index < len(self.unsortedList):
            done = self.bubbleOnce(sorted_index, show, scale, fps)
            sorted_index += 1
            if done:
                break

    def toImg(self, scale=10):
        arr = np.zeros((self.unsortedList.shape[0], self.MAX))
        for i in range(self.unsortedList.shape[0]):
            val = self.unsortedList[i]
            arr[i] = ((np.arange(self.MAX) < val) * 140) + ((np.arange(self.MAX) == val) * 0) + ((np.arange(self.MAX) > val) * 240)


        arr = arr.repeat(3).reshape((self.unsortedList.shape[0], self.MAX, 3))
        arr = cv2.resize(arr, dsize=(int(arr.shape[1] * scale), int(arr.shape[0] * scale)), interpolation=0)
        arr = np.rot90(arr)

        return arr.astype(np.uint8)


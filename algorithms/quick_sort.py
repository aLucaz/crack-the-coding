class QuickSort:

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def execute(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self.execute(arr, low, pi - 1)
            self.execute(arr, pi + 1, high)


if __name__ == '__main__':
    s = QuickSort()
    arr = [4, 2, 6, 1, 0]
    s.execute(arr, 0, len(arr) - 1)
    print(arr)

import timeit
import random
import matplotlib.pyplot as mat_plot_library

def mergeSort(arr):
    if len(arr) > 1:
        middle_of_array = len(arr) // 2         # split the array into two halves
        left_side = arr[:middle_of_array]       # left side of the array is stores in left_side array
        right_side = arr[middle_of_array:]      # right side of the array is stores in right_side array

        mergeSort(left_side)
        mergeSort(right_side)

        x = 0
        y = 0
        z = 0

        while x < len(left_side) and y < len(right_side):
            if left_side[x] <= right_side[y]:
                arr[z] = left_side[x]
                x += 1
            elif left_side[x] > right_side[y]:
                arr[z] = right_side[y]
                y += 1
            z += 1

        while x < len(left_side):
            arr[z] = left_side[x]
            x += 1
            z += 1

        while y < len(right_side):
            arr[z] = right_side[y]
            y += 1
            z += 1

def input(startNum, endNum, arr):
    for i in range(startNum, endNum):
        # maxNum = random.randint(0, 1)                             # returns an error
        # maxNum = numPy.random.normal(0,1,1)                       # returns an error
        maxNum = pow(2, 16)
        randomNum = random.randrange(startNum, maxNum)
        arr.append(randomNum)
    return arr

if __name__ == '__main__':

    start_time = 0
    end_time = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    elapsed_time = []

    for i in end_time:
        array_input = []
        array_input = input(start_time, i, array_input)

        start_timer = timeit.default_timer()
        mergeSort(array_input)
        elapsed_time.append(timeit.default_timer() - start_timer)

    mat_plot_library.title("Merge Sort Algorithm: ")
    mat_plot_library.xlabel("Number of Inputs: ")
    mat_plot_library.ylabel("Amount of Time: ")
    mat_plot_library.plot(end_time, elapsed_time)
    mat_plot_library.show()






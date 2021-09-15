import timeit
import random
import matplotlib.pyplot as mat_plot_library
import numpy as numPy


def insertion_sort(bucket):
    for x in range(1, len(bucket)):
        var = bucket[x]
        y = x - 1
        while var < bucket[y] and y >= 0:
            bucket[y + 1] = bucket[y]
            y = y - 1
        bucket[y + 1] = var


def bucketSort(bucketSort_input_arr):
    maximumValue = max(bucketSort_input_arr)
    length_of_list = maximumValue / len(bucketSort_input_arr)

    array_buckets = []
    for x in range(len(bucketSort_input_arr)):       # an array of buckets where length is equal to array_input
        array_buckets.append([])

    for i in range(len(bucketSort_input_arr)):
        j = int(bucketSort_input_arr[i] / length_of_list)       # buckets will be arranged based off its size
        if j == len(bucketSort_input_arr):
            array_buckets[len(bucketSort_input_arr) - 1].append(bucketSort_input_arr[i])
        elif j != len(bucketSort_input_arr):
            array_buckets[j].append(bucketSort_input_arr[i])

    for z in range(len(bucketSort_input_arr)):              # using insertion sort to sort within the buckets
        insertion_sort(array_buckets[z])

    output = []
    for x in range(len(bucketSort_input_arr)):
        output = output + array_buckets[x]
    return output


def input(startNum, endNum, arr):
    for i in range(startNum, endNum):
        # maxNum = random.randint(0, 1)                             # returns an error
        # maxNum = numPy.random.normal(0,1,1)                       # returns an error
        # maxNum = random.random()                                  # returns an error
        maxNum = pow(2, 16)
        randomNum = random.randrange(startNum, maxNum)
        arr.append(randomNum)
    return arr


if __name__ == '__main__':

    start_time = 0
    end_time = [10, 50, 100, 500, 1000, 5000]
    elapsed_time = []

    for i in end_time:
        array_input = []
        array_input = input(start_time, i, array_input)

        start_timer = timeit.default_timer()
        bucketSort(array_input)
        elapsed_time.append(timeit.default_timer() - start_timer)

    mat_plot_library.title("Bucket Sort Algorithm: ")
    mat_plot_library.xlabel("Number of Inputs: ")
    mat_plot_library.ylabel("Amount of Time: ")
    mat_plot_library.plot(end_time, elapsed_time)
    mat_plot_library.show()






def heapify(unsorted_list, index, heap_size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and unsorted_list[left] > unsorted_list[largest]:
        largest = left

    if right < heap_size and unsorted_list[right] > unsorted_list[largest]:
        largest = right

    if largest is not index:
        unsorted_list[largest], unsorted_list[index] = unsorted_list[index], unsorted_list[largest]
        heapify(unsorted_list, largest, heap_size)

    return unsorted_list


def heap_sort(unsorted_list):
    heap_size = len(unsorted_list)

    for i in range(heap_size // 2 - 1, -1, -1):
        heapify(unsorted_list, i, heap_size)

    for i in range(heap_size - 1, 0, -1):
        #swap(unsorted_list[0], unsorted_list[i])
        unsorted_list[0], unsorted_list[i] = unsorted_list[i], unsorted_list[0]
        heapify(unsorted_list, 0, i)

    return unsorted_list

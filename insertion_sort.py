def insertion_sort_descending(arr):
    """
    Sorts the input array in-place in decreasing order using insertion sort.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements that are smaller than key one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    # Example array
    numbers = [12, 4, 56, 17, 8, 99]
    print("Original array:", numbers)
    insertion_sort_descending(numbers)
    print("Sorted array (decreasing):", numbers)

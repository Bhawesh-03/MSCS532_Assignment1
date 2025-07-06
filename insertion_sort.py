"""
Insertion Sort Algorithm - Monotonically Decreasing Order

Author: Bhawesh
Course: MSCS532
Assignment 1
"""

def insertion_sort_descending(arr):
    """
    Sorts an array in-place in monotonically decreasing order.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    # Take input from the user
    user_input = input("Enter numbers separated by spaces: ")
    # Convert input string to list of integers
    arr = [int(x) for x in user_input.strip().split()]
    print("Original array:", arr)
    sorted_arr = insertion_sort_descending(arr)
    print("Sorted in decreasing order:", sorted_arr)

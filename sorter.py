import time

def bubble_sort(arr):
    # Get the length of the list
    n = len(arr)

    # Iterate over the list multiple times
    for i in range(n):
        # Set a flag to track whether any swaps were made
        swaps_made = False

        # Iterate over the list again, comparing each element with its neighbor
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements if the first element is larger than the second
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps_made = True

        # If no swaps were made, the list is already sorted, so we can exit the loop
        if not swaps_made:
            break
    
    # Return the sorted list
    return arr

def insertion_sort(arr):
    # Get the length of the list
    n = len(arr)

    # Iterate over the list
    for i in range(1, n):
        # Get the current element
        current = arr[i]

        # Set the position where the current element should be inserted
        position = i

        # Shift elements to the right until the correct position for the current element is found
        while position > 0 and arr[position - 1] > current:
            arr[position] = arr[position - 1]
            position -= 1

        # Insert the current element at the correct position
        arr[position] = current
    
    # Return the sorted list
    return arr

def merge_sort(arr):
    # If the list has fewer than 2 elements, it is already sorted
    if len(arr) < 2:
        return arr

    # Split the list in half
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort the left and right halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted left and right halves
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left or right halves
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    # Return the merged, sorted list
    return merged

def selection_sort(arr):
    # Get the length of the list
    n = len(arr)

    # Iterate over the list
    for i in range(n):
        # Find the position of the minimum element
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    # Return the sorted list
    return arr

def main():
    # Prompt the user for the number of items they want to enter into the array
    num_items = int(input("Enter the number of items you want to enter into the array: "))

    # Prompt the user to specify whether they want the numbers in the array to be random
    random_numbers = input("Do you want the numbers in the array to be random (y/n)? ")

    # Initialize the array
    arr = []

    # If the user wants random numbers, generate the specified number of random numbers
    if random_numbers.lower() == "y":
        import random
        for i in range(num_items):
            arr.append(random.randint(1, 1000000000))
    else:
        # Prompt the user to enter each item
        print("Enter the items one by one:")
        for i in range(num_items):
            item = input()
            arr.append(item)

    # Sort the array using the four sorting algorithms
    start = time.perf_counter()
    bubble_sorted = bubble_sort(arr)
    end = time.perf_counter()
    bubble_time = end - start

    start = time.perf_counter()
    insertion_sorted = insertion_sort(arr)
    end = time.perf_counter()
    insertion_time = end - start

    start = time.perf_counter()
    merge_sorted = merge_sort(arr)
    end = time.perf_counter()
    merge_time = end - start

    start = time.perf_counter()
    selection_sorted = selection_sort(arr)
    end = time.perf_counter()
    selection_time = end - start

    # Print the sorted lists and the time taken to sort them
    print("Bubble sort:", bubble_sorted)
    print("Time taken:", bubble_time)
    print("Insertion sort:", insertion_sorted)
    print("Time taken:", insertion_time)
    print("Merge sort:", merge_sorted)
    print("Time taken:", merge_time)
    print("Selection sort:", selection_sorted)
    print("Time taken:", selection_time)

    # Determine which sorting algorithm is the most optimized
    if bubble_sorted == insertion_sorted == merge_sorted == selection_sorted:
        print("All four sorting methods produced the same result.")
    else:
        sorted_lists = [bubble_sorted, insertion_sorted, merge_sorted, selection_sorted]
        sorting_methods = ["bubble sort", "insertion sort", "merge sort", "selection sort"]
        fastest_method = sorting_methods[sorted_lists.index(min(sorted_lists, key=len))]
        print("The most optimized sorting method is:", fastest_method)

if __name__ == "__main__":
    main()

# Merge Sort Function
def merge_sort(arr):
    if len(arr) > 1:
        # Divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call to sort each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0

        # Compare elements and merge
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements from the left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements from the right half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Driver code

# Input array
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original Array:", arr)
    
# Apply Merge Sort
merge_sort(arr)
    
# Output the sorted array
print("Sorted Array:", arr)
"""
*Complexity: O(nlogn)*
Implemented through **Recursion**
Based on the divide and conquer rule. Split the array in the half and then sort based on the values. 
This is a recursive fucntion where we split the array until it remains as a single element array 
followed by the merging the elements in a sorted fashion
Python sort() function uses Timsort() which is the combinition of both merge sort and insertion sort.

"""

#Defining the array split
def merge_sort(arr):
  if len(arr) <= 1:
    return arr

  mid_index = len(arr) // 2
  left = arr[:mid_index]
  right = arr[mid_index: ]

  left = merge_sort(left)
  right = merge_sort(right)

  return merge_arrays(left, right)

# Defining the merge function here
def merge_arrays(arr1, arr2):
  merged_array = []
  n1, n2 = len(arr1), len(arr2)
  i = j = 0
  while i < n1 and j < n2:
    if arr1[i] <= arr2[j]:
      merged_array.append(arr1[i])
      i += 1
    else:
      merged_array.append(arr2[j])
      j += 1
  while i < n1:
    merged_array.append(arr1[i])
    i += 1
  while j < n2:
    merged_array.append(arr2[j])
    j += 1

  return merged_array

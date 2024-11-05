
"""
## Counting Sort
*Complexity: O(n)*

*Linear time sorting algorithm*

It assumes that all the elements in the known range and have some form of repetition. 
If there is no repetition or the range of the elements is not within a specified bound, then this becomes the in-efficient sorting algo because of space complexity. 
Time complexity will also be affected compared to other algorithms since it will take more time to iterate through the commulative sum array.

The cumulative sum array shows the position of each element at the index in the sorted array.
For example, if we have the following array:
```
elements = [2, 4, 2, 1, 0]
count = [1, 1, 2, 0, 1]
commulative_array = [1, 2, 4, 4, 5]
```
Now in the commulative array, commulative_array[0] = 1 means that value/entry 0 should be placed at index 0 
starting the index with 0. commulative_array[1] = 2 shows that 1 should be placed at index 1 and go upto index 1 only 
since we have only one 1. commulative_array[2] = 4 means that 2 should be placed upto index 3 
and commulative_array[3] = 4 is irrelevant since 3 does not exist in the original array
"""


def counting_sort(arr):
  sorted_arr = [0 for i in range(len(arr))]
  freq_arr = [0 for i in range(max(arr)+1)]

  for i in range(len(arr)):
    freq_arr[arr[i]] += 1

  for i in range(1, len(freq_arr)):
    freq_arr[i] += freq_arr[i-1]

  for i in range(len(arr)-1, -1, -1): ## Since python indexing starts at 0, so we have to subtract 1 from here
    sorted_arr[freq_arr[arr[i]]-1] = arr[i]
    freq_arr[arr[i]] -= 1

  return sorted_arr

"""
## Quick Sort
*Complexity: O(nlogn)*

In case of extremely skewed data, the complexity becomes (O(n^2))

This algorithm is considered as one of the top 10 out of 20 algorithms. This algorithm is also based on the Divide and Conquer Rule.

"""

def swap_elements(start, end, elements):
  temp = elements[start]
  elements[start] = elements[end]
  elements[end] = temp

def partition(elements, start, end):
  pivot_index = start
  pivot = elements[pivot_index]

  start = pivot_index + 1
  end = len(elements) - 1

  while start < end:
    while start < len(elements) and elements[start] <= pivot:
      start += 1
    while elements[end] > pivot:
      end -= 1

    if start < end:
      swap_elements(start, end, elements)

  swap_elements(pivot_index, end, elements)

  return end

def quick_sort(arr, start, end):
  if start > end:
    return
  partition_index = partition(arr, start, end)
  quick_sort(arr, 0, partition_index-1)
  quick_sort(arr, partition_index + 1, end)
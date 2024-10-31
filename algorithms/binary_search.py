## Linear search Algo
def linear_search(number_list, findnumber):
  for i in range(len(number_list)):
      if findnumber == number_list[i]:
        return i
  return -1

"""
Binary Search assumes that all the elements in the given array/list are sorted.
The sorted form of the array is the ascending order of the array sorting. 
It then splits the array in half subsequently to find the number being searched.

1. Iterative Search:
    It iteratively goes through all the list/array and then keeps on splitting the array
    until the relevant entry is found. 

2. Recursive Search:
    Remove the iteration loop and replace it with recursive search.
    Define a base case and re-call the function again to recursively search for the number

"""

## Binary Search - Iterative
def binary_iterative(number_list, findnumber):
  left_index = 0
  right_index = len(number_list) - 1

  while left_index <= right_index:
    mid_index = (left_index + right_index)//2

    if findnumber == number_list[mid_index]:
      return mid_index

    if findnumber <= number_list[mid_index]:
      right_index = mid_index - 1
    else:
      left_index = mid_index + 1

  return -1


## Binary Search - Recursive
def binary_recursive(number_list, findnumber):
  def helper(number_list, findnumber, left_index, right_index):
    mid_index = (left_index + right_index) // 2

    if findnumber == number_list[mid_index]:
      return mid_index

    if findnumber < number_list[mid_index]:
      right_index = mid_index - 1
    else:
      left_index = mid_index + 1

    return helper(number_list, findnumber, left_index, right_index)

  return helper(number_list, findnumber, 0, len(number_list))
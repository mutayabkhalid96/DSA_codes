"""
## Exercise for Merge sort
Modify merge_sort function such that it can sort following list of athletes as per the time taken by them in the marathon.
```
elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
```
Merge_sort function should take key from an athlete's marathon log and sort the list as per that key. For example,

```
merge_sort(elements, key='time_hours', descending=True)
```

##Solution:
This solution is a bit different from the algorithm described above. It uses while loop to iterate through the lists

"""

#Defining the array split
def merge_sort(arr, key, descending = False):
  if len(arr) <= 1:
    return arr

  mid_index = len(arr) // 2
  left = arr[:mid_index]
  right = arr[mid_index: ]

  left = merge_sort(left, key, descending)
  right = merge_sort(right, key, descending)

  return merge_arrays(left, right, key, descending)

# Defining the merge function here
def merge_arrays(arr1, arr2, key, descending):
  merged_array = []
  n1, n2 = len(arr1), len(arr2)
  i = j = 0
  if not descending:
    while len(arr1) > 0 and len(arr2) > 0:
      if arr1[0][key] <= arr2[0][key]:
        merged_array.append(arr1.pop(0))
      else:
        merged_array.append(arr2.pop(0))
  else:
    while len(arr1) > 0 and len(arr2) > 0:
      if arr1[0][key] >= arr2[0][key]:
        merged_array.append(arr1.pop(0))
      else:
        merged_array.append(arr2.pop(0))

  merged_array.extend(arr1)
  merged_array.extend(arr2)

  return merged_array
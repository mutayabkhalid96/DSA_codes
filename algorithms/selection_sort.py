## Implementation by selecting the minimum number and then swapping its position
def selection_sort(numbers_list):
  for i in range(len(numbers_list)):
    min = i
    for j in range(i+1, len(numbers_list)):
      if numbers_list[j] < numbers_list[min]:
        min = j

    temp = numbers_list[i]
    numbers_list[i] = numbers_list[min]
    numbers_list[min] = temp

  return numbers_list
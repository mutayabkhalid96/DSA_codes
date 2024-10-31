def insertion_sort(numbers_list):
  for i in range(1, len(numbers_list)):
    key = numbers_list[i]
    j = i - 1
    while j >= 0 and numbers_list[j] > key:
      numbers_list[j+1] = numbers_list[j]
      j = j - 1
    numbers_list[j+1] = key

  return numbers_list
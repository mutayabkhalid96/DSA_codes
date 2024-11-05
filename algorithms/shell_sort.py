def shell_sort(numbers_list):
  size = len(numbers_list)
  gap = size // 2

  while gap > 0:
    for i in range(gap, size):
      key = numbers_list[i]
      j = i
      while j >= gap and numbers_list[j-gap] > key:
        numbers_list[j] = numbers_list[j-gap]
        j = j - gap

      numbers_list[j] = key
    gap = gap // 2
  return numbers_list
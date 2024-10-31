def bubble_sort(numbers_list):
  for i in range(len(numbers_list)):
    for j in range(1, len(numbers_list)-i):
      if numbers_list[j-1] > numbers_list[j]:
        temp = numbers_list[j]
        numbers_list[j] = numbers_list[j-1]
        numbers_list[j-1] = temp
  return numbers_list